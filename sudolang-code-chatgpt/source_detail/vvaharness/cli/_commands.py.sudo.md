# vvaharness/cli/_commands.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/cli/_commands.py.evidence.json`. SHA-256: `d0794c397d79b4d37e921e5cf6ba1aa914c7ff4c18e52fb50e1c507a3585b4db`.

```sudo
// Source: vvaharness/cli/_commands.py:16-27
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli._paths import _config_path_from, _config_path_from_explicit, _load_and_configure, _repo_from; preserve alias and import-time effects.
// Source: vvaharness/cli/_commands.py:28-33
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once {'ok': '✓', 'warn': '⚠', 'fail': '✗'}; assign in source target order to _ICON.
// Source: vvaharness/cli/_commands.py:36-87
// Source signature: _doctor(rest: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _doctor(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_commands.py:37-37
  In source order: Retain source documentation literal source_literal_37_4; it is not a model call.
  // Source: vvaharness/cli/_commands.py:38-51
  if (the source predicate '--help' in rest or '-h' in rest is truthy) {
    // Source: vvaharness/cli/_commands.py:40-50
    In source order: Evaluate print(source_literal_41_12); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:51-51
    End this invocation with 0.
  }
  // Source: vvaharness/cli/_commands.py:53-55
  In source order: Resolve source import from vvaharness.orchestrator import probe_backends; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import environment as env; preserve alias and import-time effects. Then Evaluate once _config_path_from(rest); assign in source target order to cfg_path.
  // Source: vvaharness/cli/_commands.py:56-58
  if (the source predicate not Path(cfg_path).exists() is truthy) {
    // Source: vvaharness/cli/_commands.py:57-57
    In source order: Evaluate console.write(source_template_57_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:58-58
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:59-59
  In source order: Evaluate once _load_and_configure(cfg_path, 'doctor'); assign in source target order to cfg.
  // Source: vvaharness/cli/_commands.py:60-61
  if (the source predicate cfg is None is truthy) {
    // Source: vvaharness/cli/_commands.py:61-61
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:63-63
  In source order: Evaluate once env.run_checks(cfg_path); assign in source target order to checks.
  // Source: vvaharness/cli/_commands.py:64-65
  for each c in checks {
    // Source: vvaharness/cli/_commands.py:65-65
    In source order: Evaluate print(source_template_65_14); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_commands.py:66-68
  In source order: Evaluate once env.summarize(checks); assign in source target order to (n_ok, n_warn, n_blocking). Then Evaluate print('  ' + '─' * 60); retain side effects and discard the expression result. Then Evaluate print(source_template_68_10); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_commands.py:70-72
  if (the source predicate n_blocking is truthy) {
    // Source: vvaharness/cli/_commands.py:71-71
    In source order: Evaluate print('  [probe] skipped — fix the blocking item(s) above first'); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:72-72
    End this invocation with 1.
  }
  // Source: vvaharness/cli/_commands.py:73-75
  In source order: Evaluate once 0 if probe_backends(cfg) else 1; assign in source target order to rc. Then Evaluate once next((c for c in checks if c.name == 'TLS / CA cert'), None); assign in source target order to tls.
  // Source: vvaharness/cli/_commands.py:76-79
  if (the source predicate rc == 0 and tls is not None and (tls.status != env.OK) is truthy) {
    // Source: vvaharness/cli/_commands.py:77-79
    In source order: Evaluate print(source_literal_77_14); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_commands.py:80-86
  if (the source predicate '--cache-probe' in rest is truthy) {
    // Source: vvaharness/cli/_commands.py:81-84
    if (the source predicate rc != 0 is truthy) {
      // Source: vvaharness/cli/_commands.py:82-83
      In source order: Evaluate console.write('  [cache-probe] skipped — fix the backend probe failure(s) above first'); retain side effects and discard the expression result.
      // Source: vvaharness/cli/_commands.py:84-84
      End this invocation with rc.
    }
    // Source: vvaharness/cli/_commands.py:85-86
    In source order: Resolve source import from vvaharness.orchestrator.preflight import run_cache_probe; preserve alias and import-time effects. Then Evaluate once 0 if run_cache_probe(cfg) else 1; assign in source target order to rc.
  }
  // Source: vvaharness/cli/_commands.py:87-87
  End this invocation with rc.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_commands.py:89-148
// Source signature: _estimate(rest: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _estimate(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_commands.py:90-94
  In source order: Resolve source import from stat import S_ISDIR; preserve alias and import-time effects. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import trusted_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope import _walk_repo; preserve alias and import-time effects.
  // Source: vvaharness/cli/_commands.py:96-99
  if (the source predicate '--help' in rest or '-h' in rest is truthy) {
    // Source: vvaharness/cli/_commands.py:97-98
    In source order: Evaluate print(source_literal_97_14); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:99-99
    End this invocation with 0.
  }
  // Source: vvaharness/cli/_commands.py:100-100
  In source order: Evaluate once _repo_from(rest); assign in source target order to repo.
  // Source: vvaharness/cli/_commands.py:101-103
  if (the source predicate not repo is truthy) {
    // Source: vvaharness/cli/_commands.py:102-102
    In source order: Evaluate console.write('usage: vvaharness estimate --repo <path> [--config PATH]'); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:103-103
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:104-104
  In source order: Evaluate once Path(repo); assign in source target order to root.
  // Source: vvaharness/cli/_commands.py:105-115
  Perform the following protected operations {
    // Source: vvaharness/cli/_commands.py:106-106
    In source order: Evaluate once S_ISDIR(root.stat().st_mode); assign in source target order to directory.
  }
  // Source: vvaharness/cli/_commands.py:107-112
  On the first matching source exception FileNotFoundError as error, in handler order {
    // Source: vvaharness/cli/_commands.py:108-110
    if (the source predicate getattr(error, 'winerror', None) == 206 is truthy) {
      // Source: vvaharness/cli/_commands.py:109-109
      In source order: Evaluate console.write('estimate: invalid repository path: path is too long'); retain side effects and discard the expression result.
      // Source: vvaharness/cli/_commands.py:110-110
      End this invocation with 2.
    }
    // Source: vvaharness/cli/_commands.py:111-111
    In source order: Evaluate console.write(source_template_111_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:112-112
    End this invocation with 1.
  }
  // Source: vvaharness/cli/_commands.py:113-115
  On the first matching source exception (OSError, ValueError) as error, in handler order {
    // Source: vvaharness/cli/_commands.py:114-114
    In source order: Evaluate console.write(source_template_114_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:115-115
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:116-118
  if (the source predicate not directory is truthy) {
    // Source: vvaharness/cli/_commands.py:117-117
    In source order: Evaluate console.write(source_template_117_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:118-118
    End this invocation with 1.
  }
  // Source: vvaharness/cli/_commands.py:119-119
  In source order: Evaluate once _config_path_from_explicit(rest); assign in source target order to (cfg_path, explicit).
  // Source: vvaharness/cli/_commands.py:120-126
  Perform the following protected operations {
    // Source: vvaharness/cli/_commands.py:121-123
    In source order: Evaluate once trusted_config(cfg_path, root, explicit=explicit); assign in source target order to cfg_path. Then Evaluate once config_mod.load(cfg_path); assign in source target order to cfg. Then Evaluate once _walk_repo(str(root), cfg); assign in source target order to (inventory, _excluded).
  }
  // Source: vvaharness/cli/_commands.py:124-126
  On the first matching source exception (OSError, ValueError, config_mod.ConfigPolicyError) as error, in handler order {
    // Source: vvaharness/cli/_commands.py:125-125
    In source order: Evaluate console.write(source_template_125_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:126-126
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:127-127
  In source order: Evaluate once 0; assign in source target order to files, bytes_.
  // Source: vvaharness/cli/_commands.py:128-133
  for each relative in inventory {
    // Source: vvaharness/cli/_commands.py:129-133
    Perform the following protected operations {
      // Source: vvaharness/cli/_commands.py:130-131
      In source order: Apply source augmented assignment bytes_ += (root / relative).stat().st_size with source evaluation/in-place semantics. Then Apply source augmented assignment files += 1 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/cli/_commands.py:132-133
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/cli/_commands.py:133-133
      In source order: Perform no operation at this source statement.
    }
  }
  // Source: vvaharness/cli/_commands.py:134-138
  In source order: Evaluate once bytes_ // 4; assign in source target order to approx_tokens. Then Evaluate print(source_template_135_10); retain side effects and discard the expression result. Then Evaluate print(source_template_136_10); retain side effects and discard the expression result. Then Evaluate print(source_template_137_10); retain side effects and discard the expression result. Then Evaluate print(source_template_138_10); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_commands.py:139-143
  In source order: Evaluate once 250000 + 5 * approx_tokens if files else 0; assign in source target order to lower. Then Evaluate once 1000000 + 20 * approx_tokens if files else 0; assign in source target order to upper. Then Evaluate print(source_template_141_10); retain side effects and discard the expression result. Then Evaluate print('  assumes 250k-1M fixed prompt/tool overhead plus 5-20x source tokens.'); retain side effects and discard the expression result. Then Evaluate print('  Not a measured forecast or spend cap; agent turns, findings, retries'); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_commands.py:144-147
  In source order: Evaluate print('  and cache billing can put actual usage outside this range. S10/S11'); retain side effects and discard the expression result. Then Evaluate print('  and exploit verification are extra. No model calls were made.'); retain side effects and discard the expression result. Then Evaluate print('  Scope is before config dedup and optional auto-exclusions; use'); retain side effects and discard the expression result. Then Evaluate print('  --stop-after s3 for the final inventory. Cost depends on model pricing.'); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_commands.py:148-148
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_commands.py:150-206
// Source signature: _gc(rest: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gc(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_commands.py:151-157
  In source order: Retain source documentation literal source_literal_151_4; it is not a model call. Then Resolve source import import argparse; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.checkpoints import prune_checkpoints, run_id_for; preserve alias and import-time effects. Then Evaluate once argparse.ArgumentParser(prog='vvaharness gc'); assign in source target order to ap. Then Evaluate ap.add_argument('--keep-runs', type=int, default=100, help='retain the N most-recent run_ids (default: 100)'); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_commands.py:158-166
  In source order: Evaluate ap.add_argument('--max-age-days', type=int, default=5, help='delete runs older than D days (default: 5)'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--run', metavar='PATH', help='fully evict the run for this repo PATH (its run_id is derived from the path) instead of age/count pruning'); retain side effects and discard the expression result. Then Evaluate ap.add_argument('--dry-run', action='store_true', help='show what would be deleted; touch nothing'); retain side effects and discard the expression result. Then Evaluate once ap.parse_args(rest); assign in source target order to a. Then Resolve source import from vvaharness.orchestrator import store; preserve alias and import-time effects.
  // Source: vvaharness/cli/_commands.py:168-188
  if (the source predicate a.run is truthy) {
    // Source: vvaharness/cli/_commands.py:169-169
    In source order: Evaluate once run_id_for(a.run); assign in source target order to rid.
    // Source: vvaharness/cli/_commands.py:170-180
    if (the source predicate a.dry_run is truthy) {
      // Source: vvaharness/cli/_commands.py:171-175
      Perform the following protected operations {
        // Source: vvaharness/cli/_commands.py:172-172
        In source order: Evaluate once store.run_exists(rid); assign in source target order to exists.
      }
      // Source: vvaharness/cli/_commands.py:173-175
      On the first matching source exception store.StoreError as error, in handler order {
        // Source: vvaharness/cli/_commands.py:174-174
        In source order: Evaluate log.error(Event.STORE_UNUSABLE, detail=str(error)); retain side effects and discard the expression result.
        // Source: vvaharness/cli/_commands.py:175-175
        End this invocation with 2.
      }
      // Source: vvaharness/cli/_commands.py:176-179
      if (the source predicate exists is truthy) {
        // Source: vvaharness/cli/_commands.py:177-177
        In source order: Evaluate print(source_template_177_22); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/cli/_commands.py:179-179
        In source order: Evaluate print(source_template_179_22); retain side effects and discard the expression result.
      }
      // Source: vvaharness/cli/_commands.py:180-180
      End this invocation with 0.
    }
    // Source: vvaharness/cli/_commands.py:181-185
    Perform the following protected operations {
      // Source: vvaharness/cli/_commands.py:182-182
      In source order: Evaluate once store.delete_run(rid); assign in source target order to ok.
    }
    // Source: vvaharness/cli/_commands.py:183-185
    On the first matching source exception store.StoreError as e, in handler order {
      // Source: vvaharness/cli/_commands.py:184-184
      In source order: Evaluate log.error(Event.STORE_UNUSABLE, detail=str(e)); retain side effects and discard the expression result.
      // Source: vvaharness/cli/_commands.py:185-185
      End this invocation with 2.
    }
    // Source: vvaharness/cli/_commands.py:186-187
    In source order: Evaluate print(source_template_186_14); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:188-188
    End this invocation with 0.
  }
  // Source: vvaharness/cli/_commands.py:190-196
  Perform the following protected operations {
    // Source: vvaharness/cli/_commands.py:191-193
    In source order: Evaluate once prune_checkpoints(keep_runs=a.keep_runs, max_age_days=a.max_age_days, dry_run=a.dry_run); assign in source target order to r.
  }
  // Source: vvaharness/cli/_commands.py:194-196
  On the first matching source exception store.StoreError as e, in handler order {
    // Source: vvaharness/cli/_commands.py:195-195
    In source order: Evaluate log.error(Event.STORE_UNUSABLE, detail=str(e)); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:196-196
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:197-197
  In source order: Evaluate once '[dry-run] ' if a.dry_run else ''; assign in source target order to tag.
  // Source: vvaharness/cli/_commands.py:198-201
  if (the source predicate not store.db_location().exists() is truthy) {
    // Source: vvaharness/cli/_commands.py:199-199
    In source order: Evaluate print(source_template_199_14); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/cli/_commands.py:201-201
    In source order: Evaluate print(source_template_201_14); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_commands.py:202-203
  In source order: Evaluate print(source_template_202_10); retain side effects and discard the expression result.
  // Source: vvaharness/cli/_commands.py:204-205
  for each rid in r['deleted'] {
    // Source: vvaharness/cli/_commands.py:205-205
    In source order: Evaluate print(source_template_205_14); retain side effects and discard the expression result.
  }
  // Source: vvaharness/cli/_commands.py:206-206
  End this invocation with 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_commands.py:208-211
// Source signature: _validate(rest: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_commands.py:209-210
  In source order: Retain source documentation literal source_literal_209_4; it is not a model call. Then Resolve source import from vvaharness.validation.cli import main as validate_main; preserve alias and import-time effects.
  // Source: vvaharness/cli/_commands.py:211-211
  End this invocation with validate_main(rest).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_commands.py:213-234
// Source signature: _remediate(rest: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remediate(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_commands.py:214-218
  In source order: Retain source documentation literal source_literal_214_4; it is not a model call. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import trusted_config; preserve alias and import-time effects. Then Resolve source import from vvaharness.remediation_agent import remediate; preserve alias and import-time effects. Then Evaluate once _repo_from(rest); assign in source target order to repo.
  // Source: vvaharness/cli/_commands.py:219-221
  if (the source predicate not repo is truthy) {
    // Source: vvaharness/cli/_commands.py:220-220
    In source order: Evaluate console.write('usage: vvaharness remediate --repo <path>'); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:221-221
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:222-222
  In source order: Evaluate once _config_path_from_explicit(rest); assign in source target order to (cfg_path, explicit).
  // Source: vvaharness/cli/_commands.py:223-227
  Perform the following protected operations {
    // Source: vvaharness/cli/_commands.py:224-224
    In source order: Evaluate once trusted_config(cfg_path, repo, explicit=explicit); assign in source target order to cfg_path.
  }
  // Source: vvaharness/cli/_commands.py:225-227
  On the first matching source exception config_mod.ConfigPolicyError as e, in handler order {
    // Source: vvaharness/cli/_commands.py:226-226
    In source order: Evaluate console.write(source_template_226_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:227-227
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:228-230
  if (the source predicate not Path(cfg_path).exists() is truthy) {
    // Source: vvaharness/cli/_commands.py:229-229
    In source order: Evaluate console.write(source_template_229_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:230-230
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:231-231
  In source order: Evaluate once _load_and_configure(cfg_path, 'remediate'); assign in source target order to cfg.
  // Source: vvaharness/cli/_commands.py:232-233
  if (the source predicate cfg is None is truthy) {
    // Source: vvaharness/cli/_commands.py:233-233
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:234-234
  End this invocation with remediate(repo, rest, cfg).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/cli/_commands.py:236-254
// Source signature: _ev_replay(rest: list[str]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_replay(rest) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/cli/_commands.py:237-241
  In source order: Retain source documentation literal source_literal_237_4; it is not a model call. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.exploit_verification.replay.run import replay_run; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import trusted_config; preserve alias and import-time effects. Then Evaluate once _repo_from(rest); assign in source target order to repo.
  // Source: vvaharness/cli/_commands.py:242-244
  if (the source predicate not repo is truthy) {
    // Source: vvaharness/cli/_commands.py:243-243
    In source order: Evaluate console.write('usage: vvaharness ev-replay --repo <path>'); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:244-244
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:245-245
  In source order: Evaluate once _config_path_from_explicit(rest); assign in source target order to (cfg_path, explicit).
  // Source: vvaharness/cli/_commands.py:246-250
  Perform the following protected operations {
    // Source: vvaharness/cli/_commands.py:247-247
    In source order: Evaluate once trusted_config(cfg_path, repo, explicit=explicit); assign in source target order to cfg_path.
  }
  // Source: vvaharness/cli/_commands.py:248-250
  On the first matching source exception config_mod.ConfigPolicyError as e, in handler order {
    // Source: vvaharness/cli/_commands.py:249-249
    In source order: Evaluate console.write(source_template_249_22); retain side effects and discard the expression result.
    // Source: vvaharness/cli/_commands.py:250-250
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:251-251
  In source order: Evaluate once _load_and_configure(cfg_path, 'ev-replay'); assign in source target order to cfg.
  // Source: vvaharness/cli/_commands.py:252-253
  if (the source predicate cfg is None is truthy) {
    // Source: vvaharness/cli/_commands.py:253-253
    End this invocation with 2.
  }
  // Source: vvaharness/cli/_commands.py:254-254
  End this invocation with replay_run(repo, rest, cfg).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.cli._paths import _config_path_from, _config_path_from_explicit, _load_and_configure, _repo_from` at source line 22: `source_detail/vvaharness/cli/_paths.py.sudo.md`.
- `from vvaharness.util import console` at source line 28: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 28: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 29: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.orchestrator import probe_backends` at source line 53: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.util import environment as env` at source line 54: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import environment as env` at source line 54: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 92: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 92: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import trusted_config` at source line 93: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.scope import _walk_repo` at source line 94: `source_detail/vvaharness/scope/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import prune_checkpoints, run_id_for` at source line 154: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 166: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 166: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.validation.cli import main as validate_main` at source line 210: `source_detail/vvaharness/validation/cli/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 215: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 215: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import trusted_config` at source line 216: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import remediate` at source line 217: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import remediate` at source line 217: `source_detail/vvaharness/remediation_agent/remediate.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 238: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 238: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification.replay.run import replay_run` at source line 239: `source_detail/vvaharness/exploit_verification/replay/run.py.sudo.md`.
- `from vvaharness.orchestrator import trusted_config` at source line 240: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.preflight import run_cache_probe` at source line 85: `source_detail/vvaharness/orchestrator/preflight.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/cli/_commands.py.sudo.md). Exact strings in the evidence asset support this conversion.
