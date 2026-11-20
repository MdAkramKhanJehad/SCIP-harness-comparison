# vvaharness/cli/_app.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/cli/_app.py.evidence.json`. SHA-256: `67ecdc97753d5713febc584746c40c778f09cf608c4904ef9b8216d45e0e0615`.

```sudo
// Source: vvaharness/cli/_app.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from typing import Any; preserve alias and import-time effects. Then Resolve source import import typer; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.constants.artifacts import VALIDATE_COMMANDS; preserve alias and import-time effects.
// Source: vvaharness/cli/_app.py:24-38
In source order: Evaluate once ['COMMANDS', 'Interrupted', 'app', 'run']; assign in source target order to __all__. Then Evaluate once getattr(typer.core, '_click', None) or typer.core.click; assign in source target order to _click. Then For _PASSTHROUGH, assign {'allow_extra_args': True, 'ignore_unknown_options': True, 'help_option_names': []}; source annotation dict[str, Any]. Then Evaluate once typer.Typer(name='vvaharness', help='Agentic SAST pipeline: scan a repository for vulnerabilities.', add_completion=True, rich_markup_mode='rich', context_settings={'help_option_names': ['-h', '--help']}); assign in source target order to app.
// Source: vvaharness/cli/_app.py:41-42
interface Interrupted {
  Describe the source Python type, preserving its base/metaclass expression order: Exception.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/cli/_app.py:42-42
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call.
}
// Source: vvaharness/cli/_app.py:45-53
// Source signature: _delegate(command: str, ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _delegate(command, ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:46-47
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call. Then Resolve source import from vvaharness import cli; preserve alias and import-time effects.
  // Source: vvaharness/cli/_app.py:49-52
  Perform the following protected operations {
    // Source: vvaharness/cli/_app.py:50-50
    In source order: Evaluate once cli._dispatch([command, *ctx.args]); assign in source target order to code.
  }
  // Source: vvaharness/cli/_app.py:51-52
  On the first matching source exception KeyboardInterrupt as exc, in handler order {
    // Source: vvaharness/cli/_app.py:52-52
    Raise Interrupted with explicit source cause exc.
  }
  // Source: vvaharness/cli/_app.py:53-53
  Raise typer.Exit(code).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_app.py:58-59
// Source: vvaharness/cli/_app.py:56-57
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('setup', context_settings=_PASSTHROUGH, help='Guided readiness check: AI agents, keys, deps, gateway, config.').
// Source: vvaharness/cli/_app.py:58-59
// Source signature: setup(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn setup(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:59-59
  In source order: Evaluate _delegate('setup', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:63-64
// Source: vvaharness/cli/_app.py:62-62
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('init', context_settings=_PASSTHROUGH, hidden=True, help='Alias for `setup`.').
// Source: vvaharness/cli/_app.py:63-64
// Source signature: init(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn init(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:64-64
  In source order: Evaluate _delegate('init', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:71-72
// Source: vvaharness/cli/_app.py:67-70
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('doctor', context_settings=_PASSTHROUGH, help=source_literal_68_18).
// Source: vvaharness/cli/_app.py:71-72
// Source signature: doctor(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn doctor(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:72-72
  In source order: Evaluate _delegate('doctor', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:77-78
// Source: vvaharness/cli/_app.py:75-76
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('estimate', context_settings=_PASSTHROUGH, help='Print a rough scope/cost preview for a repo (no API spend).').
// Source: vvaharness/cli/_app.py:77-78
// Source signature: estimate(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn estimate(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:78-78
  In source order: Evaluate _delegate('estimate', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:83-84
// Source: vvaharness/cli/_app.py:81-82
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('gc', context_settings=_PASSTHROUGH, help='Delete old runs: checkpoints and code-graph workspaces (--keep-runs / --max-age-days / --dry-run).').
// Source: vvaharness/cli/_app.py:83-84
// Source signature: gc(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn gc(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:84-84
  In source order: Evaluate _delegate('gc', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:92-93
// Source: vvaharness/cli/_app.py:87-91
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('scan', context_settings=_PASSTHROUGH, help=source_literal_88_18).
// Source: vvaharness/cli/_app.py:92-93
// Source signature: scan(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:93-93
  In source order: Evaluate _delegate('scan', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:98-99
// Source: vvaharness/cli/_app.py:96-97
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('remediate', context_settings=_PASSTHROUGH, help='Walk findings from a prior scan and remediate them (Remediation Agent).').
// Source: vvaharness/cli/_app.py:98-99
// Source signature: remediate(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn remediate(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:99-99
  In source order: Evaluate _delegate('remediate', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:104-105
// Source: vvaharness/cli/_app.py:102-103
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('validate', context_settings=_PASSTHROUGH, help='Run the s11 agentic validation agent on applied remediations.').
// Source: vvaharness/cli/_app.py:104-105
// Source signature: validate(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:105-105
  In source order: Evaluate _delegate('validate', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:110-111
// Source: vvaharness/cli/_app.py:108-109
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('s11', context_settings=_PASSTHROUGH, hidden=True, help='Alias for `validate`.').
// Source: vvaharness/cli/_app.py:110-111
// Source signature: s11(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn s11(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:111-111
  In source order: Evaluate _delegate('s11', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:116-117
// Source: vvaharness/cli/_app.py:114-115
Before creating this callable, evaluate and retain decorators top-to-bottom: app.command('ev-replay', context_settings=_PASSTHROUGH, help='Re-check exploit-verified findings against a REDEPLOYED target.').
// Source: vvaharness/cli/_app.py:116-117
// Source signature: ev_replay(ctx: typer.Context) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn ev_replay(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:117-117
  In source order: Evaluate _delegate('ev-replay', ctx); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
// Source: vvaharness/cli/_app.py:120-123
In source order: For COMMANDS, assign frozenset({'setup', 'init', 'doctor', 'estimate', 'gc', 'scan', 'remediate', 'ev-replay', *VALIDATE_COMMANDS}); source annotation frozenset[str].
// Source: vvaharness/cli/_app.py:126-137
// Source signature: run(args: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_app.py:127-128
  In source order: Retain source documentation literal source_literal_127_4; it is not a model call. Then Evaluate once typer.main.get_command(app); assign in source target order to command.
  // Source: vvaharness/cli/_app.py:129-137
  Perform the following protected operations {
    // Source: vvaharness/cli/_app.py:130-130
    End this invocation with int(command.main(args=args, prog_name='vvaharness', standalone_mode=False) or 0).
  }
  // Source: vvaharness/cli/_app.py:131-132
  On the first matching source exception typer.Exit as exc, in handler order {
    // Source: vvaharness/cli/_app.py:132-132
    End this invocation with int(exc.exit_code).
  }
  // Source: vvaharness/cli/_app.py:133-134
  On the first matching source exception (Interrupted, typer.Abort) as exc, in handler order {
    // Source: vvaharness/cli/_app.py:134-134
    Raise KeyboardInterrupt with explicit source cause exc.
  }
  // Source: vvaharness/cli/_app.py:135-137
  On the first matching source exception _click.exceptions.ClickException as exc, in handler order {
    // Source: vvaharness/cli/_app.py:136-136
    In source order: Evaluate exc.show(); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_app.py:137-137
    End this invocation with int(exc.exit_code).
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.validation.constants.artifacts import VALIDATE_COMMANDS` at source line 22: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
- `from vvaharness import cli` at source line 47: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import cli` at source line 47: `source_detail/vvaharness/cli/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/cli/_app.py.sudo.md). Exact strings in the evidence asset support this conversion.
