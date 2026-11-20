# vvaharness/cli/_setup.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/cli/_setup.py.evidence.json`. SHA-256: `9d4c7a30144bf9491aeab7ed297f581277ba589e245dd72c7a9be38cc568483e`.

```sudo
// Source: vvaharness/cli/_setup.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import stat; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects.
// Source: vvaharness/cli/_setup.py:22-29
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli._commands import _ICON; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli._paths import _config_path_from; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once os.name == 'posix'; assign in source target order to _POSIX.
// Source: vvaharness/cli/_setup.py:32-43
// Source signature: _symlinked_ancestor(path: Path, anchor: Path) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _symlinked_ancestor(path, anchor) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_setup.py:33-34
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then Evaluate once path; assign in source target order to node.
  // Source: vvaharness/cli/_setup.py:35-42
  while (the source predicate node != anchor and node != node.parent is truthy) {
    // Source: vvaharness/cli/_setup.py:36-39
    Perform the following protected operations {
      // Source: vvaharness/cli/_setup.py:37-37
      In source order: Evaluate once node.lstat(); assign in source target order to lst.
    }
    // Source: vvaharness/cli/_setup.py:38-39
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/cli/_setup.py:39-39
      In source order: Evaluate once None; assign in source target order to lst.
    }
    // Source: vvaharness/cli/_setup.py:40-41
    if (the source predicate lst is not None and stat.S_ISLNK(lst.st_mode) is truthy) {
      // Source: vvaharness/cli/_setup.py:41-41
      End this invocation with node.
    }
    // Source: vvaharness/cli/_setup.py:42-42
    In source order: Evaluate once node.parent; assign in source target order to node.
  }
  // Source: vvaharness/cli/_setup.py:43-43
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_setup.py:46-86
// Source signature: _cache_advisory(cfg_path: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_advisory(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_setup.py:47-52
  In source order: Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import shlex; preserve alias and import-time effects. Then Resolve source import from types import SimpleNamespace; preserve alias and import-time effects. Then Resolve source import from urllib.parse import urlsplit; preserve alias and import-time effects. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects.
  // Source: vvaharness/cli/_setup.py:53-54
  In source order: Resolve source import from vvaharness.backends.llm import cache, sdk; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import _iter_model_roles; preserve alias and import-time effects.
  // Source: vvaharness/cli/_setup.py:56-59
  Perform the following protected operations {
    // Source: vvaharness/cli/_setup.py:57-57
    In source order: Evaluate once config_mod.load(cfg_path); assign in source target order to cfg.
  }
  // Source: vvaharness/cli/_setup.py:58-59
  On the first matching source exception (config_mod.ConfigPolicyError, OSError, ValueError), in handler order {
    // Source: vvaharness/cli/_setup.py:59-59
    End this invocation with None.
  }
  // Source: vvaharness/cli/_setup.py:60-62
  if (the source predicate not any((getattr(model, 'via', None) == 'sdk' for _, model in _iter_model_roles(cfg))) is truthy) {
    // Source: vvaharness/cli/_setup.py:62-62
    End this invocation with None.
  }
  // Source: vvaharness/cli/_setup.py:63-63
  In source order: Evaluate once cfg._data; assign in source target order to settings.
  // Source: vvaharness/cli/_setup.py:64-65
  if (the source predicate not cache.markers_enabled(settings) is truthy) {
    // Source: vvaharness/cli/_setup.py:65-65
    End this invocation with None.
  }
  // Source: vvaharness/cli/_setup.py:66-66
  In source order: Evaluate once settings.get('cache_route', 'auto'); assign in source target order to declared.
  // Source: vvaharness/cli/_setup.py:67-68
  if (the source predicate declared is False or str(declared).strip().lower() == 'none' is truthy) {
    // Source: vvaharness/cli/_setup.py:68-68
    End this invocation with None.
  }
  // Source: vvaharness/cli/_setup.py:69-71
  In source order: Evaluate once getattr(cfg, 'sdk', None); assign in source target order to transport. Then Evaluate once getattr(transport, 'base_url', None) or os.environ.get('ANTHROPIC_BASE_URL') or 'https://api.anthropic.com'; assign in source target order to endpoint.
  // Source: vvaharness/cli/_setup.py:72-77
  Perform the following protected operations {
    // Source: vvaharness/cli/_setup.py:73-75
    In source order: Evaluate once sdk._cache_route(SimpleNamespace(base_url=endpoint), config=settings, emit_note=False); assign in source target order to route. Then Evaluate once urlsplit(str(endpoint)).hostname; assign in source target order to host.
  }
  // Source: vvaharness/cli/_setup.py:76-77
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/cli/_setup.py:77-77
    End this invocation with None.
  }
  // Source: vvaharness/cli/_setup.py:78-79
  if (the source predicate route != sdk._ROUTE_UNKNOWN is truthy) {
    // Source: vvaharness/cli/_setup.py:79-79
    End this invocation with None.
  }
  // Source: vvaharness/cli/_setup.py:80-84
  In source order: Evaluate print(source_literal_80_10); retain side effects and discard the expression result. Then Evaluate print(source_template_81_10); retain side effects and discard the expression result. Then Evaluate print('      For an Anthropic-Messages-compatible gateway, set this in'); retain side effects and discard the expression result. Then Evaluate print('      config.local.yaml beside the selected profile (trusted, operator-owned):'); retain side effects and discard the expression result. Then Evaluate print('          cache_route: anthropic'); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_setup.py:85-86
  In source order: Evaluate print('      Verify provider support with a live probe (spends model tokens):'); retain side effects and discard the expression result. Then Evaluate print(source_template_86_10); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_setup.py:89-119
// Source signature: _install_agents() -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _install_agents() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_setup.py:90-94
  In source order: Retain source documentation literal source_literal_90_4; it is not a model call. Then Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import from vvaharness import agentdoc; preserve alias and import-time effects. Then Evaluate once (Path.cwd(), Path.home()); assign in source target order to (cwd, home).
  // Source: vvaharness/cli/_setup.py:96-108
  // Source signature: put(path: Path, content: str, *, anchor: Path) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn put(path, content, anchor) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/cli/_setup.py:97-99
    if (the source predicate path.exists() is truthy) {
      // Source: vvaharness/cli/_setup.py:98-98
      In source order: Evaluate print(source_template_98_18); retain side effects and discard the expression result.
      // Source: vvaharness/cli/_setup.py:99-99
      End this invocation with None.
    }
    // Source: vvaharness/cli/_setup.py:100-105
    if (the source predicate _POSIX is truthy) {
      // Source: vvaharness/cli/_setup.py:101-101
      In source order: Evaluate once _symlinked_ancestor(path, anchor); assign in source target order to symlink.
      // Source: vvaharness/cli/_setup.py:102-105
      if (the source predicate symlink is not None is truthy) {
        // Source: vvaharness/cli/_setup.py:103-104
        In source order: Evaluate console.mark('warn', source_template_103_37, indent=4, err=False); retain side effects and discard the expression result.
        // Source: vvaharness/cli/_setup.py:105-105
        End this invocation with None.
      }
    }
    // Source: vvaharness/cli/_setup.py:106-108
    In source order: Evaluate path.parent.mkdir(parents=True, exist_ok=True); retain side effects and discard the expression result. Then Evaluate path.write_text(content, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate console.mark('ok', source_template_108_27, indent=4, err=False); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/cli/_setup.py:111-112
  In source order: Evaluate put(cwd / 'AGENTS.md', agentdoc.AGENT_DOC, anchor=cwd); retain side effects and discard the expression result. Then Evaluate put(cwd / '.github' / 'copilot-instructions.md', agentdoc.AGENT_DOC, anchor=cwd); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_setup.py:113-116
  if (the source predicate shutil.which('claude') is truthy) {
    // Source: vvaharness/cli/_setup.py:114-116
    In source order: Evaluate put(cwd / 'CLAUDE.md', agentdoc.AGENT_DOC, anchor=cwd); retain side effects and discard the expression result. Then Evaluate put(home / '.claude' / 'skills' / 'vvaharness' / 'SKILL.md', agentdoc.CLAUDE_SKILL, anchor=home); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_setup.py:117-118
  if (the source predicate shutil.which('gemini') is truthy) {
    // Source: vvaharness/cli/_setup.py:118-118
    In source order: Evaluate put(cwd / 'GEMINI.md', agentdoc.gemini_doc(), anchor=cwd); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_setup.py:119-119
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_setup.py:121-215
// Source signature: _setup(rest: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _setup(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_setup.py:122-127
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import environment as env; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.environment import FAIL; preserve alias and import-time effects. Then Evaluate once _config_path_from(rest); assign in source target order to cfg_path.
  // Source: vvaharness/cli/_setup.py:128-132
  In source order: Evaluate once '--write-env' in rest; assign in source target order to write_env. Then Evaluate print(source_template_130_10); retain side effects and discard the expression result. Then Evaluate _prompt_for_remediation_inputs(); retain side effects and discard the expression result. Then Evaluate once env.run_checks(cfg_path); assign in source target order to checks.
  // Source: vvaharness/cli/_setup.py:133-134
  for each c in checks {
    // Source: vvaharness/cli/_setup.py:134-134
    In source order: Evaluate print(source_template_134_14); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_setup.py:136-140
  In source order: Evaluate once env.summarize(checks); assign in source target order to (n_ok, n_warn, n_blocking). Then Evaluate print('  ' + '─' * 60); retain side effects and discard the expression result. Then Evaluate print(source_template_138_10); retain side effects and discard the expression result. Then Evaluate once env.recommend_profile(); assign in source target order to (prof, why).
  // Source: vvaharness/cli/_setup.py:141-145
  if (the source predicate prof is truthy) {
    // Source: vvaharness/cli/_setup.py:142-142
    In source order: Evaluate print(source_template_142_14); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_setup.py:143-145
    if (the source predicate prof != 'default' is truthy) {
      // Source: vvaharness/cli/_setup.py:144-145
      In source order: Evaluate print(source_template_144_18); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/cli/_setup.py:148-151
  In source order: Evaluate once next((c for c in checks if c.name == 'via:sdk endpoint' and c.status == FAIL), None); assign in source target order to gw. Then Evaluate once env.detect_gateway(); assign in source target order to (gw_url, gw_src). Then Evaluate once env.detect_ca_cert(); assign in source target order to ca.
  // Source: vvaharness/cli/_setup.py:152-165
  if (the source predicate gw is truthy) {
    // Source: vvaharness/cli/_setup.py:153-153
    In source order: Evaluate print(source_literal_153_14); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_setup.py:154-158
    if (the source predicate gw_url is truthy) {
      // Source: vvaharness/cli/_setup.py:155-156
      In source order: Evaluate print(source_template_155_18); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/cli/_setup.py:158-158
      In source order: Evaluate print('      export ANTHROPIC_BASE_URL=https://<your-gateway>/'); retain side effects and discard the expression result.
    }
    // Source: vvaharness/cli/_setup.py:159-163
    if (the source predicate ca is truthy) {
      // Source: vvaharness/cli/_setup.py:161-163
      In source order: Evaluate print(source_template_161_18); retain side effects and discard the expression result.
    }
    // Source: vvaharness/cli/_setup.py:164-165
    In source order: Evaluate print('      export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1   # if the gateway rejects beta flags (400)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_setup.py:167-169
  In source order: Evaluate _cache_advisory(cfg_path); retain side effects and discard the expression result. Then Evaluate once Path('.env'); assign in source target order to env_file.
  // Source: vvaharness/cli/_setup.py:170-195
  if (the source predicate not env_file.exists() is truthy) {
    // Source: vvaharness/cli/_setup.py:171-171
    In source order: Evaluate once Path('.env.example'); assign in source target order to example.
    // Source: vvaharness/cli/_setup.py:172-195
    if (the source predicate write_env is truthy) {
      // Source: vvaharness/cli/_setup.py:173-174
      In source order: Evaluate once example.read_text(encoding='utf-8') if example.exists() else ''; assign in source target order to base. Then Evaluate once ''; assign in source target order to extra.
      // Source: vvaharness/cli/_setup.py:175-176
      if (the source predicate gw_url is truthy) {
        // Source: vvaharness/cli/_setup.py:176-176
        In source order: Apply source augmented assignment extra += source_template_176_25 with source evaluation/in-place semantics.
      }
      // Source: vvaharness/cli/_setup.py:177-187
      if (the source predicate ca is truthy) {
        // Source: vvaharness/cli/_setup.py:178-187
        In source order: Apply source augmented assignment extra += source_template_179_20 with source evaluation/in-place semantics.
      }
      // Source: vvaharness/cli/_setup.py:188-190
      if (the source predicate gw_url or ca is truthy) {
        // Source: vvaharness/cli/_setup.py:189-190
        In source order: Apply source augmented assignment extra += source_literal_189_25 with source evaluation/in-place semantics.
      }
      // Source: vvaharness/cli/_setup.py:191-195
      In source order: Evaluate env_file.write_text(base + extra, encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate console.mark('ok', 'wrote .env' + (' (incl. detected gateway)' if gw_url else '') + ' — fill in any remaining keys, then `set -a && source .env && set +a`', indent=2, lead=source_literal_195_70, err=False); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/cli/_setup.py:197-204
  if (the source predicate '--install-agents' in rest is truthy) {
    // Source: vvaharness/cli/_setup.py:198-199
    In source order: Evaluate print(source_literal_198_14); retain side effects and discard the expression result. Then Evaluate _install_agents(); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/cli/_setup.py:201-204
    In source order: Evaluate print(source_literal_201_14); retain side effects and discard the expression result. Then Evaluate print('  (Operating manual: AGENTS.md · capabilities: docs/SKILLS.md)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_setup.py:205-208
  if (the source predicate n_blocking is truthy) {
    // Source: vvaharness/cli/_setup.py:206-207
    In source order: Evaluate print(source_template_206_14); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_setup.py:208-208
    End this invocation with 1.
  }
  // Source: vvaharness/cli/_setup.py:209-214
  In source order: Evaluate print(source_literal_209_10); retain side effects and discard the expression result. Then Evaluate print('  The packaged default profile skips S10 remediation and S11 validation.'); retain side effects and discard the expression result. Then Evaluate console.mark('warn', '--remediate enables S10 only and can edit target source; in-scan S11 needs step_validate.enabled: true.', indent=2, err=False); retain side effects and discard the expression result. Then Evaluate print(source_literal_213_10); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_setup.py:215-215
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_setup.py:217-241
// Source signature: _prompt_for_remediation_inputs() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _prompt_for_remediation_inputs() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_setup.py:218-221
  In source order: Retain source documentation literal source_literal_218_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent import rule_paths; preserve alias and import-time effects. Then Evaluate once rule_paths.missing_rules(rule_paths.__file__); assign in source target order to missing.
  // Source: vvaharness/cli/_setup.py:222-223
  if (the source predicate not missing or not sys.stdin.isatty() is truthy) {
    // Source: vvaharness/cli/_setup.py:223-223
    End this invocation with None.
  }
  // Source: vvaharness/cli/_setup.py:224-224
  In source order: Evaluate print('  ! remediation defaults are missing: ' + ', '.join(missing)); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_setup.py:225-241
  while (the source predicate True is truthy) {
    // Source: vvaharness/cli/_setup.py:226-232
    Perform the following protected operations {
      // Source: vvaharness/cli/_setup.py:227-229
      In source order: Evaluate once input('  Path to the VVAH inputs directory (blank to skip): ').strip(); assign in source target order to answer.
    }
    // Source: vvaharness/cli/_setup.py:230-232
    On the first matching source exception (EOFError, KeyboardInterrupt), in handler order {
      // Source: vvaharness/cli/_setup.py:231-231
      In source order: Evaluate print(); retain side effects and discard the expression result.
      // Source: vvaharness/cli/_setup.py:232-232
      End this invocation with None.
    }
    // Source: vvaharness/cli/_setup.py:233-234
    if (the source predicate not answer is truthy) {
      // Source: vvaharness/cli/_setup.py:234-234
      End this invocation with None.
    }
    // Source: vvaharness/cli/_setup.py:235-235
    In source order: Evaluate once rule_paths.validate_inputs_dir(answer); assign in source target order to (directory, absent).
    // Source: vvaharness/cli/_setup.py:236-238
    if (the source predicate absent is truthy) {
      // Source: vvaharness/cli/_setup.py:237-237
      In source order: Evaluate print(source_template_237_18); retain side effects and discard the expression result.
      // Source: vvaharness/cli/_setup.py:238-238
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/cli/_setup.py:239-240
    In source order: Evaluate once rule_paths.save_inputs_dir(directory); assign in source target order to target. Then Evaluate console.mark('ok', source_template_240_27, indent=2, err=False); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_setup.py:241-241
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.cli._commands import _ICON` at source line 24: `source_detail/vvaharness/cli/_commands.py.sudo.md`.
- `from vvaharness.cli._paths import _config_path_from` at source line 25: `source_detail/vvaharness/cli/_paths.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 26: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 52: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 52: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cache, sdk` at source line 53: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cache, sdk` at source line 53: `source_detail/vvaharness/backends/llm/cache.py.sudo.md`.
- `from vvaharness.backends.llm import cache, sdk` at source line 53: `source_detail/vvaharness/backends/llm/sdk.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _iter_model_roles` at source line 54: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness import agentdoc` at source line 93: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import agentdoc` at source line 93: `source_detail/vvaharness/agentdoc.py.sudo.md`.
- `from vvaharness import __version__` at source line 123: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.util import environment as env` at source line 124: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import environment as env` at source line 124: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.util.environment import FAIL` at source line 125: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.remediation_agent import rule_paths` at source line 219: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import rule_paths` at source line 219: `source_detail/vvaharness/remediation_agent/rule_paths.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/cli/_setup.py.sudo.md). Exact strings in the evidence asset support this conversion.
