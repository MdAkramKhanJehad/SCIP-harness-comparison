# vvaharness/orchestrator/entry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/entry.py.evidence.json`. SHA-256: `b90a3ff0639aec11559a5eab4228580729ec3fdca1daf89ce3ae51e928ae05f6`.

```sudo
// Source: vvaharness/orchestrator/entry.py:14-19
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Retain source documentation literal source_literal_17_0; it is not a model call. Then Resolve source import import argparse; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/entry.py:20-25
In source order: Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import import traceback; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import AuthenticationError, ProxyError; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/entry.py:26-32
In source order: Resolve source import from vvaharness.backends.llm.registry import resolve as resolve_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.errors import EVInputError, EVUnreachableError; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.options import collection_path as ev_collection_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.options import load_options as ev_load_options; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.options import may_run as ev_may_run; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/entry.py:33-44
In source order: Resolve source import from vvaharness.exploit_verification.options import resolution_error as ev_resolution_error; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.batch import run_batch; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.cmdb import _cmdb_path, _set_cmdb_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import EV_MODEL_ROLES, _default_config, _iter_model_roles, trusted_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.preflight import check_backends, configure_backends; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/entry.py:45-49
In source order: Resolve source import from vvaharness.orchestrator.scan import scan_repo; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.store import StoreError; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import EmptyScopeError; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/entry.py:50-54
In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.pricing import load_pricing_cached; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/entry.py:56-60
for each _s in (sys.stdout, sys.stderr) {
  // Source: vvaharness/orchestrator/entry.py:57-60
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/entry.py:58-58
    In source order: Evaluate _s.reconfigure(encoding='utf-8'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/entry.py:59-60
  On the first matching source exception (AttributeError, ValueError), in handler order {
    // Source: vvaharness/orchestrator/entry.py:60-60
    In source order: Perform no operation at this source statement.
  }
}
// Source: vvaharness/orchestrator/entry.py:63-69
// Source signature: _top_arg(raw: str)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _top_arg(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/entry.py:64-65
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent.select import _coerce_top_value; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/entry.py:66-69
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/entry.py:67-67
    End this invocation with _coerce_top_value(raw, source='--top').
  }
  // Source: vvaharness/orchestrator/entry.py:68-69
  On the first matching source exception ValueError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:69-69
    Raise argparse.ArgumentTypeError(str(e)).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/entry.py:72-100
// Source signature: _ev_gate(args, cfg) -> tuple[int | None, object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_gate(args, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/entry.py:73-75
  In source order: Retain source documentation literal source_literal_73_4; it is not a model call. Then Evaluate once ev_collection_path(os.environ); assign in source target order to path.
  // Source: vvaharness/orchestrator/entry.py:76-82
  if (the source predicate not path is truthy) {
    // Source: vvaharness/orchestrator/entry.py:77-81
    if (the source predicate getattr(args, 'stop_after', None) == 'ev' and (not getattr(args, 'resume', False)) is truthy) {
      // Source: vvaharness/orchestrator/entry.py:79-80
      In source order: Evaluate log.error("--stop-after ev requires EV_API_COLLECTION to be set (or --resume, to re-probe this run's checkpointed collection)"); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:81-81
      End this invocation with (2, None).
    }
    // Source: vvaharness/orchestrator/entry.py:82-82
    End this invocation with (None, None).
  }
  // Source: vvaharness/orchestrator/entry.py:83-85
  if (the source predicate config_mod.is_network_path(path) is truthy) {
    // Source: vvaharness/orchestrator/entry.py:84-84
    In source order: Evaluate log.error(Event.EV_COLLECTION_NOT_LOCAL, path=path); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:85-85
    End this invocation with (2, None).
  }
  // Source: vvaharness/orchestrator/entry.py:86-90
  if (the source predicate args.repo_file is truthy) {
    // Source: vvaharness/orchestrator/entry.py:88-89
    In source order: Evaluate log.warning('exploit verification is single-repo only; ignoring EV_API_COLLECTION for this batch (--repo-file) run.'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:90-90
    End this invocation with (None, None).
  }
  // Source: vvaharness/orchestrator/entry.py:91-91
  In source order: Resolve source import from vvaharness.exploit_verification import gate as ev_gate; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/entry.py:92-96
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/entry.py:93-93
    In source order: Evaluate once ev_gate.run_gate(ev_load_options(cfg, os.environ)); assign in source target order to result.
  }
  // Source: vvaharness/orchestrator/entry.py:94-96
  On the first matching source exception EVInputError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:95-95
    In source order: Evaluate console.mark('fail', source_template_95_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:96-96
    End this invocation with (2, None).
  }
  // Source: vvaharness/orchestrator/entry.py:97-99
  if (the source predicate result.enabled is truthy) {
    // Source: vvaharness/orchestrator/entry.py:98-99
    In source order: Evaluate console.write('  [exploit-verification] collection gate:'); retain side effects and discard the expression result. Then Evaluate console.write(ev_gate.format_checks(result.checks)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/entry.py:100-100
  End this invocation with (None, result.collection).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/entry.py:103-113
// Source signature: _resolve_auto_step1(flag: bool, cfg, disable: bool=False) -> tuple[bool, str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_auto_step1(flag, cfg, disable) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/entry.py:105-105
  In source order: Retain source documentation literal source_literal_105_4; it is not a model call.
  // Source: vvaharness/orchestrator/entry.py:106-107
  if (the source predicate disable is truthy) {
    // Source: vvaharness/orchestrator/entry.py:107-107
    End this invocation with (False, '--no-auto-step1').
  }
  // Source: vvaharness/orchestrator/entry.py:108-109
  if (the source predicate flag is truthy) {
    // Source: vvaharness/orchestrator/entry.py:109-109
    End this invocation with (True, '--auto-step1').
  }
  // Source: vvaharness/orchestrator/entry.py:110-110
  In source order: Evaluate once getattr(cfg, 'step1', None); assign in source target order to step1.
  // Source: vvaharness/orchestrator/entry.py:111-112
  if (the source predicate bool(getattr(step1, 'auto_exclude', False)) is truthy) {
    // Source: vvaharness/orchestrator/entry.py:112-112
    End this invocation with (True, 'step1.auto_exclude').
  }
  // Source: vvaharness/orchestrator/entry.py:113-113
  End this invocation with (False, None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/entry.py:116-120
// Source signature: _repo_name(repo: Path, explicit: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repo_name(repo, explicit) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/entry.py:117-117
  In source order: Retain source documentation literal source_literal_117_4; it is not a model call.
  // Source: vvaharness/orchestrator/entry.py:118-119
  if (the source predicate explicit and explicit.strip() is truthy) {
    // Source: vvaharness/orchestrator/entry.py:119-119
    End this invocation with explicit.strip().
  }
  // Source: vvaharness/orchestrator/entry.py:120-120
  End this invocation with repo.resolve().name or 'repo'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/entry.py:123-137
// Source signature: _pricing_note(cfg) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pricing_note(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/entry.py:124-125
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call. Then Evaluate once getattr(getattr(cfg, 'pricing', None), 'file', None); assign in source target order to file.
  // Source: vvaharness/orchestrator/entry.py:126-127
  if (the source predicate file is None is truthy) {
    // Source: vvaharness/orchestrator/entry.py:127-127
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/entry.py:128-128
  In source order: Evaluate once load_pricing_cached(file); assign in source target order to table.
  // Source: vvaharness/orchestrator/entry.py:129-131
  if (the source predicate table is None is truthy) {
    // Source: vvaharness/orchestrator/entry.py:131-131
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/entry.py:132-133
  In source order: Evaluate once {resolve_model(m)[0] for _, m in _iter_model_roles(cfg)}; assign in source target order to role_model_ids. Then Evaluate once set(role_model_ids) - table.models.keys(); assign in source target order to missing.
  // Source: vvaharness/orchestrator/entry.py:134-135
  if (the source predicate not missing is truthy) {
    // Source: vvaharness/orchestrator/entry.py:135-135
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/entry.py:136-137
  End this invocation with source_template_136_12.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/entry.py:140-223
// Source signature: build_parser() -> argparse.ArgumentParser
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_parser() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/entry.py:141-152
  In source order: Retain source documentation literal source_literal_141_4; it is not a model call. Then Evaluate once argparse.ArgumentParser(prog='vvaharness scan', description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); assign in source target order to ap. Then Evaluate once ap.add_mutually_exclusive_group(required=True); assign in source target order to src. Then Evaluate src.add_argument('--repo', help='path to a single local target codebase'); retain side effects and discard the expression result. Then Evaluate src.add_argument('--repo-file', help=source_literal_147_26); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/entry.py:153-166
  In source order: Evaluate ap.add_argument('--config', default=None, help='config profile path (else the auto-detected ./config.yaml, or the packaged default)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--repo-name', help='module / repositoryName tag for report filenames and SARIF run.properties (single-repo mode only; default: dir name)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--application-id', help='application/asset ID — drives CMDB AppProfile lookup, VulContextSeverity scoring, and SARIF run.properties.applicationId'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--workspace', default='./batch-workspace', help='directory to clone remote repos into (batch mode)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--keep-clones', action='store_true', help='do not delete cloned repos after scanning (batch mode)'); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/entry.py:167-190
  In source order: Evaluate ap.add_argument('--group-by-app', action='store_true', help=source_literal_168_25); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--resume', action='store_true', help='reuse existing checkpoints for completed steps'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--stop-after', choices=['clone', 'ev', 's0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11'], help=source_literal_177_25); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--s6-progress-file', action='store_true', help='write state/s6_progress/<run_id>/s6_progress.json after each S6 verification'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--remediate', action='store_true', help=source_literal_186_25); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/entry.py:191-209
  In source order: Evaluate ap.add_argument('--top', type=_top_arg, default=None, metavar='N|all', help=source_literal_192_25); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--force', action='store_true', help='override safety refusals (currently: the s10 git-SHA staleness check)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--skip-preflight', action='store_true', help='skip the startup credential/backend readiness probe (does NOT bypass model/API authentication)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--step1-config', help=source_literal_205_25); retain side effects and discard the expression result. Then Evaluate once ap.add_mutually_exclusive_group(); assign in source target order to auto_grp.
  // Source: vvaharness/orchestrator/entry.py:210-222
  In source order: Evaluate auto_grp.add_argument('--auto-step1', action='store_true', help=source_literal_211_25); retain side effects and discard the expression result. Then Evaluate auto_grp.add_argument('--no-auto-step1', action='store_true', help=source_literal_218_25); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/entry.py:223-223
  End this invocation with ap.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/entry.py:226-405
// Source signature: main(argv: list[str] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn main(argv) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/entry.py:227-228
  In source order: Evaluate once build_parser(); assign in source target order to ap. Then Evaluate once ap.parse_args(argv); assign in source target order to args.
  // Source: vvaharness/orchestrator/entry.py:230-241
  if (the source predicate not args.repo_file is truthy) {
    // Source: vvaharness/orchestrator/entry.py:231-233
    In source order: Resolve source import from stat import S_ISDIR; preserve alias and import-time effects. Then Evaluate once Path(args.repo); assign in source target order to repo.
    // Source: vvaharness/orchestrator/entry.py:234-241
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/entry.py:235-237
      if (the source predicate not S_ISDIR(repo.stat().st_mode) is truthy) {
        // Source: vvaharness/orchestrator/entry.py:236-236
        In source order: Evaluate log.error(Event.REPO_NOT_A_DIRECTORY, path=repo); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/entry.py:237-237
        End this invocation with 2.
      }
      // Source: vvaharness/orchestrator/entry.py:238-238
      In source order: Evaluate once _repo_name(repo, args.repo_name); assign in source target order to repo_name.
    }
    // Source: vvaharness/orchestrator/entry.py:239-241
    On the first matching source exception (OSError, ValueError), in handler order {
      // Source: vvaharness/orchestrator/entry.py:240-240
      In source order: Evaluate log.error(Event.REPO_NOT_A_DIRECTORY, path=repo); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:241-241
      End this invocation with 2.
    }
  }
  // Source: vvaharness/orchestrator/entry.py:244-244
  In source order: Evaluate once args.config is not None; assign in source target order to config_explicit.
  // Source: vvaharness/orchestrator/entry.py:245-246
  if (the source predicate not config_explicit is truthy) {
    // Source: vvaharness/orchestrator/entry.py:246-246
    In source order: Evaluate once str(_default_config()); assign in source target order to args.config.
  }
  // Source: vvaharness/orchestrator/entry.py:247-247
  In source order: Evaluate once args.repo; assign in source target order to boundary.
  // Source: vvaharness/orchestrator/entry.py:248-253
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/entry.py:249-250
    In source order: Evaluate once trusted_config(args.config, boundary, explicit=config_explicit); assign in source target order to args.config. Then Evaluate once config_mod.load(args.config); assign in source target order to cfg.
  }
  // Source: vvaharness/orchestrator/entry.py:251-253
  On the first matching source exception config_mod.ConfigPolicyError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:252-252
    In source order: Evaluate log.error(Event.CONFIG_POLICY_REFUSED, detail=str(e)); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:253-253
    End this invocation with 2.
  }
  // Source: vvaharness/orchestrator/entry.py:254-255
  if (the source predicate args.s6_progress_file is truthy) {
    // Source: vvaharness/orchestrator/entry.py:255-255
    In source order: Evaluate once True; assign in source target order to cfg.step6_verify.progress_file.
  }
  // Source: vvaharness/orchestrator/entry.py:256-260
  In source order: Evaluate once Path(args.config); assign in source target order to cfg_path. Then Evaluate once cfg_path.resolve().parent; assign in source target order to cfg_dir. Then Evaluate once 'config.yaml' if cfg_path.resolve() == (Path.cwd() / 'config.yaml').resolve() else str(cfg_path); assign in source target order to cfg_display. Then Evaluate console.write(source_template_259_18); retain side effects and discard the expression result. Then Evaluate _set_cmdb_path(cfg, cfg_dir); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/entry.py:263-264
  In source order: Evaluate once _resolve_auto_step1(args.auto_step1, cfg, disable=args.no_auto_step1); assign in source target order to (args.auto_step1, auto_step1_src).
  // Source: vvaharness/orchestrator/entry.py:265-267
  if (the source predicate args.no_auto_step1 is truthy) {
    // Source: vvaharness/orchestrator/entry.py:266-267
    In source order: Evaluate console.write('  step1 overlay: --no-auto-step1 (AI auto-exclude disabled, overriding any config default)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/entry.py:269-293
  if (the source predicate args.step1_config is truthy) {
    // Source: vvaharness/orchestrator/entry.py:270-272
    if (the source predicate config_mod.is_network_path(args.step1_config) is truthy) {
      // Source: vvaharness/orchestrator/entry.py:271-271
      In source order: Evaluate log.error(Event.CONFIG_PATH_NOT_LOCAL, flag='--step1-config', path=args.step1_config); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:272-272
      End this invocation with 2.
    }
    // Source: vvaharness/orchestrator/entry.py:273-273
    In source order: Evaluate once Path(args.step1_config); assign in source target order to s1_path.
    // Source: vvaharness/orchestrator/entry.py:274-278
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/entry.py:275-275
      In source order: Evaluate once config_mod.apply_step1_overlay(cfg, s1_path); assign in source target order to (cfg, s1_applied).
    }
    // Source: vvaharness/orchestrator/entry.py:276-278
    On the first matching source exception (config_mod.ConfigPolicyError, ValueError) as e, in handler order {
      // Source: vvaharness/orchestrator/entry.py:277-277
      In source order: Evaluate log.error(Event.STEP1_OVERLAY_REFUSED, path=s1_path, detail=str(e)); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:278-278
      End this invocation with 2.
    }
    // Source: vvaharness/orchestrator/entry.py:279-281
    if (the source predicate not s1_applied is truthy) {
      // Source: vvaharness/orchestrator/entry.py:280-280
      In source order: Evaluate log.error(Event.STEP1_OVERLAY_NOT_FOUND, path=s1_path); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:281-281
      End this invocation with 2.
    }
    // Source: vvaharness/orchestrator/entry.py:282-286
    In source order: Evaluate once cfg._data.get('step1', {}); assign in source target order to s1. Then Evaluate console.write(source_template_283_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:287-290
    if (the source predicate args.auto_step1 is truthy) {
      // Source: vvaharness/orchestrator/entry.py:288-290
      In source order: Evaluate console.write(source_template_288_26); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to args.auto_step1.
    }
  }
  else {
    // Source: vvaharness/orchestrator/entry.py:291-293
    if (the source predicate args.auto_step1 is truthy) {
      // Source: vvaharness/orchestrator/entry.py:292-293
      In source order: Evaluate console.write(source_template_292_22); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/entry.py:296-296
  In source order: Evaluate once _cmdb_path(); assign in source target order to _cmdb.
  // Source: vvaharness/orchestrator/entry.py:297-299
  if (the source predicate not _cmdb or not os.path.isfile(_cmdb) is truthy) {
    // Source: vvaharness/orchestrator/entry.py:298-299
    In source order: Evaluate once _cmdb or 'inject.cmdb_file unset'; assign in source target order to _where. Then Evaluate log.warning(Event.CMDB_MISSING, path=_where); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/entry.py:301-301
  In source order: Evaluate once _pricing_note(cfg); assign in source target order to _pricing_warning.
  // Source: vvaharness/orchestrator/entry.py:302-303
  if (the source predicate _pricing_warning is truthy) {
    // Source: vvaharness/orchestrator/entry.py:303-303
    In source order: Evaluate console.write(_pricing_warning); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/entry.py:305-308
  In source order: Evaluate configure_backends(cfg, cfg_dir); retain side effects and discard the expression result. Then Evaluate once ev_resolution_error(cfg, args); assign in source target order to _ev_err.
  // Source: vvaharness/orchestrator/entry.py:309-311
  if (the source predicate _ev_err is truthy) {
    // Source: vvaharness/orchestrator/entry.py:310-310
    In source order: Evaluate log.error(Event.EV_RESOLUTION_CONFLICT, detail=_ev_err); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:311-311
    End this invocation with 2.
  }
  // Source: vvaharness/orchestrator/entry.py:314-314
  In source order: Evaluate once _ev_gate(args, cfg); assign in source target order to (rc, ev_collection_in).
  // Source: vvaharness/orchestrator/entry.py:315-316
  if (the source predicate rc is not None is truthy) {
    // Source: vvaharness/orchestrator/entry.py:316-316
    End this invocation with rc.
  }
  // Source: vvaharness/orchestrator/entry.py:319-338
  if (the source predicate not args.skip_preflight and args.stop_after not in ('clone', 'ev') is truthy) {
    // Source: vvaharness/orchestrator/entry.py:321-326
    In source order: For _skip, assign set(() if not args.repo_file and ev_may_run(cfg, os.environ) else EV_MODEL_ROLES); source annotation set[str]. Then Evaluate once getattr(cfg, 'step_remediate', None); assign in source target order to _rem_cfg. Then Evaluate once bool(getattr(args, 'remediate', False) or getattr(_rem_cfg, 'enabled', False)); assign in source target order to _rem_on.
    // Source: vvaharness/orchestrator/entry.py:327-328
    if (the source predicate not (args.stop_after in (None, 's10', 's11') and _rem_on) is truthy) {
      // Source: vvaharness/orchestrator/entry.py:328-328
      In source order: Evaluate _skip.add('remediate'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/entry.py:329-330
    In source order: Evaluate once getattr(cfg, 'step_validate', None); assign in source target order to _val_cfg. Then Evaluate once bool(getattr(_val_cfg, 'enabled', False)); assign in source target order to _val_on.
    // Source: vvaharness/orchestrator/entry.py:331-332
    if (the source predicate not (args.stop_after in (None, 's11') and _val_on) is truthy) {
      // Source: vvaharness/orchestrator/entry.py:332-332
      In source order: Evaluate _skip.add('validate'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/entry.py:333-338
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/entry.py:334-335
      if (the source predicate not check_backends(cfg, skip_roles=_skip) is truthy) {
        // Source: vvaharness/orchestrator/entry.py:335-335
        End this invocation with 1.
      }
    }
    // Source: vvaharness/orchestrator/entry.py:336-338
    On the first matching source exception KeyboardInterrupt, in handler order {
      // Source: vvaharness/orchestrator/entry.py:337-337
      In source order: Evaluate console.mark('fail', 'scan aborted by user (Ctrl-C).', indent=2, lead=source_literal_337_82); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:338-338
      End this invocation with 130.
    }
  }
  // Source: vvaharness/orchestrator/entry.py:340-350
  if (the source predicate args.repo_file is truthy) {
    // Source: vvaharness/orchestrator/entry.py:341-341
    In source order: Evaluate once Path(args.repo_file); assign in source target order to list_file.
    // Source: vvaharness/orchestrator/entry.py:342-344
    if (the source predicate not list_file.is_file() is truthy) {
      // Source: vvaharness/orchestrator/entry.py:343-343
      In source order: Evaluate log.error(Event.REPO_FILE_NOT_A_FILE, path=list_file); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:344-344
      End this invocation with 2.
    }
    // Source: vvaharness/orchestrator/entry.py:345-350
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/entry.py:346-346
      End this invocation with run_batch(list_file, args, cfg).
    }
    // Source: vvaharness/orchestrator/entry.py:347-350
    On the first matching source exception StoreError as e, in handler order {
      // Source: vvaharness/orchestrator/entry.py:349-349
      In source order: Evaluate console.mark('fail', source_template_349_33, indent=2, lead=source_literal_349_56); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/entry.py:350-350
      End this invocation with 2.
    }
  }
  // Source: vvaharness/orchestrator/entry.py:352-403
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/entry.py:353-354
    In source order: Evaluate once scan_repo(repo, repo_name, args.application_id, args, cfg, ev_collection_in=ev_collection_in); assign in source target order to outcome.
  }
  // Source: vvaharness/orchestrator/entry.py:355-357
  On the first matching source exception KeyboardInterrupt, in handler order {
    // Source: vvaharness/orchestrator/entry.py:356-356
    In source order: Evaluate console.mark('fail', 'scan aborted by user (Ctrl-C).', indent=2, lead=source_literal_356_78); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:357-357
    End this invocation with 130.
  }
  // Source: vvaharness/orchestrator/entry.py:358-366
  On the first matching source exception AuthenticationError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:360-365
    In source order: Evaluate console.mark('fail', source_template_360_29, indent=2, lead=source_literal_360_52); retain side effects and discard the expression result. Then Evaluate _errlog.log('auth', repo_name, e, error_code=AuthenticationError.error_code, application_id=getattr(args, 'application_id', None)); retain side effects and discard the expression result. Then Evaluate console.write('  (use `vvaharness doctor` to verify credentials; add --resume to continue from the last checkpoint)'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:366-366
    End this invocation with 1.
  }
  // Source: vvaharness/orchestrator/entry.py:367-374
  On the first matching source exception ProxyError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:369-373
    In source order: Evaluate console.mark('fail', source_template_369_29, indent=2, lead=source_literal_369_52); retain side effects and discard the expression result. Then Evaluate _errlog.log('proxy', repo_name, e, error_code=ProxyError.error_code, application_id=getattr(args, 'application_id', None)); retain side effects and discard the expression result. Then Evaluate console.write('  (use `vvaharness doctor` to verify network/TLS settings)'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:374-374
    End this invocation with 1.
  }
  // Source: vvaharness/orchestrator/entry.py:375-378
  On the first matching source exception EVUnreachableError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:377-377
    In source order: Evaluate console.mark('fail', source_template_377_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:378-378
    End this invocation with 2.
  }
  // Source: vvaharness/orchestrator/entry.py:379-382
  On the first matching source exception EVInputError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:381-381
    In source order: Evaluate console.mark('fail', source_template_381_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:382-382
    End this invocation with 2.
  }
  // Source: vvaharness/orchestrator/entry.py:383-386
  On the first matching source exception StoreError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:385-385
    In source order: Evaluate console.mark('fail', source_template_385_29, indent=2, lead=source_literal_385_52); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:386-386
    End this invocation with 2.
  }
  // Source: vvaharness/orchestrator/entry.py:387-393
  On the first matching source exception EmptyScopeError as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:389-392
    In source order: Evaluate console.mark('fail', source_template_389_29, indent=2, lead=source_literal_389_52); retain side effects and discard the expression result. Then Evaluate _errlog.log('s1', repo_name, e, reason='empty_scope', application_id=getattr(args, 'application_id', None)); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:393-393
    End this invocation with 2.
  }
  // Source: vvaharness/orchestrator/entry.py:394-403
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/orchestrator/entry.py:396-397
    In source order: Evaluate console.mark('fail', source_template_396_29, indent=2); retain side effects and discard the expression result. Then Evaluate _errlog.log('scan', repo_name, e, application_id=args.application_id); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/entry.py:398-402
    if (the source predicate os.environ.get('VVAHARNESS_DEBUG') is truthy) {
      // Source: vvaharness/orchestrator/entry.py:399-399
      In source order: Evaluate traceback.print_exc(file=sys.stderr); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/entry.py:401-402
      In source order: Evaluate console.write('  (set VVAHARNESS_DEBUG=1 for the full traceback; details in the *_errors.jsonl under security-scan/)'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/entry.py:403-403
    End this invocation with 1.
  }
  // Source: vvaharness/orchestrator/entry.py:405-405
  End this invocation with outcome.exit_code.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 15: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 15: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 24: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 24: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.models import AuthenticationError, ProxyError` at source line 25: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve as resolve_model` at source line 26: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.exploit_verification.errors import EVInputError, EVUnreachableError` at source line 27: `source_detail/vvaharness/exploit_verification/errors.py.sudo.md`.
