# vvaharness/manifest.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/manifest.py.evidence.json`. SHA-256: `d6c6a837575caf9a90220e166b4b73a09ea3dcc5693bfe41020e8dd404777f00`.

```sudo
// Source: vvaharness/manifest.py:15-32
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import contextlib; preserve alias and import-time effects. Then Resolve source import import datetime as _dt; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects.
// Source: vvaharness/manifest.py:33-37
In source order: Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects.
// Source: vvaharness/manifest.py:38-47
In source order: Resolve source import import types; preserve alias and import-time effects. Then Resolve source import from datetime import datetime; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once re.compile(source_literal_46_4); assign in source target order to _SECRET_FLAG_RX.
// Source: vvaharness/manifest.py:50-50
In source order: Evaluate once 'run_manifest'; assign in source target order to _RUN_MANIFEST_STEM.
// Source: vvaharness/manifest.py:53-59
// Source signature: _manifest_ts_from_started(started_iso: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _manifest_ts_from_started(started_iso) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:54-54
  In source order: Retain source documentation literal source_literal_54_4; it is not a model call.
  // Source: vvaharness/manifest.py:55-58
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:56-56
    In source order: Evaluate once _dt.datetime.fromisoformat(started_iso.replace('Z', '+00:00')); assign in source target order to dt.
  }
  // Source: vvaharness/manifest.py:57-58
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/manifest.py:58-58
    In source order: Evaluate once _dt.datetime.now(_dt.UTC); assign in source target order to dt.
  }
  // Source: vvaharness/manifest.py:59-59
  End this invocation with dt.astimezone(_dt.UTC).strftime('%Y%m%dT%H%M%SZ').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:62-74
// Source signature: _default_manifest_dest(started_iso: str, cwd: Path | None=None) -> Path
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _default_manifest_dest(started_iso, cwd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:63-66
  In source order: Retain source documentation literal source_literal_63_4; it is not a model call. Then Evaluate once cwd or Path.cwd(); assign in source target order to root. Then Evaluate once _manifest_ts_from_started(started_iso); assign in source target order to ts. Then Evaluate once 0; assign in source target order to i.
  // Source: vvaharness/manifest.py:67-74
  while (the source predicate True is truthy) {
    // Source: vvaharness/manifest.py:68-69
    In source order: Evaluate once '' if i == 0 else source_template_68_35; assign in source target order to suffix. Then Evaluate once root / source_template_69_27; assign in source target order to candidate.
    // Source: vvaharness/manifest.py:70-74
    Perform the following protected operations {
      // Source: vvaharness/manifest.py:71-71
      In source order: Evaluate os.close(os.open(candidate, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 420)); retain side effects and discard the expression result.
      // Source: vvaharness/manifest.py:72-72
      End this invocation with candidate.
    }
    // Source: vvaharness/manifest.py:73-74
    On the first matching source exception FileExistsError, in handler order {
      // Source: vvaharness/manifest.py:74-74
      In source order: Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:77-99
// Source signature: _scrub_argv(argv: list[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scrub_argv(argv) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:78-80
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call. Then For out, assign []; source annotation list[str]. Then Evaluate once (0, len(argv)); assign in source target order to (i, n).
  // Source: vvaharness/manifest.py:81-96
  while (the source predicate i < n is truthy) {
    // Source: vvaharness/manifest.py:82-82
    In source order: Evaluate once argv[i]; assign in source target order to tok.
    // Source: vvaharness/manifest.py:83-88
    if (the source predicate tok.startswith('-') and '=' in tok is truthy) {
      // Source: vvaharness/manifest.py:84-84
      In source order: Evaluate once tok.partition('='); assign in source target order to (flag, _eq, val).
      // Source: vvaharness/manifest.py:85-88
      if (the source predicate val and _SECRET_FLAG_RX.search(flag) is truthy) {
        // Source: vvaharness/manifest.py:86-87
        In source order: Evaluate out.append(source_template_86_27); retain side effects and discard the expression result. Then Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/manifest.py:88-88
        Continue the immediately enclosing source loop at its next iteration.
      }
    }
    // Source: vvaharness/manifest.py:89-94
    if (the source predicate tok.startswith('-') and _SECRET_FLAG_RX.search(tok) and (i + 1 < n) and (not argv[i + 1].startswith('-')) is truthy) {
      // Source: vvaharness/manifest.py:91-93
      In source order: Evaluate out.append(tok); retain side effects and discard the expression result. Then Evaluate out.append('***'); retain side effects and discard the expression result. Then Apply source augmented assignment i += 2 with source evaluation/in-place semantics.
      // Source: vvaharness/manifest.py:94-94
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/manifest.py:95-96
    In source order: Evaluate out.append(tok); retain side effects and discard the expression result. Then Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/manifest.py:98-98
  In source order: Resolve source import from vvaharness.report.redact import redact_tree; preserve alias and import-time effects.
  // Source: vvaharness/manifest.py:99-99
  End this invocation with redact_tree(out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:102-108
// Source signature: _metadata_failure(phase: str, error: Exception) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _metadata_failure(phase, error) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:103-108
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:104-106
    In source order: Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects. Then Evaluate console.write(source_template_106_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/manifest.py:107-108
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/manifest.py:108-108
    In source order: Perform no operation at this source statement.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:111-139
// Source signature: _git_sha(args: list[str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _git_sha(args) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:112-112
  In source order: Evaluate once None; assign in source target order to repo.
  // Source: vvaharness/manifest.py:113-117
  for each (i, a) in enumerate(args) {
    // Source: vvaharness/manifest.py:114-117
    if (the source predicate a == '--repo' and i + 1 < len(args) is truthy) {
      // Source: vvaharness/manifest.py:115-115
      In source order: Evaluate once args[i + 1]; assign in source target order to repo.
    }
    else {
      // Source: vvaharness/manifest.py:116-117
      if (the source predicate a.startswith('--repo=') is truthy) {
        // Source: vvaharness/manifest.py:117-117
        In source order: Evaluate once a.split('=', 1)[1]; assign in source target order to repo.
      }
    }
  }
  // Source: vvaharness/manifest.py:118-119
  if (the source predicate not repo is truthy) {
    // Source: vvaharness/manifest.py:119-119
    End this invocation with None.
  }
  // Source: vvaharness/manifest.py:121-126
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:122-122
    In source order: Evaluate once Path(repo).resolve(); assign in source target order to repo_dir.
    // Source: vvaharness/manifest.py:123-124
    if (the source predicate not repo_dir.is_dir() is truthy) {
      // Source: vvaharness/manifest.py:124-124
      End this invocation with None.
    }
  }
  // Source: vvaharness/manifest.py:125-126
  On the first matching source exception (OSError, ValueError), in handler order {
    // Source: vvaharness/manifest.py:126-126
    End this invocation with None.
  }
  // Source: vvaharness/manifest.py:127-139
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:128-129
    In source order: Evaluate once subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=str(repo_dir), capture_output=True, text=True, timeout=10); assign in source target order to out.
    // Source: vvaharness/manifest.py:130-132
    if (the source predicate out.returncode != 0 is truthy) {
      // Source: vvaharness/manifest.py:131-131
      In source order: Evaluate _metadata_failure('git revision unavailable', RuntimeError(source_template_131_71)); retain side effects and discard the expression result.
      // Source: vvaharness/manifest.py:132-132
      End this invocation with None.
    }
    // Source: vvaharness/manifest.py:133-133
    End this invocation with out.stdout.strip() or None.
  }
  // Source: vvaharness/manifest.py:134-136
  On the first matching source exception (OSError, subprocess.SubprocessError, UnicodeError) as error, in handler order {
    // Source: vvaharness/manifest.py:135-135
    In source order: Evaluate _metadata_failure('git revision unavailable', error); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:136-136
    End this invocation with None.
  }
  // Source: vvaharness/manifest.py:137-139
  On the first matching source exception Exception as error, in handler order {
    // Source: vvaharness/manifest.py:138-138
    In source order: Evaluate _metadata_failure('unexpected git metadata failure', error); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:139-139
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:143-150
In source order: Evaluate once ('graph_annotate', 'callgraph_creation', 'autoexclude', 'preprocess', 'threatmodel', 'decompose', 'deepdive', 'verify', 'dedup', 'chain', 'remediate', 'validate'); assign in source target order to _MODEL_ROLES. Then Evaluate once {'cli': 'anthropic', 'sdk': 'anthropic', 'openai': 'openai'}; assign in source target order to _FIXED_VIA_ROUTES.
// Source: vvaharness/manifest.py:153-162
// Source signature: _resolved_route(via: str, model_id: str, provider: str | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolved_route(via, model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:154-155
  In source order: Retain source documentation literal source_literal_154_4; it is not a model call. Then Evaluate once _FIXED_VIA_ROUTES.get(via); assign in source target order to fixed.
  // Source: vvaharness/manifest.py:156-157
  if (the source predicate fixed is not None is truthy) {
    // Source: vvaharness/manifest.py:157-157
    End this invocation with fixed.
  }
  // Source: vvaharness/manifest.py:158-161
  if (the source predicate via == 'deepagents' is truthy) {
    // Source: vvaharness/manifest.py:160-160
    In source order: Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects.
    // Source: vvaharness/manifest.py:161-161
    End this invocation with 'anthropic' if routes_to_anthropic(model_id, provider) else 'openai'.
  }
  // Source: vvaharness/manifest.py:162-162
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:166-169
In source order: Evaluate once 'deepagents'; assign in source target order to _DEEPAGENTS_VIA. Then Evaluate once 'openai'; assign in source target order to _OPENAI_VIA.
// Source: vvaharness/manifest.py:172-194
// Source signature: _resolved_transport_openai(model_id: str, override: bool | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolved_transport_openai(model_id, override) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:173-183
  In source order: Retain source documentation literal source_literal_173_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import EFFORT_REJECTIONS, TRANSPORT_MEMORY; preserve alias and import-time effects.
  // Source: vvaharness/manifest.py:184-185
  if (the source predicate model_id in TRANSPORT_MEMORY.chat_only is truthy) {
    // Source: vvaharness/manifest.py:185-185
    End this invocation with TRANSPORT_CHAT_COMPLETIONS.
  }
  // Source: vvaharness/manifest.py:186-187
  if (the source predicate override is True is truthy) {
    // Source: vvaharness/manifest.py:187-187
    End this invocation with TRANSPORT_RESPONSES.
  }
  // Source: vvaharness/manifest.py:188-190
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import resolve_use_responses_api; preserve alias and import-time effects.
  // Source: vvaharness/manifest.py:191-193
  if (the source predicate model_id in EFFORT_REJECTIONS.tools_off and resolve_use_responses_api(model_id, None, override) is truthy) {
    // Source: vvaharness/manifest.py:193-193
    End this invocation with TRANSPORT_RESPONSES.
  }
  // Source: vvaharness/manifest.py:194-194
  End this invocation with TRANSPORT_CHAT_COMPLETIONS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:197-222
// Source signature: _resolved_transport(via: str, model_id: str, provider: str | None, node: object) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolved_transport(via, model_id, provider, node) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:199-208
  In source order: Retain source documentation literal source_literal_199_4; it is not a model call. Then Evaluate once getattr(node, 'use_responses_api', None); assign in source target order to override.
  // Source: vvaharness/manifest.py:209-210
  if (the source predicate via == _OPENAI_VIA is truthy) {
    // Source: vvaharness/manifest.py:210-210
    End this invocation with _resolved_transport_openai(model_id, override).
  }
  // Source: vvaharness/manifest.py:211-212
  if (the source predicate via != _DEEPAGENTS_VIA is truthy) {
    // Source: vvaharness/manifest.py:212-212
    End this invocation with None.
  }
  // Source: vvaharness/manifest.py:213-220
  In source order: Resolve source import from vvaharness.backends.harness.deepagents.options.model_building import resolve_use_responses_api; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES; preserve alias and import-time effects. Then Evaluate once resolve_use_responses_api(model_id, provider, override); assign in source target order to allowed.
  // Source: vvaharness/manifest.py:221-222
  End this invocation with None if allowed is None else TRANSPORT_RESPONSES if allowed else TRANSPORT_CHAT_COMPLETIONS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:225-228
// Source signature: _effective_effort(cfg: object, name: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effective_effort(cfg, name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:226-227
  In source order: Retain source documentation literal source_literal_226_4; it is not a model call. Then Resolve source import from vvaharness.orchestrator.config_paths import role_effort; preserve alias and import-time effects.
  // Source: vvaharness/manifest.py:228-228
  End this invocation with role_effort(cfg, name).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:231-302
// Source signature: _models(cfg_path: Path) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _models(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:232-232
  In source order: Evaluate once 'could not load model roles'; assign in source target order to phase.
  // Source: vvaharness/manifest.py:233-302
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:234-237
    In source order: Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Evaluate once config_mod.load(cfg_path); assign in source target order to cfg. Then Evaluate once 'could not extract model roles'; assign in source target order to phase. Then Evaluate once {}; assign in source target order to roles.
    // Source: vvaharness/manifest.py:238-270
    for each name in _MODEL_ROLES {
      // Source: vvaharness/manifest.py:239-240
      In source order: Evaluate once getattr(cfg.models, name, None); assign in source target order to r. Then Evaluate once name == 'validate'; assign in source target order to is_validate.
      // Source: vvaharness/manifest.py:241-242
      if (the source predicate is_validate and r is not None is truthy) {
        // Source: vvaharness/manifest.py:242-242
        In source order: Evaluate once getattr(r, 'orchestrator', None); assign in source target order to r.
      }
      // Source: vvaharness/manifest.py:243-270
      if (the source predicate r is not None is truthy) {
        // Source: vvaharness/manifest.py:244-250
        In source order: Evaluate once getattr(r, 'id', str(r)); assign in source target order to model_id. Then Evaluate once getattr(r, 'provider', None); assign in source target order to provider. Then Evaluate once getattr(r, 'via', None) or 'cli'; assign in source target order to via. Then Evaluate once via; assign in source target order to declared_via.
        // Source: vvaharness/manifest.py:251-256
        if (the source predicate is_validate is truthy) {
          // Source: vvaharness/manifest.py:253-256
          In source order: Resolve source import from vvaharness.validation.config.validate_role import normalize_validate_backend; preserve alias and import-time effects. Then Evaluate once normalize_validate_backend(via, provider); assign in source target order to (via, provider).
        }
        // Source: vvaharness/manifest.py:257-270
        In source order: Evaluate once getattr(r, 'use_responses_api', None); assign in source target order to use_responses_api. Then Evaluate once {'id': model_id, 'via': via, 'provider': provider, 'resolved_route': _resolved_route(via, model_id, provider), 'resolved_transport': _resolved_transport(via, model_id, provider, r), 'use_responses_api': use_responses_api if isinstance(use_responses_api, bool) else None, 'declared_via': declared_via, 'effective_effort': _effective_effort(cfg, name)}; assign in source target order to roles[name].
      }
    }
    // Source: vvaharness/manifest.py:272-272
    In source order: Evaluate once getattr(cfg.models, 'exploit_verification', None); assign in source target order to ev.
    // Source: vvaharness/manifest.py:273-298
    if (the source predicate ev is not None is truthy) {
      // Source: vvaharness/manifest.py:274-274
      In source order: Resolve source import from vvaharness.exploit_verification.settings import EV_MODULES, ev_effort; preserve alias and import-time effects.
      // Source: vvaharness/manifest.py:275-298
      for each sub_name in EV_MODULES {
        // Source: vvaharness/manifest.py:276-276
        In source order: Evaluate once getattr(ev, sub_name, None); assign in source target order to node.
        // Source: vvaharness/manifest.py:277-278
        if (the source predicate node is None is truthy) {
          // Source: vvaharness/manifest.py:278-278
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/manifest.py:280-298
        In source order: Evaluate once getattr(node, 'id', str(node)); assign in source target order to model_id. Then Evaluate once getattr(node, 'provider', None); assign in source target order to provider. Then Evaluate once getattr(node, 'via', None) or 'cli'; assign in source target order to via. Then Evaluate once getattr(node, 'use_responses_api', None); assign in source target order to use_responses_api. Then Evaluate once {'id': model_id, 'via': via, 'provider': provider, 'resolved_route': _resolved_route(via, model_id, provider), 'resolved_transport': _resolved_transport(via, model_id, provider, node), 'use_responses_api': use_responses_api if isinstance(use_responses_api, bool) else None, 'declared_via': via, 'effective_effort': ev_effort(cfg, sub_name)}; assign in source target order to roles[f'exploit_verification.{sub_name}'].
      }
    }
    // Source: vvaharness/manifest.py:299-299
    End this invocation with roles.
  }
  // Source: vvaharness/manifest.py:300-302
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/manifest.py:301-301
    In source order: Evaluate _metadata_failure(phase, e); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:302-302
    End this invocation with {}.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:305-316
// Source signature: _model_spec(role) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _model_spec(role) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:306-307
  if (the source predicate role is None is truthy) {
    // Source: vvaharness/manifest.py:307-307
    End this invocation with None.
  }
  // Source: vvaharness/manifest.py:308-310
  In source order: Evaluate once {'id': getattr(role, 'id', str(role)), 'via': getattr(role, 'via', 'cli')}; assign in source target order to spec. Then Evaluate once getattr(role, 'provider', None); assign in source target order to provider.
  // Source: vvaharness/manifest.py:311-312
  if (the source predicate provider is truthy) {
    // Source: vvaharness/manifest.py:312-312
    In source order: Evaluate once provider; assign in source target order to spec['provider'].
  }
  // Source: vvaharness/manifest.py:313-313
  In source order: Evaluate once getattr(role, 'use_responses_api', None); assign in source target order to use_responses_api.
  // Source: vvaharness/manifest.py:314-315
  if (the source predicate isinstance(use_responses_api, bool) is truthy) {
    // Source: vvaharness/manifest.py:315-315
    In source order: Evaluate once use_responses_api; assign in source target order to spec['use_responses_api'].
  }
  // Source: vvaharness/manifest.py:316-316
  End this invocation with spec.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:319-321
In source order: Evaluate once 'orchestrator'; assign in source target order to _PANEL_ORCHESTRATOR. Then Evaluate once ('security_architect', 'penetration_tester', 'cross_repo_analyzer'); assign in source target order to _PANEL_PERSONAS.
// Source: vvaharness/manifest.py:324-334
// Source signature: _panel_specs(validate: object) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _panel_specs(validate) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:325-327
  In source order: Retain source documentation literal source_literal_325_4; it is not a model call. Then Evaluate once {}; assign in source target order to specs. Then Evaluate once getattr(validate, _PANEL_ORCHESTRATOR, None); assign in source target order to orch.
  // Source: vvaharness/manifest.py:328-329
  if (the source predicate orch is not None is truthy) {
    // Source: vvaharness/manifest.py:329-329
    In source order: Evaluate once orch; assign in source target order to specs[_PANEL_ORCHESTRATOR].
  }
  // Source: vvaharness/manifest.py:330-333
  for each name in _PANEL_PERSONAS {
    // Source: vvaharness/manifest.py:331-331
    In source order: Evaluate once getattr(validate, name, None); assign in source target order to spec.
    // Source: vvaharness/manifest.py:332-333
    if (the source predicate spec is not None is truthy) {
      // Source: vvaharness/manifest.py:333-333
      In source order: Evaluate once spec; assign in source target order to specs[name].
    }
  }
  // Source: vvaharness/manifest.py:334-334
  End this invocation with specs.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:337-347
// Source signature: _panel_entry(spec: object, via: str, provider: str | None, declared_via: str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _panel_entry(spec, via, provider, declared_via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:339-339
  In source order: Evaluate once getattr(spec, 'id', str(spec)); assign in source target order to model_id.
  // Source: vvaharness/manifest.py:340-347
  End this invocation with {'id': model_id, 'via': via, 'provider': provider, 'resolved_route': _resolved_route(via, model_id, provider), 'declared_via': declared_via}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:350-371
// Source signature: _validation_panel(validate: object) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validation_panel(validate) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:351-351
  In source order: Retain source documentation literal source_literal_351_4; it is not a model call.
  // Source: vvaharness/manifest.py:353-354
  if (the source predicate validate is None is truthy) {
    // Source: vvaharness/manifest.py:354-354
    End this invocation with {}.
  }
  // Source: vvaharness/manifest.py:355-356
  In source order: Evaluate once _panel_specs(validate); assign in source target order to specs. Then Evaluate once specs.get(_PANEL_ORCHESTRATOR); assign in source target order to orch.
  // Source: vvaharness/manifest.py:357-360
  if (the source predicate orch is None is truthy) {
    // Source: vvaharness/manifest.py:359-360
    End this invocation with {name: {'id': getattr(spec, 'id', str(spec))} for name, spec in specs.items()}.
  }
  // Source: vvaharness/manifest.py:362-369
  In source order: Resolve source import from vvaharness.validation.config.validate_role import normalize_validate_backend; preserve alias and import-time effects. Then Evaluate once getattr(orch, 'via', None) or 'cli'; assign in source target order to via. Then Evaluate once via; assign in source target order to declared_via. Then Evaluate once normalize_validate_backend(via, getattr(orch, 'provider', None)); assign in source target order to (via, provider).
  // Source: vvaharness/manifest.py:370-371
  End this invocation with {name: _panel_entry(spec, via, provider, declared_via) for name, spec in specs.items()}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:374-375
// Source signature: _pick(section, *names: str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pick(section, names) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:375-375
  End this invocation with {name: getattr(section, name, None) for name in names}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:378-386
// Source signature: _input_fingerprint(value, config_dir: Path) -> dict | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _input_fingerprint(value, config_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:379-380
  if (the source predicate value is None or not str(value).strip() is truthy) {
    // Source: vvaharness/manifest.py:380-380
    End this invocation with None.
  }
  // Source: vvaharness/manifest.py:381-382
  In source order: Evaluate once Path(str(value)); assign in source target order to configured_path. Then Evaluate once configured_path if configured_path.is_absolute() else config_dir / configured_path; assign in source target order to resolved_path.
  // Source: vvaharness/manifest.py:383-386
  End this invocation with {'path': str(configured_path), 'sha256': _config_sha256(resolved_path)}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:389-480
// Source signature: _effective_scan_controls(cfg_path: Path) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effective_scan_controls(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:390-390
  In source order: Retain source documentation literal source_literal_390_4; it is not a model call.
  // Source: vvaharness/manifest.py:391-480
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:392-397
    In source order: Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Evaluate once config_mod.load(cfg_path); assign in source target order to cfg. Then Evaluate once _validation_panel(getattr(cfg.models, 'validate', None)); assign in source target order to panel. Then Evaluate once Path(getattr(cfg, '_config_dir', cfg_path.parent)); assign in source target order to config_dir. Then Evaluate once getattr(cfg, 'inject', None); assign in source target order to inject.
    // Source: vvaharness/manifest.py:398-474
    In source order: Evaluate once getattr(cfg, 'step_remediate', None); assign in source target order to remediate. Then Evaluate once {'cache': _pick(cfg, 'cache_markers', 'cache_route', 'cache_min_block_tokens'), 'thinking': _pick(cfg, 'think_in_prompt'), 'refusals': _pick(cfg, 'refusal_retries'), 'step0': _pick(cfg.step0, 'callgraph_detection', 'min_graph_nodes_for_gate'), 'step1': _pick(cfg.step1, 'auto_exclude', 'auto_exclude_max_tokens', 'auto_exclude_protect_templates', 'auto_exclude_protect_key_material', 'auto_exclude_protect_secrets', 'auto_exclude_protect_client_sinks', 'max_file_kb', 'config_dedup'), 'step2': _pick(cfg.step2, 'max_tokens', 'max_threats', 'baseline', 'max_doc_chars', 'max_manifest_chars', 'max_modules', 'max_entry_points', 'max_inventory_files', 'bash', 'max_config_reps', 'max_api_artefacts', 'max_graph_files', 'max_graph_sinks', 'max_graph_edges', 'graph_tools', 'require_graph', 'require_graph_rejections', 'empty_retry', 'deadline', 'replay_timeout', 'resume_timeout', 'replay_max_tokens', 'max_model_calls'), 'step4': _pick(cfg.step4, 'parallel', 'max_turns', 'line_bucket', 'max_findings_per_run', 'max_tokens', 'cwe_tools', 'cwe_tool_budget', 'graph_tool_budget', 'planning', 'inline_source', 'evidence_gate', 'evidence_gate_refusals', 'skills', 'effort', 'require_graph', 'bash', 'max_model_calls', 'batch_size', 'split_retry', 'max_extra_cwes', 'deadline', 'replay_timeout', 'resume_timeout', 'replay_max_tokens', 'allowed_tools'), 'step5_prefilter': _pick(getattr(cfg, 'step5_prefilter', None), 'line_tolerance', 'sink_reanchor', 'sink_reanchor_max_move_lines'), 'step5_detectors': _pick(getattr(cfg, 'step5_detectors', None), 'enabled', 'max_rows'), 'step6_verify': _pick(cfg.step6_verify, 'parallel', 'min_confidence', 'max_budget_usd', 'max_turns', 'allowed_tools', 'batch_size', 'inline_source', 'graph_tools', 'graph_tool_budget', 'max_model_calls', 'batch_wall_clock_ceiling', 'batch_deadline', 'replay_timeout', 'resume_timeout', 'replay_max_tokens', 'trait_stamps', 'reframe_enabled', 'max_tokens', 'split_retry', 'require_graph', 'evidence_gate_refusals'), 'step7_dedup': _pick(cfg.step7_dedup, 'line_tolerance', 'semantic', 'max_tokens', 'per_sink_keep'), 'step8': _pick(cfg.step8, 'max_tokens', 'timeout', 'max_model_calls', 'max_turns', 'deadline', 'resume_timeout', 'prompt_token_budget', 'severity_lift_gate', 'chain_quality_checks', 'chain_dedup', 'prompt_fact_blocks', 'hop_text'), 'step9': _pick(getattr(cfg, 'step9', None), 'duplicate_result_guard'), 'output': _pick(getattr(cfg, 'output', None), 'posture_channel', 'emit_unreachable_appendix'), 'cli': _pick(getattr(cfg, 'cli', None), 'mcp_tools', 'restricted'), 'step_remediate': _pick(remediate, 'enabled', 'enforce_policy', 'top_n_findings', 'max_budget_usd', 'max_turns', 'allowed_tools'), 'remediation_model': _model_spec(getattr(cfg.models, 'remediate', None)), 'step_validate': _pick(cfg.step_validate, 'enabled', 'effort', 'max_turns', 'max_budget_usd', 'max_findings', 'timeout', 'allowed_tools'), 'validation_panel': panel, 'input_hashes': {'cve_file': _input_fingerprint(getattr(inject, 'cve_file', None), config_dir), 'controls_file': _input_fingerprint(getattr(inject, 'controls_file', None), config_dir), 'cmdb_file': _input_fingerprint(getattr(inject, 'cmdb_file', None), config_dir), 'policy_file': _input_fingerprint(getattr(remediate, 'policy_file', None), config_dir), 'playbook_file': _input_fingerprint(getattr(remediate, 'playbook_file', None), config_dir)}}; assign in source target order to controls.
    // Source: vvaharness/manifest.py:475-475
    End this invocation with controls.
  }
  // Source: vvaharness/manifest.py:476-480
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/manifest.py:477-479
    In source order: Evaluate console.write(source_template_478_12); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:480-480
    End this invocation with {}.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:483-490
// Source signature: _pricing_file(cfg_path: Path) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pricing_file(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:484-490
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:485-486
    In source order: Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Evaluate once config_mod.load(cfg_path); assign in source target order to cfg.
    // Source: vvaharness/manifest.py:487-487
    End this invocation with getattr(getattr(cfg, 'pricing', None), 'file', None).
  }
  // Source: vvaharness/manifest.py:488-490
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/manifest.py:489-489
    In source order: Evaluate console.write(source_template_489_22); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:490-490
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:493-511
// Source signature: _telemetry_fields(cfg_path: Path, models: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _telemetry_fields(cfg_path, models) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:494-494
  In source order: Retain source documentation literal source_literal_494_4; it is not a model call.
  // Source: vvaharness/manifest.py:496-511
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:497-507
    In source order: Resolve source import from vvaharness.util import stage_telemetry; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.pricing import load_pricing_cached; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects. Then Evaluate once {role: spec['id'] for role, spec in models.items() if isinstance(spec, dict) and spec.get('id')}; assign in source target order to role_models. Then Evaluate once stage_telemetry.compose_stage_section(stage_telemetry.STAGES.snapshot(), TOKENS.snapshot(), role_models, load_pricing_cached(_pricing_file(cfg_path)), stage_telemetry.CACHED_PROVENANCE.snapshot()); assign in source target order to section.
    // Source: vvaharness/manifest.py:508-508
    End this invocation with dict(section).
  }
  // Source: vvaharness/manifest.py:509-511
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/manifest.py:510-510
    In source order: Evaluate console.write(source_template_510_22); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:511-511
    End this invocation with {}.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:514-521
// Source signature: _config_sha256(cfg_path: Path) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _config_sha256(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:515-516
  if (the source predicate not cfg_path.exists() is truthy) {
    // Source: vvaharness/manifest.py:516-516
    End this invocation with None.
  }
  // Source: vvaharness/manifest.py:517-521
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:518-518
    End this invocation with hashlib.sha256(cfg_path.read_bytes()).hexdigest().
  }
  // Source: vvaharness/manifest.py:519-521
  On the first matching source exception OSError as e, in handler order {
    // Source: vvaharness/manifest.py:520-520
    In source order: Evaluate console.write(source_template_520_22); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:521-521
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:522-531
// Source signature: _ev_collection() -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_collection() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:523-523
  In source order: Retain source documentation literal source_literal_523_4; it is not a model call.
  // Source: vvaharness/manifest.py:525-531
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:526-527
    In source order: Resolve source import from vvaharness.exploit_verification.options import collection_path; preserve alias and import-time effects. Then Evaluate once collection_path(); assign in source target order to path.
    // Source: vvaharness/manifest.py:528-528
    End this invocation with Path(path) if path else None.
  }
  // Source: vvaharness/manifest.py:529-531
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/manifest.py:530-530
    In source order: Evaluate console.write(source_template_530_22); retain side effects and discard the expression result.
    // Source: vvaharness/manifest.py:531-531
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:534-539
// Source signature: _refresh_resolved_transport(m: dict) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refresh_resolved_transport(m) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:535-535
  In source order: Retain source documentation literal source_literal_535_4; it is not a model call.
  // Source: vvaharness/manifest.py:536-539
  for each role in (m.get('models') or {}).values() {
    // Source: vvaharness/manifest.py:537-539
    In source order: Evaluate once types.SimpleNamespace(use_responses_api=role.get('use_responses_api')); assign in source target order to node. Then Evaluate once _resolved_transport(role['via'], role['id'], role.get('provider'), node); assign in source target order to role['resolved_transport'].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/manifest.py:542-543
interface _Terminated {
  Describe the source Python type, preserving its base/metaclass expression order: SystemExit.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/manifest.py:543-543
  In source order: Retain source documentation literal source_literal_543_4; it is not a model call.
}
// Source: vvaharness/manifest.py:547-624
// Source: vvaharness/manifest.py:546-546
Before creating this callable, evaluate and retain decorators top-to-bottom: contextlib.contextmanager.
// Source: vvaharness/manifest.py:547-624
// Source signature: capture(cfg_path: Path, args: list[str], out: Path | None=None)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn capture(cfg_path, args, out) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/manifest.py:548-569
  In source order: Evaluate once Path(cfg_path); assign in source target order to cfg_path. Then Resolve source import from vvaharness import __version__; preserve alias and import-time effects. Then Evaluate once _ev_collection(); assign in source target order to ev_collection. Then For m, assign {'tool': 'vvaharness', 'version': __version__, 'started': datetime.now(_dt.UTC).isoformat(), 'argv': _scrub_argv(args), 'config_profile': str(cfg_path), 'config_sha256': _config_sha256(cfg_path), 'config_local_sha256': _config_sha256(cfg_path.with_name('config.local.yaml')), 'ev_api_collection': str(ev_collection) if ev_collection else None, 'ev_api_collection_sha256': _config_sha256(ev_collection) if ev_collection else None, 'models': _models(cfg_path), 'effective_scan_controls': _effective_scan_controls(cfg_path), 'target_git_sha': _git_sha(args), 'exit_code': None}; source annotation dict. Then Evaluate once time.time(); assign in source target order to t0.
  // Source: vvaharness/manifest.py:570-624
  Perform the following protected operations {
    // Source: vvaharness/manifest.py:571-571
    In source order: Yield m; suspend this generator until resumed.
  }
  // Source: vvaharness/manifest.py:572-577
  On the first matching source exception (KeyboardInterrupt, _Terminated) as e, in handler order {
    // Source: vvaharness/manifest.py:574-575
    if (the source predicate m.get('exit_code') is None is truthy) {
      // Source: vvaharness/manifest.py:575-575
      In source order: Evaluate once 130 if isinstance(e, KeyboardInterrupt) else 143; assign in source target order to m['exit_code'].
    }
    // Source: vvaharness/manifest.py:576-576
    In source order: Evaluate once 'SIGINT' if isinstance(e, KeyboardInterrupt) else 'SIGTERM'; assign in source target order to m['exit_cause'].
    // Source: vvaharness/manifest.py:577-577
    Raise the currently handled exception.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/manifest.py:580-624
    if (the source predicate m.get('exit_code') is not None is truthy) {
      // Source: vvaharness/manifest.py:581-582
      In source order: Evaluate once datetime.now(_dt.UTC).isoformat(); assign in source target order to m['ended']. Then Evaluate once round(time.time() - t0, 1); assign in source target order to m['duration_sec'].
      // Source: vvaharness/manifest.py:583-586
      Perform the following protected operations {
        // Source: vvaharness/manifest.py:584-584
        In source order: Evaluate _refresh_resolved_transport(m); retain side effects and discard the expression result.
      }
      // Source: vvaharness/manifest.py:585-586
      On the first matching source exception Exception, in handler order {
        // Source: vvaharness/manifest.py:586-586
        In source order: Perform no operation at this source statement.
      }
      // Source: vvaharness/manifest.py:587-587
      In source order: Evaluate m.update(_telemetry_fields(cfg_path, m.get('models') or {})); retain side effects and discard the expression result.
      // Source: vvaharness/manifest.py:589-595
      Perform the following protected operations {
        // Source: vvaharness/manifest.py:590-591
        In source order: Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Evaluate once _errlog.counts_by_stage(); assign in source target order to errors.
        // Source: vvaharness/manifest.py:592-593
        if (the source predicate errors is truthy) {
          // Source: vvaharness/manifest.py:593-593
          In source order: Evaluate once errors; assign in source target order to m['errors_by_stage'].
        }
      }
      // Source: vvaharness/manifest.py:594-595
      On the first matching source exception Exception, in handler order {
        // Source: vvaharness/manifest.py:595-595
        In source order: Perform no operation at this source statement.
      }
      // Source: vvaharness/manifest.py:597-603
      Perform the following protected operations {
        // Source: vvaharness/manifest.py:598-599
        In source order: Resolve source import from vvaharness.orchestrator import case_rollup; preserve alias and import-time effects. Then Evaluate once case_rollup.totals(); assign in source target order to rollup.
        // Source: vvaharness/manifest.py:600-601
        if (the source predicate rollup is truthy) {
          // Source: vvaharness/manifest.py:601-601
          In source order: Evaluate once rollup; assign in source target order to m['remediation'].
        }
      }
      // Source: vvaharness/manifest.py:602-603
      On the first matching source exception Exception, in handler order {
        // Source: vvaharness/manifest.py:603-603
        In source order: Perform no operation at this source statement.
      }
      // Source: vvaharness/manifest.py:605-615
      Perform the following protected operations {
        // Source: vvaharness/manifest.py:606-609
        In source order: Resolve source import from vvaharness.report.redact import redact_tree; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS as _COUNTERS; preserve alias and import-time effects. Then Evaluate once _COUNTERS.snapshot_cumulative(); assign in source target order to snap.
        // Source: vvaharness/manifest.py:610-613
        if (the source predicate snap is truthy) {
          // Source: vvaharness/manifest.py:612-613
          In source order: Evaluate once redact_tree({k: snap[k] for k in sorted(snap)}); assign in source target order to m['counters'].
        }
      }
      // Source: vvaharness/manifest.py:614-615
      On the first matching source exception Exception, in handler order {
        // Source: vvaharness/manifest.py:615-615
        In source order: Perform no operation at this source statement.
      }
      // Source: vvaharness/manifest.py:616-616
      In source order: Evaluate once out or _default_manifest_dest(str(m.get('started') or '')); assign in source target order to dest.
      // Source: vvaharness/manifest.py:617-624
      Perform the following protected operations {
        // Source: vvaharness/manifest.py:619-621
        In source order: Evaluate dest.write_text(json.dumps(m, indent=2, default=str), encoding='utf-8'); retain side effects and discard the expression result. Then Evaluate console.write(source_template_621_30); retain side effects and discard the expression result.
      }
      // Source: vvaharness/manifest.py:622-624
      On the first matching source exception OSError as e, in handler order {
        // Source: vvaharness/manifest.py:623-624
        In source order: Evaluate console.write(source_template_623_30); retain side effects and discard the expression result.
      }
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
```

