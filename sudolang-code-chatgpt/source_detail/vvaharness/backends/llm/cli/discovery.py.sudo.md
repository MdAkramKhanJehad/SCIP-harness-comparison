# vvaharness/backends/llm/cli/discovery.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/backends/llm/cli/discovery.py.evidence.json`. SHA-256: `1f87dd9f70b8dc6d36b9c62ec5c2ddfe1016d003a0db8b648126b408df4a59f7`.

```sudo
// Source: vvaharness/backends/llm/cli/discovery.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/discovery.py:21-26
In source order: Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects.
// Source: vvaharness/backends/llm/cli/discovery.py:27-31
In source order: Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/backends/llm/cli/discovery.py:36-49
// Source signature: _which_abs(*names: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _which_abs(names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:37-44
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/discovery.py:45-48
  for each name in names {
    // Source: vvaharness/backends/llm/cli/discovery.py:46-46
    In source order: Evaluate once shutil.which(name); assign in source target order to hit.
    // Source: vvaharness/backends/llm/cli/discovery.py:47-48
    if (the source predicate hit and Path(hit).is_absolute() is truthy) {
      // Source: vvaharness/backends/llm/cli/discovery.py:48-48
      End this invocation with hit.
    }
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:49-49
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:52-86
// Source signature: _find_claude_cmd() -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _find_claude_cmd() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:53-54
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once os.environ.get('VVAHARNESS_CLAUDE_BINARY'); assign in source target order to override.
  // Source: vvaharness/backends/llm/cli/discovery.py:55-59
  if (the source predicate override is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:56-58
    if (the source predicate Path(override).is_file() is truthy) {
      // Source: vvaharness/backends/llm/cli/discovery.py:57-57
      In source order: Evaluate console.write(source_template_57_26); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/discovery.py:58-58
      End this invocation with [override].
    }
    // Source: vvaharness/backends/llm/cli/discovery.py:59-59
    In source order: Evaluate log.warning(Event.CLI_BINARY_OVERRIDE_MISSING, path=override); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:60-80
  if (the source predicate os.name == 'nt' is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:64-65
    In source order: Evaluate os.environ.setdefault('NoDefaultCurrentDirectoryInExePath', '1'); retain side effects and discard the expression result. Then Evaluate once _which_abs('claude', 'claude.cmd', 'claude.CMD'); assign in source target order to cmd_path.
    // Source: vvaharness/backends/llm/cli/discovery.py:66-78
    if (the source predicate cmd_path is truthy) {
      // Source: vvaharness/backends/llm/cli/discovery.py:67-69
      In source order: Evaluate once Path(cmd_path).parent / 'node_modules' / '@anthropic-ai' / 'claude-code'; assign in source target order to pkg. Then Evaluate once pkg / 'bin' / 'claude.exe'; assign in source target order to native.
      // Source: vvaharness/backends/llm/cli/discovery.py:70-71
      if (the source predicate native.exists() is truthy) {
        // Source: vvaharness/backends/llm/cli/discovery.py:71-71
        End this invocation with [str(native)].
      }
      // Source: vvaharness/backends/llm/cli/discovery.py:73-73
      In source order: Evaluate once pkg / 'cli.js'; assign in source target order to cli_js.
      // Source: vvaharness/backends/llm/cli/discovery.py:74-76
      if (the source predicate cli_js.exists() is truthy) {
        // Source: vvaharness/backends/llm/cli/discovery.py:75-75
        In source order: Evaluate once _which_abs('node') or 'node'; assign in source target order to node.
        // Source: vvaharness/backends/llm/cli/discovery.py:76-76
        End this invocation with [node, str(cli_js)].
      }
      // Source: vvaharness/backends/llm/cli/discovery.py:78-78
      End this invocation with [cmd_path].
    }
    // Source: vvaharness/backends/llm/cli/discovery.py:79-79
    In source order: Evaluate log.warning("'claude' not found on PATH; using bare name"); retain side effects and discard the expression result.
    // Source: vvaharness/backends/llm/cli/discovery.py:80-80
    End this invocation with ['claude'].
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:82-82
  In source order: Evaluate once shutil.which('claude'); assign in source target order to resolved.
  // Source: vvaharness/backends/llm/cli/discovery.py:83-84
  if (the source predicate resolved is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:84-84
    End this invocation with [resolved].
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:85-85
  In source order: Evaluate log.warning("'claude' not found on PATH; using bare name"); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/discovery.py:86-86
  End this invocation with ['claude'].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:90-97
In source order: Evaluate once _find_claude_cmd(); assign in source target order to _CLAUDE_CMD. Then Evaluate once ('dontAsk', 'manual', 'default', 'acceptEdits'); assign in source target order to _PERMISSION_FALLBACKS. Then For _caps_cache, assign None; source annotation dict | None. Then Evaluate once ('--vvah-capability-probe-aaa', '--vvah-capability-probe-bbb'); assign in source target order to _PROBE_SENTINELS.
// Source: vvaharness/backends/llm/cli/discovery.py:100-107
// Source signature: _cli_output(*args: str, timeout: int=20) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cli_output(timeout, args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:101-101
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/discovery.py:102-106
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/discovery.py:103-104
    In source order: Evaluate once subprocess.run([*_CLAUDE_CMD, *args], capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL); assign in source target order to r.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:105-106
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/llm/cli/discovery.py:106-106
    End this invocation with ''.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:107-107
  End this invocation with (r.stdout or '') + (r.stderr or '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:110-117
// Source signature: _resume_capable() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resume_capable() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:111-114
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call. Then Evaluate once re.search('(\\d+)\\.(\\d+)\\.(\\d+)', _cli_output('--version')); assign in source target order to m.
  // Source: vvaharness/backends/llm/cli/discovery.py:115-116
  if (the source predicate not m is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:116-116
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:117-117
  End this invocation with tuple((int(g) for g in m.groups())) >= (2, 1, 286).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:120-122
// Source signature: _parse_probe(flag: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_probe(flag) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:121-121
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/discovery.py:122-122
  End this invocation with _cli_output(flag, *_PROBE_SENTINELS, '-p', 'x', '--output-format', 'json', timeout=30).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:125-133
// Source signature: _flag_accepted(flag: str, help_text: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _flag_accepted(flag, help_text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:126-126
  In source order: Retain source documentation literal source_literal_126_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/discovery.py:127-128
  if (the source predicate flag in help_text is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:128-128
    End this invocation with True.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:129-130
  if (the source predicate not help_text is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:130-130
    End this invocation with False.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:131-131
  In source order: Evaluate once _parse_probe(flag); assign in source target order to out.
  // Source: vvaharness/backends/llm/cli/discovery.py:132-133
  End this invocation with source_template_132_12 not in out and any((sentinel in out for sentinel in _PROBE_SENTINELS)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:136-170
// Source signature: _cli_capabilities() -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cli_capabilities() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:137-138
  In source order: Retain source documentation literal source_literal_137_4; it is not a model call. Then Bind names in module scope: _caps_cache.
  // Source: vvaharness/backends/llm/cli/discovery.py:139-140
  if (the source predicate _caps_cache is not None is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:140-140
    End this invocation with _caps_cache.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:141-145
  In source order: Evaluate once _cli_output('--help'); assign in source target order to help_text. Then For modes, assign set(); source annotation set[str]. Then Evaluate once re.search('--permission-mode\\b.*?\\(choices:\\s*([^)]*)\\)', help_text, re.DOTALL); assign in source target order to m.
  // Source: vvaharness/backends/llm/cli/discovery.py:146-147
  if (the source predicate m is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:147-147
    In source order: Evaluate once set(re.findall('"([^"]+)"', m.group(1))); assign in source target order to modes.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:148-168
  In source order: Evaluate once bool(help_text); assign in source target order to probed. Then Evaluate once {'effort': _flag_accepted('--effort', help_text), 'max_turns': _flag_accepted('--max-turns', help_text), 'max_budget': _flag_accepted('--max-budget-usd', help_text), 'tools': _flag_accepted('--tools', help_text), 'disallowed_tools': _flag_accepted('--disallowedTools', help_text), 'permission_prompts': _flag_accepted('--permission-prompts', help_text), 'strict_mcp_config': _flag_accepted('--strict-mcp-config', help_text), 'setting_sources': _flag_accepted('--setting-sources', help_text), 'disable_slash_commands': _flag_accepted('--disable-slash-commands', help_text), 'restricted': _flag_accepted('--restricted', help_text), 'json_schema': not probed or _flag_accepted('--json-schema', help_text), 'permission_modes': modes, 'probed': probed, 'resume': _resume_capable()}; assign in source target order to _caps_cache.
  // Source: vvaharness/backends/llm/cli/discovery.py:170-170
  End this invocation with _caps_cache.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:173-195
// Source signature: _safe_permission_mode(requested: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _safe_permission_mode(requested) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:174-176
  In source order: Retain source documentation literal source_literal_174_4; it is not a model call. Then Evaluate once _cli_capabilities(); assign in source target order to caps. Then Evaluate once caps['permission_modes']; assign in source target order to modes.
  // Source: vvaharness/backends/llm/cli/discovery.py:177-178
  if (the source predicate not modes is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:178-178
    End this invocation with requested.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:179-180
  if (the source predicate requested in modes is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:180-180
    End this invocation with requested.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:181-184
  for each m in _PERMISSION_FALLBACKS {
    // Source: vvaharness/backends/llm/cli/discovery.py:182-184
    if (the source predicate m in modes is truthy) {
      // Source: vvaharness/backends/llm/cli/discovery.py:183-183
      In source order: Evaluate log.warning(Event.CLI_PERMISSION_MODE_UNAVAILABLE, requested=requested, using=m); retain side effects and discard the expression result.
      // Source: vvaharness/backends/llm/cli/discovery.py:184-184
      End this invocation with m.
    }
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:186-187
  In source order: Evaluate once next((m for m in sorted(modes) if m != 'bypassPermissions'), None); assign in source target order to fallback.
  // Source: vvaharness/backends/llm/cli/discovery.py:188-192
  if (the source predicate fallback is None is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:189-192
    Raise RuntimeError(source_template_190_12).
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:193-194
  In source order: Evaluate log.warning(Event.CLI_NO_PERMISSION_MODE, offered=sorted(_PERMISSION_FALLBACKS), fallback=fallback); retain side effects and discard the expression result.
  // Source: vvaharness/backends/llm/cli/discovery.py:195-195
  End this invocation with fallback.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:198-204
// Source signature: _tail(text: str | None, n: int=1200) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _tail(text, n) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:199-200
  if (the source predicate not text is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:200-200
    End this invocation with ''.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:201-201
  In source order: Evaluate once text.strip(); assign in source target order to text.
  // Source: vvaharness/backends/llm/cli/discovery.py:202-203
  if (the source predicate len(text) <= n is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:203-203
    End this invocation with text.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:204-204
  End this invocation with source_literal_204_11 + text[-n:].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:207-216
// Source signature: _short_cmd(cmd: list[str]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _short_cmd(cmd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:208-209
  In source order: Retain source documentation literal source_literal_208_4; it is not a model call. Then Evaluate once []; assign in source target order to out.
  // Source: vvaharness/backends/llm/cli/discovery.py:210-215
  for each a in cmd {
    // Source: vvaharness/backends/llm/cli/discovery.py:211-215
    if (the source predicate len(a) > 80 is truthy) {
      // Source: vvaharness/backends/llm/cli/discovery.py:212-213
      In source order: Evaluate once a[:60].replace(source_literal_212_34, ' '); assign in source target order to head. Then Evaluate out.append(source_template_213_23); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/backends/llm/cli/discovery.py:215-215
      In source order: Evaluate out.append(a); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:216-216
  End this invocation with ' '.join(out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:219-248
// Source signature: _extract_envelope_error(stdout: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _extract_envelope_error(stdout) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:220-220
  In source order: Retain source documentation literal source_literal_220_4; it is not a model call.
  // Source: vvaharness/backends/llm/cli/discovery.py:221-222
  if (the source predicate not stdout is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:222-222
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:223-225
  In source order: Evaluate once stdout.strip(); assign in source target order to s. Then Evaluate once [p for p in (s.find('{'), s.find('[')) if p >= 0]; assign in source target order to candidates.
  // Source: vvaharness/backends/llm/cli/discovery.py:226-227
  if (the source predicate not candidates is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:227-227
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:228-231
  Perform the following protected operations {
    // Source: vvaharness/backends/llm/cli/discovery.py:229-229
    In source order: Evaluate once json.loads(s[min(candidates):]); assign in source target order to env.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:230-231
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/backends/llm/cli/discovery.py:231-231
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:233-241
  if (the source predicate isinstance(env, list) is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:235-241
    In source order: Evaluate once next((e for e in reversed(env) if isinstance(e, dict) and (e.get('type') == 'result' or e.get('is_error') or e.get('subtype') in ('error', 'error_during_execution'))), None); assign in source target order to evt. Then Evaluate once evt; assign in source target order to env.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:242-243
  if (the source predicate not isinstance(env, dict) is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:243-243
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:244-245
  if (the source predicate not (env.get('is_error') or env.get('subtype') in ('error', 'error_during_execution')) is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:245-245
    End this invocation with None.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:246-247
  In source order: Evaluate once env.get('api_error_status'); assign in source target order to status. Then Evaluate once env.get('result') or env.get('error') or env.get('message') or 'unknown error'; assign in source target order to msg.
  // Source: vvaharness/backends/llm/cli/discovery.py:248-248
  End this invocation with source_template_248_11 if status else str(msg).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/backends/llm/cli/discovery.py:251-269
// Source signature: _format_cli_error(prefix: str, cmd: list[str], result: subprocess.CompletedProcess) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _format_cli_error(prefix, cmd, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/backends/llm/cli/discovery.py:252-252
  In source order: Evaluate once _extract_envelope_error(result.stdout); assign in source target order to env_err.
  // Source: vvaharness/backends/llm/cli/discovery.py:253-254
  if (the source predicate env_err is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:254-254
    End this invocation with source_template_254_15.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:257-262
  In source order: Evaluate once _tail(redact(result.stderr)); assign in source target order to err_tail. Then Evaluate once _tail(redact(result.stdout)); assign in source target order to out_tail. Then Evaluate once [source_template_260_8, source_template_261_8]; assign in source target order to parts.
  // Source: vvaharness/backends/llm/cli/discovery.py:263-264
  if (the source predicate err_tail is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:264-264
    In source order: Evaluate parts.append(source_template_264_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:265-266
  if (the source predicate out_tail is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:266-266
    In source order: Evaluate parts.append(source_template_266_21); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:267-268
  if (the source predicate not err_tail and (not out_tail) is truthy) {
    // Source: vvaharness/backends/llm/cli/discovery.py:268-268
    In source order: Evaluate parts.append('no stdout/stderr captured'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/backends/llm/cli/discovery.py:269-269
  End this invocation with source_literal_269_11.join(parts).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.report.redact import redact` at source line 25: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 26: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 26: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 27: `source_detail/vvaharness/util/events.py.sudo.md`.
