# vvaharness/remediation_agent/interactive/loop.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/interactive/loop.py.evidence.json`. SHA-256: `95432f4f518730813cb81fe6d4fec698c8681cfabcb222a1ce015370b9bfea75`.

```sudo
// Source: vvaharness/remediation_agent/interactive/loop.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.case import Attempt; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/interactive/loop.py:22-26
In source order: Resolve source import from vvaharness.models.derive import state_of; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import CaseState; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.artifacts import artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import save_ckpt; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent import policy as _policy; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/interactive/loop.py:27-41
In source order: Resolve source import from vvaharness.remediation_agent.interactive.keys import DOWN, ENTER, QUIT, UP, _read_key; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.interactive.render import _clear_and_draw, parse_selection, render_rows; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.plugin_runner import apply_plugin, checkpoint_record; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.runner import step_key_of; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/interactive/loop.py:42-46
In source order: Resolve source import from vvaharness.util.status import stage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/remediation_agent/interactive/loop.py:49-78
// Source signature: _remediate_one(target, *, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, verbose=False, policy_ctx=None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remediate_one(target, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, verbose, policy_ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/loop.py:51-53
  In source order: Retain source documentation literal source_literal_51_4; it is not a model call. Then Evaluate once step_key_of(target, cfg); assign in source target order to step. Then Evaluate once redact(target.label); assign in source target order to label.
  // Source: vvaharness/remediation_agent/interactive/loop.py:54-78
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/interactive/loop.py:57-59
    In source order: Evaluate once artifact_dir(rem_dir, target.slug); assign in source target order to out_dir. Then Evaluate once False if verbose else None; assign in source target order to animate.
    // Source: vvaharness/remediation_agent/interactive/loop.py:60-69
    Enter source context managers left-to-right: stage(label, n=target.index, total=None, animate=animate) {
      // Source: vvaharness/remediation_agent/interactive/loop.py:61-69
      In source order: Evaluate once apply_plugin(target, out_dir, cfg=cfg, repo=rem_dir.parent, mode=mode, verbose=verbose, policy_ctx=policy_ctx); assign in source target order to remediation. Then Evaluate once {**checkpoint_record(target, out_dir, remediation), 'finding_id': target.case_id}; assign in source target order to record. Then Evaluate save_ckpt(ckpt_dir, run_id, step, record); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/remediation_agent/interactive/loop.py:72-74
    In source order: Evaluate once state_of([Attempt(ordinal=1, remediation=remediation)]); assign in source target order to state. Then Evaluate once state in (CaseState.REMEDIATED, CaseState.VALIDATED); assign in source target order to target.done. Then Evaluate console.write(source_template_74_22); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/interactive/loop.py:75-75
    End this invocation with True.
  }
  // Source: vvaharness/remediation_agent/interactive/loop.py:76-78
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/remediation_agent/interactive/loop.py:77-77
    In source order: Evaluate log.warning(Event.REMEDIATION_FINDING_FAILED, finding=target.index, detail=redact(str(e))); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/interactive/loop.py:78-78
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/interactive/loop.py:81-108
// Source signature: run_interactive(findings, *, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, out=None, verbose=False) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_interactive(findings, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, out, verbose) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/loop.py:83-87
  In source order: Retain source documentation literal source_literal_83_4; it is not a model call. Then Evaluate once out or sys.stderr; assign in source target order to out. Then Evaluate once 0; assign in source target order to session. Then Evaluate once _policy.build_context(cfg, rem_dir.parent); assign in source target order to policy_ctx.
  // Source: vvaharness/remediation_agent/interactive/loop.py:88-90
  if (the source predicate policy_ctx.enabled is truthy) {
    // Source: vvaharness/remediation_agent/interactive/loop.py:89-90
    In source order: Evaluate console.write('  [Remediation Agent] policy gate ENABLED (deny-list + playbook + diff post-gate)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/interactive/loop.py:91-94
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/interactive/loop.py:92-92
    In source order: Evaluate once sys.stdin.isatty() and out.isatty(); assign in source target order to interactive_tty.
  }
  // Source: vvaharness/remediation_agent/interactive/loop.py:93-94
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/remediation_agent/interactive/loop.py:94-94
    In source order: Evaluate once False; assign in source target order to interactive_tty.
  }
  // Source: vvaharness/remediation_agent/interactive/loop.py:96-103
  if (the source predicate interactive_tty is truthy) {
    // Source: vvaharness/remediation_agent/interactive/loop.py:97-99
    In source order: Evaluate once _loop_tty(findings, report_path=report_path, rem_dir=rem_dir, ckpt_dir=ckpt_dir, run_id=run_id, cfg=cfg, mode=mode, out=out, verbose=verbose, policy_ctx=policy_ctx); assign in source target order to session.
  }
  else {
    // Source: vvaharness/remediation_agent/interactive/loop.py:101-103
    In source order: Evaluate once _loop_prompt(findings, report_path=report_path, rem_dir=rem_dir, ckpt_dir=ckpt_dir, run_id=run_id, cfg=cfg, mode=mode, verbose=verbose, policy_ctx=policy_ctx); assign in source target order to session.
  }
  // Source: vvaharness/remediation_agent/interactive/loop.py:105-107
  In source order: Evaluate once sum((1 for f in findings if f.done)); assign in source target order to total_done. Then Evaluate console.mark('ok', source_template_106_23, indent=2, lead=source_literal_107_75); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/interactive/loop.py:108-108
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/interactive/loop.py:111-138
// Source signature: _loop_tty(findings, *, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, out, verbose=False, policy_ctx=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _loop_tty(findings, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, out, verbose, policy_ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/loop.py:113-114
  In source order: Evaluate once 0; assign in source target order to cursor. Then Evaluate once 0; assign in source target order to session.
  // Source: vvaharness/remediation_agent/interactive/loop.py:115-138
  while (the source predicate True is truthy) {
    // Source: vvaharness/remediation_agent/interactive/loop.py:116-116
    In source order: Evaluate _clear_and_draw(findings, cursor, out); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/interactive/loop.py:117-124
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/interactive/loop.py:118-118
      In source order: Evaluate once _read_key(); assign in source target order to key.
    }
    // Source: vvaharness/remediation_agent/interactive/loop.py:119-124
    On the first matching source exception RuntimeError, in handler order {
      // Source: vvaharness/remediation_agent/interactive/loop.py:121-124
      End this invocation with session + _loop_prompt(findings, report_path=report_path, rem_dir=rem_dir, ckpt_dir=ckpt_dir, run_id=run_id, cfg=cfg, mode=mode, verbose=verbose, policy_ctx=policy_ctx).
    }
    // Source: vvaharness/remediation_agent/interactive/loop.py:125-126
    if (the source predicate key == QUIT is truthy) {
      // Source: vvaharness/remediation_agent/interactive/loop.py:126-126
      End this invocation with session.
    }
    // Source: vvaharness/remediation_agent/interactive/loop.py:127-138
    if (the source predicate key == UP is truthy) {
      // Source: vvaharness/remediation_agent/interactive/loop.py:128-128
      In source order: Evaluate once (cursor - 1) % len(findings); assign in source target order to cursor.
    }
    else {
      // Source: vvaharness/remediation_agent/interactive/loop.py:129-138
      if (the source predicate key == DOWN is truthy) {
        // Source: vvaharness/remediation_agent/interactive/loop.py:130-130
        In source order: Evaluate once (cursor + 1) % len(findings); assign in source target order to cursor.
      }
      else {
        // Source: vvaharness/remediation_agent/interactive/loop.py:131-138
        if (the source predicate key == ENTER is truthy) {
          // Source: vvaharness/remediation_agent/interactive/loop.py:132-133
          In source order: Evaluate out.write('\x1b[2J\x1b[H'); retain side effects and discard the expression result. Then Evaluate out.flush(); retain side effects and discard the expression result.
          // Source: vvaharness/remediation_agent/interactive/loop.py:134-138
          if (the source predicate _remediate_one(findings[cursor], report_path=report_path, rem_dir=rem_dir, ckpt_dir=ckpt_dir, run_id=run_id, cfg=cfg, mode=mode, verbose=verbose, policy_ctx=policy_ctx) is truthy) {
            // Source: vvaharness/remediation_agent/interactive/loop.py:138-138
            In source order: Apply source augmented assignment session += 1 with source evaluation/in-place semantics.
          }
        }
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/interactive/loop.py:141-159
// Source signature: _loop_prompt(findings, *, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, verbose=False, policy_ctx=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _loop_prompt(findings, report_path, rem_dir, ckpt_dir, run_id, cfg, mode, verbose, policy_ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/interactive/loop.py:143-143
  In source order: Evaluate once 0; assign in source target order to session.
  // Source: vvaharness/remediation_agent/interactive/loop.py:144-159
  while (the source predicate True is truthy) {
    // Source: vvaharness/remediation_agent/interactive/loop.py:145-146
    for each row in render_rows(findings) {
      // Source: vvaharness/remediation_agent/interactive/loop.py:146-146
      In source order: Evaluate console.write(row); retain side effects and discard the expression result.
    }
    // Source: vvaharness/remediation_agent/interactive/loop.py:147-150
    Perform the following protected operations {
      // Source: vvaharness/remediation_agent/interactive/loop.py:148-148
      In source order: Evaluate once input('  Select issues (e.g. 1,3-5 | all | pending | q): '); assign in source target order to raw.
    }
    // Source: vvaharness/remediation_agent/interactive/loop.py:149-150
    On the first matching source exception (EOFError, KeyboardInterrupt), in handler order {
      // Source: vvaharness/remediation_agent/interactive/loop.py:150-150
      End this invocation with session.
    }
    // Source: vvaharness/remediation_agent/interactive/loop.py:151-151
    In source order: Evaluate once parse_selection(raw, findings); assign in source target order to picks.
    // Source: vvaharness/remediation_agent/interactive/loop.py:152-153
    if (the source predicate picks is None is truthy) {
      // Source: vvaharness/remediation_agent/interactive/loop.py:153-153
      End this invocation with session.
    }
    // Source: vvaharness/remediation_agent/interactive/loop.py:154-159
    for each i in picks {
      // Source: vvaharness/remediation_agent/interactive/loop.py:155-159
      if (the source predicate _remediate_one(findings[i], report_path=report_path, rem_dir=rem_dir, ckpt_dir=ckpt_dir, run_id=run_id, cfg=cfg, mode=mode, verbose=verbose, policy_ctx=policy_ctx) is truthy) {
        // Source: vvaharness/remediation_agent/interactive/loop.py:159-159
        In source order: Apply source augmented assignment session += 1 with source evaluation/in-place semantics.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.models.case import Attempt` at source line 21: `source_detail/vvaharness/models/case.py.sudo.md`.