## Local import links

- `from vvaharness.util import console` at source line 42: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 42: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.report.redact import redact_tree` at source line 98: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES` at source line 179: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.models import EFFORT_REJECTIONS, TRANSPORT_MEMORY` at source line 183: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import resolve_use_responses_api` at source line 188: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.options.model_building import resolve_use_responses_api` at source line 213: `source_detail/vvaharness/backends/harness/deepagents/options/model_building.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import TRANSPORT_CHAT_COMPLETIONS, TRANSPORT_RESPONSES` at source line 216: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import role_effort` at source line 227: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.validation.config.validate_role import normalize_validate_backend` at source line 362: `source_detail/vvaharness/validation/config/validate_role.py.sudo.md`.
- `from vvaharness import __version__` at source line 549: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 104: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 160: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 234: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 234: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 392: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 392: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 485: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 485: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.util import stage_telemetry` at source line 497: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import stage_telemetry` at source line 497: `source_detail/vvaharness/util/stage_telemetry.py.sudo.md`.
- `from vvaharness.util.pricing import load_pricing_cached` at source line 498: `source_detail/vvaharness/util/pricing.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 499: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.exploit_verification.options import collection_path` at source line 526: `source_detail/vvaharness/exploit_verification/options.py.sudo.md`.
- `from vvaharness.exploit_verification.settings import EV_MODULES, ev_effort` at source line 274: `source_detail/vvaharness/exploit_verification/settings.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 590: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 590: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.orchestrator import case_rollup` at source line 598: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import case_rollup` at source line 598: `source_detail/vvaharness/orchestrator/case_rollup.py.sudo.md`.
- `from vvaharness.report.redact import redact_tree` at source line 606: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS as _COUNTERS` at source line 607: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.validation.config.validate_role import normalize_validate_backend` at source line 253: `source_detail/vvaharness/validation/config/validate_role.py.sudo.md`.
