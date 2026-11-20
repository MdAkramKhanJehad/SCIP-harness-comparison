# vvaharness/remediation_agent/remediate.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/remediate.py.evidence.json`. SHA-256: `9de05984201d3ae8f908161595cd739d2688e4ff711b68e540b775d4e791d027`.

```sudo
// Source: vvaharness/remediation_agent/remediate.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, prune_stale_steps; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.findings_json import InvalidFindingsJSON; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/remediate.py:23-35
In source order: Resolve source import from vvaharness.remediation_agent.discovery import load_findings, locate_report, prepare_layout; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.options import parse_options; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.runner import model_banner, process_targets, step_key_of; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent.select import resolve_top; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/remediation_agent/remediate.py:38-101
// Source signature: remediate(repo: str | None, args=None, cfg=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn remediate(repo, args, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/remediate.py:39-39
  In source order: Retain source documentation literal source_literal_39_4; it is not a model call.
  // Source: vvaharness/remediation_agent/remediate.py:40-42
  if (the source predicate not repo is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:41-41
    In source order: Evaluate console.write('usage: vvaharness remediate --repo <path>'); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/remediate.py:42-42
    End this invocation with 2.
  }
  // Source: vvaharness/remediation_agent/remediate.py:43-45
  if (the source predicate cfg is None is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:44-44
    In source order: Evaluate console.mark('fail', 'no config loaded — internal error: remediate() requires cfg.', indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/remediate.py:45-45
    End this invocation with 2.
  }
  // Source: vvaharness/remediation_agent/remediate.py:47-51
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/remediate.py:48-48
    In source order: Evaluate once parse_options(args or []); assign in source target order to opts.
  }
  // Source: vvaharness/remediation_agent/remediate.py:49-51
  On the first matching source exception ValueError as e, in handler order {
    // Source: vvaharness/remediation_agent/remediate.py:50-50
    In source order: Evaluate console.mark('fail', source_template_50_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/remediate.py:51-51
    End this invocation with 2.
  }
  // Source: vvaharness/remediation_agent/remediate.py:53-53
  In source order: Evaluate once Path(repo); assign in source target order to repo_path.
  // Source: vvaharness/remediation_agent/remediate.py:54-56
  if (the source predicate not repo_path.exists() is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:55-55
    In source order: Evaluate console.mark('fail', source_template_55_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/remediate.py:56-56
    End this invocation with 1.
  }
  // Source: vvaharness/remediation_agent/remediate.py:58-58
  In source order: Evaluate once locate_report(repo_path); assign in source target order to (report, rc).
  // Source: vvaharness/remediation_agent/remediate.py:59-60
  if (the source predicate report is None is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:60-60
    End this invocation with rc.
  }
  // Source: vvaharness/remediation_agent/remediate.py:63-66
  if (the source predicate opts.interactive and opts.top is None is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:64-64
    In source order: Evaluate once None; assign in source target order to top.
  }
  else {
    // Source: vvaharness/remediation_agent/remediate.py:66-66
    In source order: Evaluate once resolve_top(opts.top, cfg); assign in source target order to top.
  }
  // Source: vvaharness/remediation_agent/remediate.py:67-67
  In source order: Evaluate console.write(source_template_67_18); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/remediate.py:68-73
  Perform the following protected operations {
    // Source: vvaharness/remediation_agent/remediate.py:69-69
    In source order: Evaluate once load_findings(repo_path, report, top); assign in source target order to found.
  }
  // Source: vvaharness/remediation_agent/remediate.py:70-73
  On the first matching source exception InvalidFindingsJSON as e, in handler order {
    // Source: vvaharness/remediation_agent/remediate.py:72-72
    In source order: Evaluate console.mark('fail', source_template_72_29, indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/remediate.py:73-73
    End this invocation with 1.
  }
  // Source: vvaharness/remediation_agent/remediate.py:74-76
  In source order: Evaluate once found.selected; assign in source target order to findings. Then Evaluate once len(findings); assign in source target order to n.
  // Source: vvaharness/remediation_agent/remediate.py:77-79
  if (the source predicate n == 0 is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:78-78
    In source order: Evaluate console.mark('ok', 'identified 0 SAST issue(s) — nothing to remediate.', indent=2); retain side effects and discard the expression result.
    // Source: vvaharness/remediation_agent/remediate.py:79-79
    End this invocation with 0.
  }
  // Source: vvaharness/remediation_agent/remediate.py:81-87
  In source order: Evaluate once prepare_layout(repo_path); assign in source target order to layout. Then Evaluate prune_stale_steps(layout.run_id, REMEDIATE_PREFIX, [step_key_of(t, cfg) for t in found.discovered]); retain side effects and discard the expression result. Then Evaluate console.write(source_template_85_18); retain side effects and discard the expression result. Then Evaluate console.write(source_template_86_18); retain side effects and discard the expression result. Then Evaluate console.write(source_template_87_18); retain side effects and discard the expression result.
  // Source: vvaharness/remediation_agent/remediate.py:88-90
  if (the source predicate opts.verbose is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:89-90
    In source order: Evaluate console.write('  [Remediation Agent] verbose: printing prompt + raw LLM response per finding'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/remediation_agent/remediate.py:92-97
  if (the source predicate opts.interactive is truthy) {
    // Source: vvaharness/remediation_agent/remediate.py:93-93
    In source order: Resolve source import from vvaharness.remediation_agent.interactive import run_interactive; preserve alias and import-time effects.
    // Source: vvaharness/remediation_agent/remediate.py:94-97
    End this invocation with run_interactive(findings, report_path=report, rem_dir=layout.rem_dir, ckpt_dir=layout.ckpt_dir, run_id=layout.run_id, cfg=cfg, mode=opts.mode, verbose=opts.verbose).
  }
  // Source: vvaharness/remediation_agent/remediate.py:100-101
  End this invocation with process_targets(findings, layout=layout, cfg=cfg, repo_path=repo_path, opts=opts, report=report).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.orchestrator.checkpoints import REMEDIATE_PREFIX, prune_stale_steps` at source line 21: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator.findings_json import InvalidFindingsJSON` at source line 22: `source_detail/vvaharness/orchestrator/findings_json.py.sudo.md`.
- `from vvaharness.remediation_agent.discovery import load_findings, locate_report, prepare_layout` at source line 23: `source_detail/vvaharness/remediation_agent/discovery.py.sudo.md`.
- `from vvaharness.remediation_agent.options import parse_options` at source line 28: `source_detail/vvaharness/remediation_agent/options.py.sudo.md`.
- `from vvaharness.remediation_agent.runner import model_banner, process_targets, step_key_of` at source line 29: `source_detail/vvaharness/remediation_agent/runner.py.sudo.md`.
- `from vvaharness.remediation_agent.select import resolve_top` at source line 34: `source_detail/vvaharness/remediation_agent/select/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.remediation_agent.interactive import run_interactive` at source line 93: `source_detail/vvaharness/remediation_agent/interactive/__init__.py.sudo.md`.
