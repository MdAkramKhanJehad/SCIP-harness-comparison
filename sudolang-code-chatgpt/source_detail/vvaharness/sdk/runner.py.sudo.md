# vvaharness/sdk/runner.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/sdk/runner.py.evidence.json`. SHA-256: `2b64320ead8b9e3af2260380e03bbf394e1c0354f761550260f6a48b1648ad9f`.

```sudo
// Source: vvaharness/sdk/runner.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Evaluate once Path(__file__).resolve().parent.parent / 'config' / 'profiles'; assign in source target order to _PROFILE_DIR.
// Source: vvaharness/sdk/runner.py:24-25
interface ScanOptionsError {
  Describe the source Python type, preserving its base/metaclass expression order: ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/runner.py:25-25
  In source order: Retain source documentation literal source_literal_25_4; it is not a model call.
}
// Source: vvaharness/sdk/runner.py:28-37
// Source signature: profile_path(profile: str | Path) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn profile_path(profile) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/runner.py:29-30
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then Evaluate once Path(profile); assign in source target order to candidate.
  // Source: vvaharness/sdk/runner.py:31-32
  if (the source predicate candidate.suffix or candidate.parent != Path() is truthy) {
    // Source: vvaharness/sdk/runner.py:32-32
    End this invocation with candidate.
  }
  // Source: vvaharness/sdk/runner.py:33-33
  In source order: Evaluate once _PROFILE_DIR / source_template_33_29; assign in source target order to shipped.
  // Source: vvaharness/sdk/runner.py:34-36
  if (the source predicate not shipped.is_file() is truthy) {
    // Source: vvaharness/sdk/runner.py:35-35
    In source order: Evaluate once sorted((p.stem for p in _PROFILE_DIR.glob('*.yaml'))); assign in source target order to available.
    // Source: vvaharness/sdk/runner.py:36-36
    Raise ScanOptionsError(source_template_36_31).
  }
  // Source: vvaharness/sdk/runner.py:37-37
  End this invocation with shipped.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/runner.py:41-63
// Source: vvaharness/sdk/runner.py:40-40
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/sdk/runner.py:41-63
interface ScanOptions {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/runner.py:42-47
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then For repo, declare without assigning a value; source annotation Path | str. Then For profile, assign None; source annotation str | Path | None. Then For stop_after, assign None; source annotation str | None. Then For resume, assign False; source annotation bool.
  // Source: vvaharness/sdk/runner.py:48-50
  In source order: For application_id, assign None; source annotation str | None. Then For repo_name, assign None; source annotation str | None. Then For extra_argv, assign field(default_factory=tuple); source annotation tuple[str, ...].
  // Source: vvaharness/sdk/runner.py:52-63
  // Source signature: argv(self) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn argv(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/runner.py:53-54
    In source order: Retain source documentation literal source_literal_53_8; it is not a model call. Then Evaluate once ['--repo', str(self.repo)]; assign in source target order to argv.
    // Source: vvaharness/sdk/runner.py:55-56
    if (the source predicate self.profile is not None is truthy) {
      // Source: vvaharness/sdk/runner.py:56-56
      In source order: Apply source augmented assignment argv += ['--config', str(profile_path(self.profile))] with source evaluation/in-place semantics.
    }
    // Source: vvaharness/sdk/runner.py:57-61
    for each (flag, value) in (('--stop-after', self.stop_after), ('--application-id', self.application_id), ('--repo-name', self.repo_name)) {
      // Source: vvaharness/sdk/runner.py:60-61
      if (the source predicate value is truthy) {
        // Source: vvaharness/sdk/runner.py:61-61
        In source order: Apply source augmented assignment argv += [flag, value] with source evaluation/in-place semantics.
      }
    }
    // Source: vvaharness/sdk/runner.py:62-62
    In source order: Evaluate once ['--resume'] if self.resume else []; assign in source target order to resume.
    // Source: vvaharness/sdk/runner.py:63-63
    End this invocation with argv + resume + list(self.extra_argv).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/sdk/runner.py:67-76
// Source: vvaharness/sdk/runner.py:66-66
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/sdk/runner.py:67-76
interface ScanResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/sdk/runner.py:68-71
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call. Then For exit_code, declare without assigning a value; source annotation int. Then For argv, declare without assigning a value; source annotation tuple[str, ...].
  // Source: vvaharness/sdk/runner.py:74-76
  // Source: vvaharness/sdk/runner.py:73-73
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/sdk/runner.py:74-76
  // Source signature: ok(self) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn ok(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/sdk/runner.py:75-75
    In source order: Retain source documentation literal source_literal_75_8; it is not a model call.
    // Source: vvaharness/sdk/runner.py:76-76
    End this invocation with self.exit_code == 0.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/sdk/runner.py:79-84
// Source signature: scan(options: ScanOptions) -> ScanResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn scan(options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/runner.py:80-83
  In source order: Retain source documentation literal source_literal_80_4; it is not a model call. Then Resolve source import from vvaharness.orchestrator import entry; preserve alias and import-time effects. Then Evaluate once options.argv(); assign in source target order to argv. Then Evaluate _reject_unknown_flags(argv); retain side effects and discard the expression result.
  // Source: vvaharness/sdk/runner.py:84-84
  End this invocation with ScanResult(exit_code=entry.main(argv), argv=tuple(argv)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/runner.py:87-93
// Source signature: _reject_unknown_flags(argv: list[str]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reject_unknown_flags(argv) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/sdk/runner.py:88-89
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call. Then Resolve source import from vvaharness.orchestrator import entry; preserve alias and import-time effects.
  // Source: vvaharness/sdk/runner.py:90-93
  Perform the following protected operations {
    // Source: vvaharness/sdk/runner.py:91-91
    In source order: Evaluate entry.build_parser().parse_args(argv); retain side effects and discard the expression result.
  }
  // Source: vvaharness/sdk/runner.py:92-93
  On the first matching source exception SystemExit as exc, in handler order {
    // Source: vvaharness/sdk/runner.py:93-93
    Raise ScanOptionsError(source_template_93_31) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/sdk/runner.py:96-96
In source order: Evaluate once ['ScanOptions', 'ScanOptionsError', 'ScanResult', 'profile_path', 'scan']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.orchestrator import entry` at source line 81: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import entry` at source line 81: `source_detail/vvaharness/orchestrator/entry.py.sudo.md`.
- `from vvaharness.orchestrator import entry` at source line 89: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import entry` at source line 89: `source_detail/vvaharness/orchestrator/entry.py.sudo.md`.