- `from vvaharness.models.derive import state_of` at source line 22: `source_detail/vvaharness/models/derive.py.sudo.md`.
- `from vvaharness.models.vocab import CaseState` at source line 23: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import artifact_dir` at source line 24: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import save_ckpt` at source line 25: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.remediation_agent import policy as _policy` at source line 26: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import policy as _policy` at source line 26: `source_detail/vvaharness/remediation_agent/policy/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.interactive.keys import DOWN, ENTER, QUIT, UP, _read_key` at source line 27: `source_detail/vvaharness/remediation_agent/interactive/keys.py.sudo.md`.
- `from vvaharness.remediation_agent.interactive.render import _clear_and_draw, parse_selection, render_rows` at source line 34: `source_detail/vvaharness/remediation_agent/interactive/render.py.sudo.md`.
- `from vvaharness.remediation_agent.plugin_runner import apply_plugin, checkpoint_record` at source line 39: `source_detail/vvaharness/remediation_agent/plugin_runner/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent.runner import step_key_of` at source line 40: `source_detail/vvaharness/remediation_agent/runner.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 41: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util.status import stage` at source line 42: `source_detail/vvaharness/util/status.py.sudo.md`.
- `from vvaharness.util import console` at source line 43: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 43: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 44: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/remediation_agent/interactive/loop.py.sudo.md). Exact strings in the evidence asset support this conversion.
