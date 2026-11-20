# vvaharness/cli/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/cli/__init__.py.evidence.json`. SHA-256: `e0f8e9d19aecc3715e9f99892bd893227957c48bb89d707ccd9d8fdc58208e56`.

```sudo
// Source: vvaharness/cli/__init__.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import signal; preserve alias and import-time effects.
// Source: vvaharness/cli/__init__.py:22-35
In source order: Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli import _app; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli._commands import _ICON, _doctor, _estimate, _ev_replay, _gc, _remediate, _validate; preserve alias and import-time effects.
// Source: vvaharness/cli/__init__.py:36-56
In source order: Resolve source import from vvaharness.cli._dotenv import _dotenv_path, _dotenv_path_is_trusted, _dotenv_selection, _load_dotenv; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli._paths import _check_python, _config_path_from, _config_path_from_explicit, _config_trust_boundary, _load_and_configure, _repo_from; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli._setup import _install_agents, _prompt_for_remediation_inputs, _setup; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import VALIDATE_COMMANDS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects.
// Source: vvaharness/cli/__init__.py:57-131
In source order: Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['VALIDATE_COMMANDS', '_app', '_with_command', '_ICON', 'Path', '_check_python', '_config_path_from', '_config_path_from_explicit', '_config_trust_boundary', '_configure_logging', '_doctor', '_dotenv_path', '_dotenv_path_is_trusted', '_dispatch', '_dotenv_selection', '_estimate', '_ev_replay', '_gc', '_install_agents', '_load_and_configure', '_load_dotenv', '_print_help', '_prompt_for_remediation_inputs', '_remediate', '_repo_from', '_setup', '_validate', '_version', 'main', 'os', 'sys']; assign in source target order to __all__. Then For _COMMAND_HELP, assign (('setup', 'Guided readiness check: AI agents, keys, deps, gateway, config'), ('doctor', 'Check credentials + live backend connectivity (read-only)'), ('estimate', 'Print a rough scope/cost preview for a repo (no API spend)'), ('gc', 'Delete old runs: checkpoints and code-graph workspaces (--keep-runs / --max-age-days / --dry-run)'), ('scan', 'Scan a repo (or --repo-file batch) for vulnerabilities'), ('remediate', 'Walk findings from a prior scan and remediate them'), ('validate', 'Run the s11 agentic validation agent on applied remediations'), ('ev-replay', 'Re-check exploit-verified findings against a REDEPLOYED target')); source annotation tuple[tuple[str, str], ...]. Then For _NOTES, assign ('[heading]Stages[/heading]', '  scan: the packaged default skips S10/S11; --remediate enables S10 only and can edit source.', '  scan: in-scan S11 needs step_validate.enabled: true, and --stop-after s9 skips both.', source_literal_111_4, source_literal_113_4, '', '[heading]Config[/heading]', '  ./config.yaml when present, otherwise the packaged default.', '  Customise: cp vvaharness/config/profiles/sdk.yaml config.yaml   (see also full.yaml)', '  sdk/full profiles enable S10/S11; default/taint disable them. A local overlay can override these flags.', '  Standalone remediate and validate remain available when the scan flags are false.', '', '[heading]Quick start[/heading]', '  vvaharness setup', '  vvaharness estimate --repo /path/to/target', '  vvaharness scan --repo /path/to/target --application-id 12345', '  vvaharness scan --repo /path/to/target --stop-after s9   [dim]# skip S10/S11 on any profile[/dim]', '', "[dim]Run `vvaharness <command> --help` for a command's own options.[/dim]"); source annotation tuple[str, ...].
// Source: vvaharness/cli/__init__.py:134-153
// Source signature: _print_help() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _print_help() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/__init__.py:135-142
  In source order: Retain source documentation literal source_literal_135_4; it is not a model call. Then Resolve source import from rich.console import Console; preserve alias and import-time effects. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.console import THEME, banner, status_table; preserve alias and import-time effects. Then Evaluate once Console(file=sys.stdout, soft_wrap=True, highlight=False, emoji=False, theme=THEME, no_color=bool(os.environ.get('NO_COLOR'))); assign in source target order to out.
  // Source: vvaharness/cli/__init__.py:143-144
  if (the source predicate not banner(err=False) is truthy) {
    // Source: vvaharness/cli/__init__.py:144-144
    In source order: Evaluate out.print(source_template_144_18); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/__init__.py:145-146
  In source order: Evaluate out.print(source_literal_145_14, markup=False); retain side effects and discard the expression result. Then Evaluate once status_table(title='Commands:', columns=('', 'command', 'what it does')); assign in source target order to table.
  // Source: vvaharness/cli/__init__.py:147-148
  for each (name, blurb) in _COMMAND_HELP {
    // Source: vvaharness/cli/__init__.py:148-148
    In source order: Evaluate table.add_row('', source_template_148_26, blurb); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/__init__.py:149-151
  In source order: Evaluate table.add_row('', '[model]--version[/model]', 'Print the installed version'); retain side effects and discard the expression result. Then Evaluate out.print(table); retain side effects and discard the expression result. Then Evaluate out.print(''); retain side effects and discard the expression result.
  // Source: vvaharness/cli/__init__.py:152-153
  for each line in _NOTES {
    // Source: vvaharness/cli/__init__.py:153-153
    In source order: Evaluate out.print(line); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/__init__.py:155-181
// Source signature: _configure_logging(args: list[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _configure_logging(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/__init__.py:156-161
  In source order: Retain source documentation literal source_literal_156_4; it is not a model call. Then Resolve source import from vvaharness.util.logs import configure; preserve alias and import-time effects. Then Evaluate once (None, None, []); assign in source target order to (level, path, rest). Then Evaluate once iter(range(len(args))); assign in source target order to it. Then Evaluate once -1; assign in source target order to skip.
  // Source: vvaharness/cli/__init__.py:162-179
  for each i in it {
    // Source: vvaharness/cli/__init__.py:163-164
    if (the source predicate i <= skip is truthy) {
      // Source: vvaharness/cli/__init__.py:164-164
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/cli/__init__.py:165-165
    In source order: Evaluate once args[i]; assign in source target order to arg.
    // Source: vvaharness/cli/__init__.py:166-175
    for each (flag, setter) in (('--log-level', 'level'), ('--log-file', 'path')) {
      // Source: vvaharness/cli/__init__.py:167-169
      if (the source predicate arg == flag and i + 1 < len(args) is truthy) {
        // Source: vvaharness/cli/__init__.py:168-168
        In source order: Evaluate once (args[i + 1], i + 1); assign in source target order to (value, skip).
        // Source: vvaharness/cli/__init__.py:169-169
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vvaharness/cli/__init__.py:170-172
      if (the source predicate arg.startswith(source_template_170_30) is truthy) {
        // Source: vvaharness/cli/__init__.py:171-171
        In source order: Evaluate once (arg.split('=', 1)[1], setter); assign in source target order to (value, setter).
        // Source: vvaharness/cli/__init__.py:172-172
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    Only on normal iterator exhaustion, with no break from this loop {
      // Source: vvaharness/cli/__init__.py:174-174
      In source order: Evaluate rest.append(arg); retain side effects and discard the expression result.
      // Source: vvaharness/cli/__init__.py:175-175
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/cli/__init__.py:176-179
    if (the source predicate setter == 'level' is truthy) {
      // Source: vvaharness/cli/__init__.py:177-177
      In source order: Evaluate once value; assign in source target order to level.
    }
    else {
      // Source: vvaharness/cli/__init__.py:179-179
      In source order: Evaluate once value; assign in source target order to path.
    }
  }
  // Source: vvaharness/cli/__init__.py:180-180
  In source order: Evaluate configure(level, path); retain side effects and discard the expression result.
  // Source: vvaharness/cli/__init__.py:181-181
  End this invocation with rest.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/__init__.py:183-185
// Source signature: _with_command(args: list[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _with_command(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/__init__.py:184-184
  In source order: Retain source documentation literal source_literal_184_4; it is not a model call.
  // Source: vvaharness/cli/__init__.py:185-185
  End this invocation with args if args[0] in _app.COMMANDS else ['scan', *args].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/__init__.py:188-193
// Source signature: _version() -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _version() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/__init__.py:189-192
  In source order: Retain source documentation literal source_literal_189_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Evaluate print(source_template_192_10); retain side effects and discard the expression result.
  // Source: vvaharness/cli/__init__.py:193-193
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/__init__.py:195-250
// Source signature: _dispatch(args: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dispatch(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/__init__.py:196-197
  In source order: Retain source documentation literal source_literal_196_4; it is not a model call. Then Evaluate once args[0]; assign in source target order to cmd.
  // Source: vvaharness/cli/__init__.py:198-199
  if (the source predicate cmd in ('setup', 'init') is truthy) {
    // Source: vvaharness/cli/__init__.py:199-199
    End this invocation with _setup(args[1:]).
  }
  // Source: vvaharness/cli/__init__.py:200-201
  if (the source predicate cmd == 'doctor' is truthy) {
    // Source: vvaharness/cli/__init__.py:201-201
    End this invocation with _doctor(args[1:]).
  }
  // Source: vvaharness/cli/__init__.py:202-203
  if (the source predicate cmd == 'estimate' is truthy) {
    // Source: vvaharness/cli/__init__.py:203-203
    End this invocation with _estimate(args[1:]).
  }
  // Source: vvaharness/cli/__init__.py:204-205
  if (the source predicate cmd == 'gc' is truthy) {
    // Source: vvaharness/cli/__init__.py:205-205
    End this invocation with _gc(args[1:]).
  }
  // Source: vvaharness/cli/__init__.py:206-207
  if (the source predicate cmd == 'remediate' is truthy) {
    // Source: vvaharness/cli/__init__.py:207-207
    End this invocation with _remediate(args[1:]).
  }
  // Source: vvaharness/cli/__init__.py:208-209
  if (the source predicate cmd == 'ev-replay' is truthy) {
    // Source: vvaharness/cli/__init__.py:209-209
    End this invocation with _ev_replay(args[1:]).
  }
  // Source: vvaharness/cli/__init__.py:210-211
  if (the source predicate cmd in VALIDATE_COMMANDS is truthy) {
    // Source: vvaharness/cli/__init__.py:211-211
    End this invocation with _validate(args[1:]).
  }
  // Source: vvaharness/cli/__init__.py:212-213
  if (the source predicate cmd == 'scan' is truthy) {
    // Source: vvaharness/cli/__init__.py:213-213
    In source order: Evaluate once args[1:]; assign in source target order to args.
  }
  // Source: vvaharness/cli/__init__.py:215-217
  In source order: Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness import manifest, orchestrator; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.entry import build_parser; preserve alias and import-time effects.
  // Source: vvaharness/cli/__init__.py:219-222
  Perform the following protected operations {
    // Source: vvaharness/cli/__init__.py:220-220
    In source order: Evaluate build_parser().parse_args(args); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/__init__.py:221-222
  On the first matching source exception SystemExit as result, in handler order {
    // Source: vvaharness/cli/__init__.py:222-222
    End this invocation with int(result.code or 0).
  }
  // Source: vvaharness/cli/__init__.py:223-223
  In source order: Evaluate once _config_path_from_explicit(args); assign in source target order to (cfg_path, explicit).
  // Source: vvaharness/cli/__init__.py:224-231
  Perform the following protected operations {
    // Source: vvaharness/cli/__init__.py:226-228
    In source order: Evaluate once orchestrator.trusted_config(cfg_path, _config_trust_boundary(args), explicit=explicit, quiet=True); assign in source target order to cfg_path. Then Evaluate config_mod.read_primary(cfg_path); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/__init__.py:229-231
  On the first matching source exception config_mod.ConfigPolicyError as e, in handler order {
    // Source: vvaharness/cli/__init__.py:230-230
    In source order: Evaluate log.error(Event.CONFIG_POLICY_REFUSED, detail=str(e)); retain side effects and discard the expression result.
    // Source: vvaharness/cli/__init__.py:231-231
    End this invocation with 2.
  }
  // Source: vvaharness/cli/__init__.py:233-234
  // Source signature: _raise_terminated(signum, frame)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _raise_terminated(signum, frame) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/cli/__init__.py:234-234
    Raise manifest._Terminated(143).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/cli/__init__.py:238-241
  In source order: Evaluate once threading.current_thread() is threading.main_thread() and signal.getsignal(signal.SIGTERM) is signal.SIG_DFL; assign in source target order to _install_sigterm. Then Evaluate once signal.signal(signal.SIGTERM, _raise_terminated) if _install_sigterm else None; assign in source target order to _old_sigterm.
  // Source: vvaharness/cli/__init__.py:242-250
  Perform the following protected operations {
    // Source: vvaharness/cli/__init__.py:244-246
    Enter source context managers left-to-right: manifest.capture(cfg_path, args) bound to m {
      // Source: vvaharness/cli/__init__.py:245-246
      In source order: Evaluate once orchestrator.main(args); assign in source target order to rc. Then Evaluate once rc; assign in source target order to m['exit_code'].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/cli/__init__.py:247-247
    End this invocation with rc.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/cli/__init__.py:249-250
    if (the source predicate _install_sigterm is truthy) {
      // Source: vvaharness/cli/__init__.py:250-250
      In source order: Evaluate signal.signal(signal.SIGTERM, _old_sigterm); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/__init__.py:253-284
// Source signature: main(argv: list[str] | None=None) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn main(argv) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/__init__.py:254-284
  Perform the following protected operations {
    // Source: vvaharness/cli/__init__.py:255-255
    In source order: Evaluate once _check_python(); assign in source target order to err.
    // Source: vvaharness/cli/__init__.py:256-258
    if (the source predicate err is truthy) {
      // Source: vvaharness/cli/__init__.py:257-257
      In source order: Evaluate log.error(Event.PYTHON_UNSUPPORTED, detail=err); retain side effects and discard the expression result.
      // Source: vvaharness/cli/__init__.py:258-258
      End this invocation with 2.
    }
    // Source: vvaharness/cli/__init__.py:260-260
    In source order: Evaluate once list(sys.argv[1:] if argv is None else argv); assign in source target order to args.
    // Source: vvaharness/cli/__init__.py:261-262
    if (the source predicate args == ['--version'] is truthy) {
      // Source: vvaharness/cli/__init__.py:262-262
      End this invocation with _version().
    }
    // Source: vvaharness/cli/__init__.py:263-265
    In source order: Evaluate _load_dotenv(_repo_from(args)); retain side effects and discard the expression result. Then Evaluate once _configure_logging(args); assign in source target order to args.
    // Source: vvaharness/cli/__init__.py:267-269
    if (the source predicate not args is truthy) {
      // Source: vvaharness/cli/__init__.py:268-268
      In source order: Evaluate _print_help(); retain side effects and discard the expression result.
      // Source: vvaharness/cli/__init__.py:269-269
      End this invocation with 0.
    }
    // Source: vvaharness/cli/__init__.py:270-272
    if (the source predicate args[0] in ('-h', '--help', 'help') is truthy) {
      // Source: vvaharness/cli/__init__.py:271-271
      In source order: Evaluate _print_help(); retain side effects and discard the expression result.
      // Source: vvaharness/cli/__init__.py:272-272
      End this invocation with 0.
    }
    // Source: vvaharness/cli/__init__.py:274-274
    In source order: Resolve source import from vvaharness.orchestrator import store; preserve alias and import-time effects.
    // Source: vvaharness/cli/__init__.py:276-281
    Perform the following protected operations {
      // Source: vvaharness/cli/__init__.py:277-277
      End this invocation with _app.run(_with_command(args)).
    }
    // Source: vvaharness/cli/__init__.py:278-281
    On the first matching source exception store.StoreError as e, in handler order {
      // Source: vvaharness/cli/__init__.py:280-280
      In source order: Evaluate log.error(Event.STORE_UNUSABLE, detail=str(e)); retain side effects and discard the expression result.
      // Source: vvaharness/cli/__init__.py:281-281
      End this invocation with 2.
    }
  }
  // Source: vvaharness/cli/__init__.py:282-284
  On the first matching source exception KeyboardInterrupt, in handler order {
    // Source: vvaharness/cli/__init__.py:283-283
    In source order: Evaluate console.mark('fail', 'command aborted by user (Ctrl-C).', indent=2, lead=source_literal_283_81); retain side effects and discard the expression result.
    // Source: vvaharness/cli/__init__.py:284-284
    End this invocation with 130.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.cli import _app` at source line 26: `source_detail/vvaharness/cli/__init__.py.sudo.md`.