- `from vvaharness.exploit_verification.options import collection_path as ev_collection_path` at source line 28: `source_detail/vvaharness/exploit_verification/options.py.sudo.md`.
- `from vvaharness.exploit_verification.options import load_options as ev_load_options` at source line 31: `source_detail/vvaharness/exploit_verification/options.py.sudo.md`.
- `from vvaharness.exploit_verification.options import may_run as ev_may_run` at source line 32: `source_detail/vvaharness/exploit_verification/options.py.sudo.md`.
- `from vvaharness.exploit_verification.options import resolution_error as ev_resolution_error` at source line 33: `source_detail/vvaharness/exploit_verification/options.py.sudo.md`.
- `from vvaharness.orchestrator.batch import run_batch` at source line 36: `source_detail/vvaharness/orchestrator/batch.py.sudo.md`.
- `from vvaharness.orchestrator.cmdb import _cmdb_path, _set_cmdb_path` at source line 37: `source_detail/vvaharness/orchestrator/cmdb.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import EV_MODEL_ROLES, _default_config, _iter_model_roles, trusted_config` at source line 38: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import check_backends, configure_backends` at source line 44: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.
- `from vvaharness.orchestrator.scan import scan_repo` at source line 45: `source_detail/vvaharness/orchestrator/scan.py.sudo.md`.
- `from vvaharness.orchestrator.store import StoreError` at source line 46: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 47: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.scope import EmptyScopeError` at source line 48: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 49: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 49: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 50: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 50: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 51: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.pricing import load_pricing_cached` at source line 52: `source_detail/vvaharness/util/pricing.py.sudo.md`.
- `from vvaharness.remediation_agent.select import _coerce_top_value` at source line 65: `source_detail/vvaharness/remediation_agent/select/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification import gate as ev_gate` at source line 91: `source_detail/vvaharness/exploit_verification/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification import gate as ev_gate` at source line 91: `source_detail/vvaharness/exploit_verification/gate.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/orchestrator/entry.py.sudo.md). Exact strings in the evidence asset support this conversion.
