# vvaharness/validation/session/config_inject.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/session/config_inject.py.evidence.json`. SHA-256: `a0f021e647329533da39c48e48716bd9d2c14c7585f03fb5ed6af0d309bfa9db`.

```sudo
// Source: vvaharness/validation/session/config_inject.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects.
// Source: vvaharness/validation/session/config_inject.py:23-33
In source order: Resolve source import from vvaharness.validation.constants.artifacts import CLAUDE_DIRNAME, LOGGING_DIRNAME, ORCHESTRATOR_LOG_DIRNAME, SUBAGENTS_LOG_DIRNAME; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once Path(__file__).resolve().parent.parent; assign in source target order to _PKG_ROOT. Then Evaluate once _PKG_ROOT / 'claude_config'; assign in source target order to CLAUDE_CONFIG_SOURCE.
// Source: vvaharness/validation/session/config_inject.py:36-44
// Source signature: _inject_hooks(dest_claude: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inject_hooks(dest_claude) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/config_inject.py:37-40
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call. Then Evaluate once dest_claude / 'hooks' / LOGGING_DIRNAME; assign in source target order to hooks_logging. Then Evaluate hooks_logging.mkdir(parents=True); retain side effects and discard the expression result. Then Evaluate once CLAUDE_CONFIG_SOURCE / 'hooks' / LOGGING_DIRNAME / 'capture_transcript.sh'; assign in source target order to src_transcript.
  // Source: vvaharness/validation/session/config_inject.py:41-44
  if (the source predicate src_transcript.exists() is truthy) {
    // Source: vvaharness/validation/session/config_inject.py:42-44
    In source order: Evaluate once hooks_logging / 'capture_transcript.sh'; assign in source target order to dest_transcript. Then Evaluate shutil.copy2(src_transcript, dest_transcript); retain side effects and discard the expression result. Then Evaluate dest_transcript.chmod(493); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/validation/session/config_inject.py:47-73
// Source signature: inject_claude_config(workspace_dir: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn inject_claude_config(workspace_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/validation/session/config_inject.py:48-48
  In source order: Retain source documentation literal source_literal_48_4; it is not a model call.
  // Source: vvaharness/validation/session/config_inject.py:50-73
  Perform the following protected operations {
    // Source: vvaharness/validation/session/config_inject.py:51-51
    In source order: Evaluate once workspace_dir / CLAUDE_DIRNAME; assign in source target order to dest_claude.
    // Source: vvaharness/validation/session/config_inject.py:52-53
    if (the source predicate dest_claude.exists() is truthy) {
      // Source: vvaharness/validation/session/config_inject.py:53-53
      In source order: Evaluate shutil.rmtree(dest_claude); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/session/config_inject.py:54-56
    In source order: Evaluate dest_claude.mkdir(parents=True); retain side effects and discard the expression result. Then Evaluate once CLAUDE_CONFIG_SOURCE / 'rules'; assign in source target order to rules_src.
    // Source: vvaharness/validation/session/config_inject.py:57-58
    if (the source predicate not rules_src.exists() is truthy) {
      // Source: vvaharness/validation/session/config_inject.py:58-58
      Raise FileNotFoundError(source_template_58_36).
    }
    // Source: vvaharness/validation/session/config_inject.py:59-60
    In source order: Evaluate shutil.copytree(rules_src, dest_claude / 'rules'); retain side effects and discard the expression result. Then Evaluate once CLAUDE_CONFIG_SOURCE / 'skills'; assign in source target order to skills_src.
    // Source: vvaharness/validation/session/config_inject.py:61-62
    if (the source predicate skills_src.exists() is truthy) {
      // Source: vvaharness/validation/session/config_inject.py:62-62
      In source order: Evaluate shutil.copytree(skills_src, dest_claude / 'skills'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/validation/session/config_inject.py:63-70
    In source order: Evaluate _inject_hooks(dest_claude); retain side effects and discard the expression result. Then Evaluate shutil.copy2(CLAUDE_CONFIG_SOURCE / 'settings.json', dest_claude / 'settings.json'); retain side effects and discard the expression result. Then Evaluate once workspace_dir / LOGGING_DIRNAME; assign in source target order to log_dir. Then Evaluate (log_dir / ORCHESTRATOR_LOG_DIRNAME).mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate (log_dir / SUBAGENTS_LOG_DIRNAME).mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result.
  }
  // Source: vvaharness/validation/session/config_inject.py:71-73
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/validation/session/config_inject.py:72-72
    In source order: Evaluate log.exception('Failed to inject claude config into %s', workspace_dir); retain side effects and discard the expression result.
    // Source: vvaharness/validation/session/config_inject.py:73-73
    Raise the currently handled exception.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 22: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.validation.constants.artifacts import CLAUDE_DIRNAME, LOGGING_DIRNAME, ORCHESTRATOR_LOG_DIRNAME, SUBAGENTS_LOG_DIRNAME` at source line 23: `source_detail/vvaharness/validation/constants/artifacts.py.sudo.md`.