- `from vvaharness.cli import _app` at source line 26: `source_detail/vvaharness/cli/_app.py.sudo.md`.
- `from vvaharness.cli._commands import _ICON, _doctor, _estimate, _ev_replay, _gc, _remediate, _validate` at source line 27: `source_detail/vvaharness/cli/_commands.py.sudo.md`.
- `from vvaharness.cli._dotenv import _dotenv_path, _dotenv_path_is_trusted, _dotenv_selection, _load_dotenv` at source line 36: `source_detail/vvaharness/cli/_dotenv.py.sudo.md`.
- `from vvaharness.cli._paths import _check_python, _config_path_from, _config_path_from_explicit, _config_trust_boundary, _load_and_configure, _repo_from` at source line 42: `source_detail/vvaharness/cli/_paths.py.sudo.md`.
- `from vvaharness.cli._setup import _install_agents, _prompt_for_remediation_inputs, _setup` at source line 50: `source_detail/vvaharness/cli/_setup.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import VALIDATE_COMMANDS` at source line 55: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness.util import console` at source line 56: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 56: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 57: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness import __version__` at source line 138: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.util.console import THEME, banner, status_table` at source line 139: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.logs import configure` at source line 157: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness import __version__` at source line 190: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 215: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 215: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness import manifest, orchestrator` at source line 216: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import manifest, orchestrator` at source line 216: `source_detail/vvaharness/manifest.py.sudo.md`.
- `from vvaharness import manifest, orchestrator` at source line 216: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.entry import build_parser` at source line 217: `source_detail/vvaharness/orchestrator/entry.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 274: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 274: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/cli/__init__.py.sudo.md). Exact strings in the evidence asset support this conversion.
