# vvaharness/orchestrator/preflight.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/preflight.py.evidence.json`. SHA-256: `7a3addeb61be6f6711cfe1ef1234e5dfe810fb79aea075878b3c94f79a2e292c`.

```sudo
// Source: vvaharness/orchestrator/preflight.py:16-21
In source order: Retain source documentation literal source_literal_16_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/preflight.py:22-26
In source order: Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import tempfile; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/preflight.py:27-43
In source order: Resolve source import from urllib.parse import urlsplit; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.models import DegenerateResponseError, HarnessJSONDecodeError, HarnessMessageParseError, TruncatedResponseError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import cli, sdk; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import openai as oai; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.models import ClockKind, effort_scaled_seconds, rejection_text, validate_detection_tools; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/preflight.py:44-58
In source order: Resolve source import from vvaharness.backends.llm.registry import DEEPAGENTS_ROLES, POST_SCAN_ROLES, unrecognized_model_keys, use_responses_api_of; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import resolve as resolve_model; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.tls import coerce_verify; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import _iter_model_roles, _resolve_against, highest_effort, role_effort; preserve alias and import-time effects. Then Resolve source import from vvaharness.report.redact import redact; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/preflight.py:59-63
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.exceptions import exception_chain; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.response_quality import stage_floors; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.tokens import TOKENS; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/preflight.py:64-68
In source order: Resolve source import from vvaharness.util.tokens import estimate_tokens as estimate_tokens; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/preflight.py:71-77
// Source signature: _resolve_verify_path(cfg_dir: Path, value: object) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_verify_path(cfg_dir, value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:72-74
  In source order: Retain source documentation literal source_literal_72_4; it is not a model call. Then Evaluate once coerce_verify(value); assign in source target order to coerced.
  // Source: vvaharness/orchestrator/preflight.py:75-76
  if (the source predicate isinstance(coerced, str) and coerced.strip() is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:76-76
    End this invocation with _resolve_against(cfg_dir, coerced).
  }
  // Source: vvaharness/orchestrator/preflight.py:77-77
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:80-91
// Source signature: _resolve_cert_chain(cfg_dir: Path, cert: object) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_cert_chain(cfg_dir, cert) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:81-81
  In source order: Retain source documentation literal source_literal_81_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:83-84
  if (the source predicate isinstance(cert, str) is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:84-84
    End this invocation with _resolve_against(cfg_dir, cert).
  }
  // Source: vvaharness/orchestrator/preflight.py:85-90
  if (the source predicate isinstance(cert, (tuple, list)) is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:86-90
    End this invocation with tuple((_resolve_against(cfg_dir, m) if i < 2 and isinstance(m, str) and m.strip() else m for i, m in enumerate(cert))).
  }
  // Source: vvaharness/orchestrator/preflight.py:91-91
  End this invocation with cert.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:94-96
// Source signature: _mask(v: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mask(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:95-95
  In source order: Retain source documentation literal source_literal_95_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:96-96
  End this invocation with 'set ✓' if v else '<unset>'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:99-154
// Source signature: configure_backends(cfg, cfg_dir: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn configure_backends(cfg, cfg_dir) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:100-107
  In source order: Retain source documentation literal source_literal_100_4; it is not a model call. Then Evaluate once {resolve_model(m).via for _, m in _iter_model_roles(cfg)}; assign in source target order to vias. Then Evaluate once vias <= {'sdk', 'deepagents'}; assign in source target order to sdk_sole. Then Evaluate once getattr(cfg, 'cache_markers', None); assign in source target order to _cache_markers. Then Evaluate once getattr(cfg, 'cache_min_block_tokens', None); assign in source target order to _cache_min_block.
  // Source: vvaharness/orchestrator/preflight.py:109-115
  In source order: Evaluate once getattr(cfg, 'cache_route', None); assign in source target order to _cache_route. Then Evaluate sdk.configure(cache_markers=_cache_markers, cache_min_block_tokens=_cache_min_block, cache_route=_cache_route); retain side effects and discard the expression result. Then Evaluate oai.configure(cache_markers=_cache_markers); retain side effects and discard the expression result. Then Evaluate once getattr(cfg, 'sdk', None); assign in source target order to sdk_cfg.
  // Source: vvaharness/orchestrator/preflight.py:116-127
  if (the source predicate sdk_cfg is not None is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:117-127
    In source order: Evaluate once getattr(sdk_cfg, 'ca_cert', None) or None; assign in source target order to ca_cert. Then Evaluate once getattr(sdk_cfg, 'client_cert', None) or None; assign in source target order to client_cert. Then Evaluate sdk.configure(api_key=getattr(sdk_cfg, 'api_key', None), base_url=getattr(sdk_cfg, 'base_url', None), verify_ssl=_resolve_verify_path(cfg_dir, getattr(sdk_cfg, 'verify_ssl', True)), ca_cert=_resolve_against(cfg_dir, ca_cert) if ca_cert else None, client_cert=_resolve_cert_chain(cfg_dir, client_cert), no_proxy=getattr(sdk_cfg, 'no_proxy', None) or None, allow_api_key_fallback=sdk_sole); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:128-128
  In source order: Evaluate once getattr(cfg, 'openai', None); assign in source target order to oai_cfg.
  // Source: vvaharness/orchestrator/preflight.py:129-140
  if (the source predicate oai_cfg is not None is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:130-140
    In source order: Evaluate once getattr(oai_cfg, 'ca_cert', None) or None; assign in source target order to ca_cert. Then Evaluate oai.configure(api_key=getattr(oai_cfg, 'api_key', None), base_url=getattr(oai_cfg, 'base_url', None), verify_ssl=_resolve_verify_path(cfg_dir, getattr(oai_cfg, 'verify_ssl', True)), ca_cert=_resolve_against(cfg_dir, ca_cert) if ca_cert else None, client_cert=getattr(oai_cfg, 'client_cert', None) or None, organization=getattr(oai_cfg, 'organization', None) or None, no_proxy=getattr(oai_cfg, 'no_proxy', None) or None); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:142-142
  In source order: Evaluate once getattr(cfg, 'cli', None); assign in source target order to cli_cfg.
  // Source: vvaharness/orchestrator/preflight.py:143-154
  if (the source predicate cli_cfg is not None is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:144-154
    In source order: Evaluate once getattr(cli_cfg, 'ca_cert', None) or None; assign in source target order to ca_cert. Then Evaluate once getattr(cli_cfg, 'client_cert', None) or None; assign in source target order to client_cert. Then Evaluate cli.configure(verify_ssl=_resolve_verify_path(cfg_dir, getattr(cli_cfg, 'verify_ssl', True)), ca_cert=_resolve_against(cfg_dir, ca_cert) if ca_cert else None, client_cert=_resolve_cert_chain(cfg_dir, client_cert), no_proxy=getattr(cli_cfg, 'no_proxy', None) or None, effort=getattr(cli_cfg, 'effort', None) or None, restricted=bool(getattr(cli_cfg, 'restricted', True))); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:158-160
// Source signature: _reachable_despite_degenerate_reply(e: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reachable_despite_degenerate_reply(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:159-159
  In source order: Retain source documentation literal source_literal_159_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:160-160
  End this invocation with isinstance(e, DegenerateResponseError).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:163-166
// Source signature: _reachable_despite_truncated_reply(e: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reachable_despite_truncated_reply(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:164-164
  In source order: Retain source documentation literal source_literal_164_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:166-166
  End this invocation with isinstance(e, TruncatedResponseError).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:169-173
// Source signature: _reachable_despite_token_cap(err_msg: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reachable_despite_token_cap(err_msg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:170-172
  In source order: Retain source documentation literal source_literal_170_4; it is not a model call. Then Evaluate once (err_msg or '').lower(); assign in source target order to low.
  // Source: vvaharness/orchestrator/preflight.py:173-173
  End this invocation with 'exceeded' in low and 'output token' in low.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:176-179
// Source signature: _post_scan_only(roles: Iterable[str]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _post_scan_only(roles) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:177-177
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:179-179
  End this invocation with bool(roles) and set(roles) <= POST_SCAN_ROLES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:182-193
// Source signature: _report_credential_gap(message: str, roles: Iterable[str], *remedies: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _report_credential_gap(message, roles, remedies) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:183-183
  In source order: Retain source documentation literal source_literal_183_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:185-189
  if (the source predicate _post_scan_only(roles) is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:186-188
    In source order: Evaluate log.warning(Event.PREFLIGHT_CREDENTIAL_GAP, detail=message, roles=sorted(roles)); retain side effects and discard the expression result. Then Evaluate console.write(source_template_187_22); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/preflight.py:189-189
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/preflight.py:190-190
  In source order: Evaluate log.error(Event.PREFLIGHT_CREDENTIAL_GAP, detail=message); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/preflight.py:191-192
  for each line in remedies {
    // Source: vvaharness/orchestrator/preflight.py:192-192
    In source order: Evaluate console.write(source_template_192_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:193-193
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:196-202
In source order: For _HARD_TURN_CAP_VIAS, assign frozenset({'sdk', 'cli', 'openai'}); source annotation frozenset[str]. Then For _TURN_CAPPED_STAGES, assign (('step2', 'threatmodel'), ('step4', 'deepdive'), ('step6_verify', 'verify')); source annotation tuple[tuple[str, str], ...]. Then For _STARVED_TURN_CEILING, assign 20; source annotation int.
// Source: vvaharness/orchestrator/preflight.py:205-224
// Source signature: _warn_deepagents_tuned_max_turns(cfg) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _warn_deepagents_tuned_max_turns(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:206-206
  In source order: Retain source documentation literal source_literal_206_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:207-224
  for each (stage_key, role) in _TURN_CAPPED_STAGES {
    // Source: vvaharness/orchestrator/preflight.py:208-210
    In source order: Evaluate once getattr(cfg, stage_key, None); assign in source target order to block. Then Evaluate once getattr(getattr(cfg, 'models', None), role, None); assign in source target order to model. Then Evaluate once getattr(block, 'max_turns', None); assign in source target order to turns.
    // Source: vvaharness/orchestrator/preflight.py:211-212
    if (the source predicate block is None or model is None or (not isinstance(turns, int)) or (turns <= 0) is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:212-212
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:213-213
    In source order: Evaluate once resolve_model(model).via; assign in source target order to via.
    // Source: vvaharness/orchestrator/preflight.py:214-215
    if (the source predicate via not in _HARD_TURN_CAP_VIAS or turns > _STARVED_TURN_CEILING is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:215-215
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:216-224
    In source order: Evaluate log.warning(Event.PREFLIGHT_MAX_TURNS_HARD_CAPPED, stage=stage_key, role=role, via=via, max_turns=turns, detail=source_template_218_28, remedy=source_template_223_28); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:227-403
// Source signature: check_backends(cfg, *, skip_roles: Iterable[str]=()) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn check_backends(cfg, skip_roles) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:228-235
  In source order: Retain source documentation literal source_literal_228_4; it is not a model call. Then Evaluate once set(skip_roles); assign in source target order to skip. Then Evaluate once [(r, m) for r, m in _iter_model_roles(cfg) if r not in skip]; assign in source target order to model_roles. Then Evaluate once {resolve_model(m).via for _, m in model_roles}; assign in source target order to vias. Then Evaluate once getattr(getattr(cfg, 'models', None), 'deepdive', None); assign in source target order to deepdive_model.
  // Source: vvaharness/orchestrator/preflight.py:236-246
  if (the source predicate deepdive_model is not None is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:237-242
    In source order: Evaluate once resolve_model(deepdive_model).via; assign in source target order to deepdive_via. Then Resolve source import from vvaharness.backends.llm import deepagents as _da_routes; preserve alias and import-time effects. Then Evaluate once _da_routes.route_carries_tools(cfg, deepdive_via); assign in source target order to (carries, why).
    // Source: vvaharness/orchestrator/preflight.py:243-246
    if (the source predicate not carries is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:244-245
      In source order: Evaluate log.error(Event.PREFLIGHT_DEEPDIVE_ROUTE_TOOLLESS, via=deepdive_via, reason=why, remedy='route models.deepdive via deepagents/sdk/openai, or via cli with cli.mcp_tools on and the Claude Agent SDK installed'); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/preflight.py:246-246
      End this invocation with False.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:248-248
  In source order: For roles_by_via, assign {}; source annotation dict[str, set[str]].
  // Source: vvaharness/orchestrator/preflight.py:249-250
  for each (_role, _model) in model_roles {
    // Source: vvaharness/orchestrator/preflight.py:250-250
    In source order: Evaluate roles_by_via.setdefault(resolve_model(_model).via, set()).add(_role); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:253-257
  In source order: Evaluate once [source_template_254_8 for role, model in model_roles for key in unrecognized_model_keys(model)]; assign in source target order to unknown_keys.
  // Source: vvaharness/orchestrator/preflight.py:258-259
  if (the source predicate unknown_keys is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:259-259
    In source order: Evaluate log.warning(Event.MODEL_KEY_UNRECOGNIZED, keys=unknown_keys); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:261-268
  In source order: Evaluate _warn_deepagents_tuned_max_turns(cfg); retain side effects and discard the expression result. Then Evaluate console.write(source_template_263_18); retain side effects and discard the expression result. Then Resolve source import from vvaharness.util.environment import WARN as _WARN; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.environment import langsmith_tracing_check; preserve alias and import-time effects. Then Evaluate once langsmith_tracing_check(); assign in source target order to _tracing.
  // Source: vvaharness/orchestrator/preflight.py:269-270
  if (the source predicate _tracing.status == _WARN is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:270-270
    In source order: Evaluate log.warning(Event.TRACING_UPLOADS_PROMPTS, detail=_tracing.detail); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:273-282
  if (the source predicate 'cli' in vias is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:274-274
    In source order: Evaluate console.write('  [auth] cli: delegated to configured CLI; live probe verifies login'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/preflight.py:275-279
    if (the source predicate os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('ANTHROPIC_AUTH_TOKEN') is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:276-279
      In source order: Evaluate console.write(source_literal_276_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/preflight.py:280-282
    if (the source predicate os.environ.get('CLAUDE_CODE_OAUTH_TOKEN') is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:281-282
      In source order: Evaluate console.mark('ok', 'CLAUDE_CODE_OAUTH_TOKEN present for unattended CLI auth', indent=4); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:285-293
  if (the source predicate 'sdk' in vias is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:286-293
    In source order: Evaluate once getattr(cfg, 'sdk', None); assign in source target order to sdk_cfg. Then Evaluate console.write('  [auth] sdk credential sources (presence only — secrets never printed):'); retain side effects and discard the expression result. Then Evaluate console.write(source_template_288_22); retain side effects and discard the expression result. Then Evaluate console.write(source_template_290_22); retain side effects and discard the expression result. Then Evaluate console.write(source_template_292_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:295-304
  if (the source predicate 'openai' in vias is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:296-304
    In source order: Evaluate once getattr(cfg, 'openai', None); assign in source target order to openai_cfg. Then Evaluate console.write('  [auth] openai credential sources (presence only — secrets never printed):'); retain side effects and discard the expression result. Then Evaluate console.write(source_template_299_22); retain side effects and discard the expression result. Then Evaluate console.write(source_template_301_22); retain side effects and discard the expression result. Then Evaluate console.write(source_template_303_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:306-310
  In source order: Evaluate once True; assign in source target order to ok. Then Evaluate once sorted((role for role, model in model_roles if resolve_model(model).via == 'deepagents' and role not in DEEPAGENTS_ROLES)); assign in source target order to invalid_deepagents.
  // Source: vvaharness/orchestrator/preflight.py:311-316
  if (the source predicate invalid_deepagents is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:313-316
    In source order: Evaluate once ', '.join((source_template_313_30 for r in sorted(DEEPAGENTS_ROLES))); assign in source target order to supported. Then Evaluate log.error(Event.PREFLIGHT_ROUTE_UNSUPPORTED, route='deepagents', supported=supported, invalid=sorted(invalid_deepagents)); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to ok.
  }
  // Source: vvaharness/orchestrator/preflight.py:317-325
  if (the source predicate 'cli' in vias is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:318-325
    if (the source predicate not (shutil.which('claude') or shutil.which('claude.cmd')) is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:319-323
      if (the source predicate _report_credential_gap('`claude` CLI not found on PATH (required by via:cli roles).', roles_by_via['cli'], 'Install: https://docs.anthropic.com/en/docs/claude-code') is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:323-323
        In source order: Evaluate once False; assign in source target order to ok.
      }
    }
    else {
      // Source: vvaharness/orchestrator/preflight.py:325-325
      In source order: Evaluate console.mark('ok', '[cli] claude found on PATH'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:327-351
  if (the source predicate 'sdk' in vias is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:328-332
    In source order: Evaluate once getattr(getattr(cfg, 'sdk', None), 'api_key', None) or os.environ.get('ANTHROPIC_SDK_API_KEY'); assign in source target order to key. Then Evaluate once vias <= {'sdk', 'deepagents'}; assign in source target order to sdk_sole. Then Evaluate once False; assign in source target order to used_fallback.
    // Source: vvaharness/orchestrator/preflight.py:333-336
    if (the source predicate not key and sdk_sole is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:334-336
      In source order: Evaluate once os.environ.get('ANTHROPIC_API_KEY') or os.environ.get('ANTHROPIC_AUTH_TOKEN'); assign in source target order to key. Then Evaluate once bool(key); assign in source target order to used_fallback.
    }
    // Source: vvaharness/orchestrator/preflight.py:337-351
    if (the source predicate not key is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:338-338
      In source order: Evaluate once ['export ANTHROPIC_SDK_API_KEY=sk-ant-...']; assign in source target order to remedies.
      // Source: vvaharness/orchestrator/preflight.py:339-341
      if (the source predicate sdk_sole is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:340-341
        In source order: Evaluate remedies.append('(or set ANTHROPIC_API_KEY — accepted as a fallback because no via:cli role shares this run)'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/orchestrator/preflight.py:342-345
      if (the source predicate _report_credential_gap('ANTHROPIC_SDK_API_KEY not set (required by via:sdk roles).', roles_by_via['sdk'], *remedies) is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:345-345
        In source order: Evaluate once False; assign in source target order to ok.
      }
    }
    else {
      // Source: vvaharness/orchestrator/preflight.py:346-351
      if (the source predicate used_fallback is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:347-349
        In source order: Evaluate console.mark('ok', source_literal_347_31); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/preflight.py:351-351
        In source order: Evaluate console.mark('ok', '[sdk] ANTHROPIC_SDK_API_KEY present'); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:353-362
  if (the source predicate 'openai' in vias is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:354-355
    In source order: Evaluate once getattr(getattr(cfg, 'openai', None), 'api_key', None) or os.environ.get('OPENAI_API_KEY'); assign in source target order to key.
    // Source: vvaharness/orchestrator/preflight.py:356-362
    if (the source predicate not key is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:357-360
      if (the source predicate _report_credential_gap('OPENAI_API_KEY not set (required by via:openai roles).', roles_by_via['openai'], 'export OPENAI_API_KEY=sk-...') is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:360-360
        In source order: Evaluate once False; assign in source target order to ok.
      }
    }
    else {
      // Source: vvaharness/orchestrator/preflight.py:362-362
      In source order: Evaluate console.mark('ok', '[openai] OPENAI_API_KEY present'); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:364-383
  if (the source predicate 'deepagents' in vias is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:365-368
    In source order: Resolve source import from vvaharness.util.environment import _backend_credential_ok; preserve alias and import-time effects. Then For deep_specs, assign {}; source annotation dict[tuple[str, str | None], set[str]].
    // Source: vvaharness/orchestrator/preflight.py:369-373
    for each (role, model) in model_roles {
      // Source: vvaharness/orchestrator/preflight.py:370-371
      if (the source predicate resolve_model(model).via != 'deepagents' is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:371-371
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/preflight.py:372-373
      In source order: Evaluate once (resolve_model(model).model_id, getattr(model, 'provider', None)); assign in source target order to spec. Then Evaluate deep_specs.setdefault(spec, set()).add(role); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/preflight.py:375-383
    for each ((model_id, provider), roles) in sorted(deep_specs.items(), key=lambda kv: (kv[0][0], kv[0][1] or '')) {
      // Source: vvaharness/orchestrator/preflight.py:378-379
      In source order: Evaluate once _backend_credential_ok('deepagents', model_id, provider, cfg=cfg); assign in source target order to (ready, detail).
      // Source: vvaharness/orchestrator/preflight.py:380-383
      if (the source predicate ready is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:381-381
        In source order: Evaluate console.mark('ok', source_template_381_35); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/preflight.py:382-383
        if (the source predicate _report_credential_gap(source_template_382_40, roles) is truthy) {
          // Source: vvaharness/orchestrator/preflight.py:383-383
          In source order: Evaluate once False; assign in source target order to ok.
        }
      }
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:386-388
  if (the source predicate not ok is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:387-387
    In source order: Evaluate console.write('  [probe] skipped — fix credential errors above first'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/preflight.py:388-388
    End this invocation with ok.
  }
  // Source: vvaharness/orchestrator/preflight.py:390-395
  In source order: Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects. Then Evaluate once vias & {'sdk', 'cli'} or any((routes_to_anthropic(resolve_model(model).model_id, getattr(model, 'provider', None)) for _role, model in model_roles if resolve_model(model).via == 'deepagents')); assign in source target order to anthropic_route.
  // Source: vvaharness/orchestrator/preflight.py:396-402
  if (the source predicate anthropic_route is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:397-399
    In source order: Resolve source import from vvaharness.util.environment import FAIL as _FAIL; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.environment import _gateway_check; preserve alias and import-time effects. Then Evaluate once _gateway_check(); assign in source target order to gw.
    // Source: vvaharness/orchestrator/preflight.py:400-402
    if (the source predicate gw.status == _FAIL is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:401-401
      In source order: Evaluate log.error(Event.PREFLIGHT_GATEWAY_UNUSABLE, detail=gw.detail); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/preflight.py:402-402
      End this invocation with False.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:403-403
  End this invocation with probe_backends(cfg, skip_roles=skip).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:407-407
In source order: Evaluate once ('preprocess', 'verify', 'threatmodel'); assign in source target order to _AGENTIC_ROLES.
// Source: vvaharness/orchestrator/preflight.py:410-412
// Source signature: _agentic_roles(cfg) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _agentic_roles(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:411-411
  In source order: Retain source documentation literal source_literal_411_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:412-412
  End this invocation with _AGENTIC_ROLES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:415-429
// Source signature: _agentic_role_tools(cfg, role: str, via: str | None=None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _agentic_role_tools(cfg, role, via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:416-416
  In source order: Retain source documentation literal source_literal_416_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:417-420
  if (the source predicate role == 'preprocess' is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:418-420
    End this invocation with validate_detection_tools(getattr(getattr(cfg, 'step1', None), 'allowed_tools', None), config_key='step1.allowed_tools', via=via).
  }
  // Source: vvaharness/orchestrator/preflight.py:421-424
  if (the source predicate role == 'verify' is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:422-424
    End this invocation with validate_detection_tools(getattr(getattr(cfg, 'step6_verify', None), 'allowed_tools', None), config_key='step6_verify.allowed_tools', via=via).
  }
  // Source: vvaharness/orchestrator/preflight.py:425-428
  if (the source predicate role == 'threatmodel' is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:426-428
    End this invocation with validate_detection_tools(getattr(getattr(cfg, 'step2', None), 'allowed_tools', None), config_key='step2.allowed_tools', via=via).
  }
  // Source: vvaharness/orchestrator/preflight.py:429-429
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:433-440
In source order: Evaluate once 1; assign in source target order to _PROBE_PING_MIN_CHARS. Then Evaluate once 1; assign in source target order to _PROBE_PING_MIN_TOKENS. Then Evaluate once 256; assign in source target order to _PROBE_PING_MAX_TOKENS. Then Evaluate once 120; assign in source target order to _PROBE_PING_TIMEOUT_S. Then Evaluate once 300; assign in source target order to _PROBE_AGENTIC_TIMEOUT_S.
// Source: vvaharness/orchestrator/preflight.py:444-448
In source order: Evaluate once 2; assign in source target order to _PROBE_ROUNDTRIP_TURNS. Then Evaluate once 'vva_preflight_probe_marker.txt'; assign in source target order to _PROBE_MARKER_FILENAME. Then Evaluate once 'PreflightProbeEcho'; assign in source target order to _PROBE_BRIDGE_TOOL_NAME.
// Source: vvaharness/orchestrator/preflight.py:451-454
// Source signature: _probe_roundtrip_nonce() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_roundtrip_nonce() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:452-453
  In source order: Retain source documentation literal source_literal_452_4; it is not a model call. Then Resolve source import import secrets; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/preflight.py:454-454
  End this invocation with secrets.token_hex(8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:457-461
// Source signature: _write_probe_marker(workdir: str, nonce: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _write_probe_marker(workdir, nonce) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:458-460
  In source order: Retain source documentation literal source_literal_458_4; it is not a model call. Then Evaluate once Path(workdir) / _PROBE_MARKER_FILENAME; assign in source target order to path. Then Evaluate path.write_text(nonce, encoding='utf-8'); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/preflight.py:461-461
  End this invocation with _PROBE_MARKER_FILENAME.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:464-469
// Source signature: _native_roundtrip_prompt(marker_name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _native_roundtrip_prompt(marker_name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:465-465
  In source order: Retain source documentation literal source_literal_465_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:466-469
  End this invocation with source_template_467_8.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:472-476
// Source signature: _cli_bridge_enabled(cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cli_bridge_enabled(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:473-475
  In source order: Retain source documentation literal source_literal_473_4; it is not a model call. Then Resolve source import from vvaharness.backends.llm.deepagents import route_carries_tools; preserve alias and import-time effects. Then Evaluate once route_carries_tools(cfg, 'cli'); assign in source target order to (carries, _reason).
  // Source: vvaharness/orchestrator/preflight.py:476-476
  End this invocation with carries.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:479-482
// Source signature: _reachable_despite_tool_dispatch_error(e: BaseException) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reachable_despite_tool_dispatch_error(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:480-480
  In source order: Retain source documentation literal source_literal_480_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:482-482
  End this invocation with isinstance(e, (HarnessJSONDecodeError, HarnessMessageParseError)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:486-487
In source order: Evaluate once re.compile('^Could not process the query for model \\S+\\. Error: Error code: \\d+ - ?'); assign in source target order to _GATEWAY_WRAPPER_RX.
// Source: vvaharness/orchestrator/preflight.py:490-509
// Source signature: _upstream_message(e: BaseException) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _upstream_message(e) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:491-503
  In source order: Retain source documentation literal source_literal_491_4; it is not a model call. Then Evaluate once next((lk for lk in exception_chain(e) if getattr(lk, 'status_code', None) is not None), e); assign in source target order to link. Then Evaluate once getattr(link, 'body', None); assign in source target order to raw_body. Then Evaluate once raw_body if isinstance(raw_body, str) and raw_body else rejection_text(link); assign in source target order to body. Then Evaluate once _GATEWAY_WRAPPER_RX.sub('', body); assign in source target order to body.
  // Source: vvaharness/orchestrator/preflight.py:504-505
  In source order: Evaluate once body.splitlines(); assign in source target order to lines. Then Evaluate once (lines[0] if lines else '').strip() or '(no message)'; assign in source target order to upstream.
  // Source: vvaharness/orchestrator/preflight.py:506-507
  if (the source predicate link is e is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:507-507
    End this invocation with upstream.
  }
  // Source: vvaharness/orchestrator/preflight.py:508-508
  In source order: Evaluate once ' '.join(str(e).split()); assign in source target order to wrapper.
  // Source: vvaharness/orchestrator/preflight.py:509-509
  End this invocation with upstream if not wrapper or wrapper == upstream else source_template_509_63.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:512-617
// Source signature: _probe_agentic_roles(cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_agentic_roles(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:513-519
  In source order: Retain source documentation literal source_literal_513_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.models import ToolStateNotRoundTrippedError; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm import deepagents as _deepagents; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.registry import agentic as _probe_agentic; preserve alias and import-time effects. Then For targets, assign {}; source annotation dict[tuple, tuple].
  // Source: vvaharness/orchestrator/preflight.py:520-521
  In source order: Evaluate once _agentic_roles(cfg); assign in source target order to agentic_roles. Then Evaluate once True; assign in source target order to ok.
  // Source: vvaharness/orchestrator/preflight.py:522-540
  for each (role, m) in _iter_model_roles(cfg) {
    // Source: vvaharness/orchestrator/preflight.py:523-524
    if (the source predicate role not in agentic_roles is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:524-524
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:525-525
    In source order: Evaluate once resolve_model(m); assign in source target order to (mid, via, _).
    // Source: vvaharness/orchestrator/preflight.py:526-532
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/preflight.py:527-527
      In source order: Evaluate once _agentic_role_tools(cfg, role, via); assign in source target order to tools.
    }
    // Source: vvaharness/orchestrator/preflight.py:528-532
    On the first matching source exception ValueError as e, in handler order {
      // Source: vvaharness/orchestrator/preflight.py:530-531
      if (the source predicate _report_credential_gap(str(e), {role}) is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:531-531
        In source order: Evaluate once False; assign in source target order to ok.
      }
      // Source: vvaharness/orchestrator/preflight.py:532-532
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:533-537
    if (the source predicate not tools is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:535-536
      In source order: Evaluate console.write(source_template_535_26); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/preflight.py:537-537
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:538-540
    In source order: Evaluate once (mid, via, getattr(m, 'provider', None), frozenset(tools)); assign in source target order to key. Then Evaluate once targets.setdefault(key, (m, tools, [])); assign in source target order to (_node, _t, roles). Then Evaluate roles.append(role); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:542-543
  if (the source predicate not targets is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:543-543
    End this invocation with ok.
  }
  // Source: vvaharness/orchestrator/preflight.py:545-546
  In source order: Evaluate console.write(source_template_545_18); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/preflight.py:547-616
  for each ((mid, via, _provider, _tk), (mcfg, tools, roles)) in targets.items() {
    // Source: vvaharness/orchestrator/preflight.py:548-552
    In source order: Evaluate once ','.join(roles); assign in source target order to role_list. Then Evaluate once highest_effort((role_effort(cfg, r) for r in roles)); assign in source target order to effort. Then Evaluate once time.time(); assign in source target order to t0. Then Evaluate once tempfile.mkdtemp(prefix='vva-preflight-'); assign in source target order to workdir. Then Evaluate once set(roles); assign in source target order to roles_set.
    // Source: vvaharness/orchestrator/preflight.py:553-616
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/preflight.py:554-556
      In source order: Evaluate once _probe_roundtrip_nonce(); assign in source target order to nonce. Then Evaluate once _write_probe_marker(workdir, nonce); assign in source target order to marker_name. Then Evaluate once _native_roundtrip_prompt(marker_name); assign in source target order to prompt.
      // Source: vvaharness/orchestrator/preflight.py:558-586
      Enter source context managers left-to-right: stage_floors('preflight-agentic', min_chars=_PROBE_PING_MIN_CHARS, min_tokens=_PROBE_PING_MIN_TOKENS) {
        // Source: vvaharness/orchestrator/preflight.py:561-586
        if (the source predicate via == 'deepagents' is truthy) {
          // Source: vvaharness/orchestrator/preflight.py:562-571
          In source order: Evaluate once _deepagents.agentic(prompt, model=mcfg, system_prompt=None, allowed_tools=list(tools), cwd=workdir, max_turns=_PROBE_ROUNDTRIP_TURNS, tag='preflight-agentic', graph_name='preflight-agentic', sdk_cfg=getattr(cfg, 'sdk', None), openai_cfg=getattr(cfg, 'openai', None), timeout=_PROBE_AGENTIC_TIMEOUT_S, effort=effort, think_in_prompt=_deepagents.think_in_prompt_enabled(cfg)); assign in source target order to reply.
        }
        else {
          // Source: vvaharness/orchestrator/preflight.py:574-581
          In source order: Evaluate once _probe_agentic(prompt, model=mcfg, system_prompt=None, allowed_tools=list(tools), cwd=workdir, max_turns=_PROBE_ROUNDTRIP_TURNS, tag='preflight-agentic', timeout=_PROBE_AGENTIC_TIMEOUT_S, **{'effort': effort} if via != 'cli' else {}); assign in source target order to reply.
          // Source: vvaharness/orchestrator/preflight.py:582-586
          if (the source predicate via == 'cli' and _cli_bridge_enabled(cfg) is truthy) {
            // Source: vvaharness/orchestrator/preflight.py:584-586
            In source order: Evaluate _probe_agentic_via_cli_bridge(prompt, nonce=nonce, model=mid, allowed_tools=tools, cwd=workdir); retain side effects and discard the expression result.
          }
        }
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/preflight.py:587-594
      In source order: Evaluate once nonce in (reply or ''); assign in source target order to confirmed. Then Evaluate console.mark('ok' if confirmed else 'warn', '  '.join((via, mid, source_template_591_37, role_list, '' if confirmed else 'round-trip unconfirmed (reply never echoed the marker) — tool state was reachable but not proven round-tripped'))); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/preflight.py:595-614
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/orchestrator/preflight.py:596-600
      if (the source predicate isinstance(e, ToolStateNotRoundTrippedError) is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:598-599
        if (the source predicate _report_credential_gap(str(e), roles_set) is truthy) {
          // Source: vvaharness/orchestrator/preflight.py:599-599
          In source order: Evaluate once False; assign in source target order to ok.
        }
        // Source: vvaharness/orchestrator/preflight.py:600-600
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/preflight.py:601-609
      if (the source predicate _reachable_despite_token_cap(str(e)) or _reachable_despite_degenerate_reply(e) or _reachable_despite_truncated_reply(e) or _reachable_despite_tool_dispatch_error(e) is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:605-608
        In source order: Evaluate once 'reachable; terse, token-capped, or tool-mechanics reply'; assign in source target order to note. Then Evaluate console.mark('ok', '  '.join((via, mid, source_template_608_31, role_list, note))); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/preflight.py:609-609
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/preflight.py:610-614
      In source order: Evaluate once source_template_610_19; assign in source target order to note. Then Evaluate console.mark('fail', '  '.join((via, mid, source_template_611_54, role_list, note))); retain side effects and discard the expression result. Then Evaluate log.error(Event.PREFLIGHT_PROBE_FAILED, model=mid, route=via, effort=effort, cause=_upstream_message(e)); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to ok.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/orchestrator/preflight.py:616-616
      In source order: Evaluate shutil.rmtree(workdir, ignore_errors=True); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:617-617
  End this invocation with ok.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:620-661
// Source signature: _probe_agentic_via_cli_bridge(prompt: str, *, nonce: str, model: str, allowed_tools: list[str], cwd: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_agentic_via_cli_bridge(prompt, nonce, model, allowed_tools, cwd) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:623-627
  In source order: Retain source documentation literal source_literal_623_4; it is not a model call. Then Resolve source import from langchain_core.tools import tool as _lc_tool; preserve alias and import-time effects. Then Resolve source import from vvaharness.pipeline.stages.replay import start_daemon; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/preflight.py:630-632
  // Source: vvaharness/orchestrator/preflight.py:629-629
  Before creating this callable, evaluate and retain decorators top-to-bottom: _lc_tool(_PROBE_BRIDGE_TOOL_NAME).
  // Source: vvaharness/orchestrator/preflight.py:630-632
  // Source signature: _echo(marker: str) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _echo(marker) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/preflight.py:631-631
    In source order: Retain source documentation literal source_literal_631_8; it is not a model call.
    // Source: vvaharness/orchestrator/preflight.py:632-632
    End this invocation with marker.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/orchestrator/preflight.py:634-635
  // Source signature: _tool_builder(_options, allowed_tools=())
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _tool_builder(_options, allowed_tools) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/preflight.py:635-635
    End this invocation with [_echo].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/preflight.py:637-637
  In source order: Resolve source import from vvaharness.backends.llm import cli_mcp; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/preflight.py:639-646
  // Source signature: _call() -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _call() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/preflight.py:640-646
    End this invocation with cli_mcp.agentic_with_tools(source_template_641_12, model=model, system_prompt=None, allowed_tools=allowed_tools, cwd=cwd, tool_builder=_tool_builder, fact_tools=(_PROBE_BRIDGE_TOOL_NAME,), max_turns=_PROBE_ROUNDTRIP_TURNS, tag='preflight-agentic').
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/preflight.py:649-649
  In source order: Evaluate once start_daemon(_call, 'preflight-bridge-probe'); assign in source target order to future.
  // Source: vvaharness/orchestrator/preflight.py:650-661
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/preflight.py:651-651
    End this invocation with future.result(timeout=_PROBE_AGENTIC_TIMEOUT_S).
  }
  // Source: vvaharness/orchestrator/preflight.py:652-661
  On the first matching source exception TimeoutError as exc, in handler order {
    // Source: vvaharness/orchestrator/preflight.py:655-656
    if (the source predicate future.done() is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:656-656
      End this invocation with future.result().
    }
    // Source: vvaharness/orchestrator/preflight.py:657-657
    In source order: Evaluate future.cancel(); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/preflight.py:658-661
    Raise TimeoutError(source_template_659_12) with explicit source cause exc.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:664-677
// Source signature: _probe_targets(cfg, *, skip_roles: Iterable[str]=()) -> dict[tuple[str, str, str | None], tuple[object, list[str]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_targets(cfg, skip_roles) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:666-669
  In source order: Retain source documentation literal source_literal_666_4; it is not a model call. Then Evaluate once set(skip_roles); assign in source target order to skip. Then For targets, assign {}; source annotation dict[tuple[str, str, str | None], tuple[object, list[str]]].
  // Source: vvaharness/orchestrator/preflight.py:670-676
  for each (role, m) in _iter_model_roles(cfg) {
    // Source: vvaharness/orchestrator/preflight.py:671-672
    if (the source predicate role in skip is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:672-672
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:673-676
    In source order: Evaluate once resolve_model(m); assign in source target order to (mid, via, _). Then Evaluate once (mid, via, getattr(m, 'provider', None)); assign in source target order to key. Then Evaluate once targets.setdefault(key, (m, [])); assign in source target order to (_node, roles). Then Evaluate roles.append(role); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:677-677
  End this invocation with targets.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:680-737
// Source signature: _probe_deepagents_harness(cfg, model_id: str, provider: str | None, *, include_tls: bool=True, use_responses_api: bool | None=None, effort: str | None=None) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_deepagents_harness(cfg, model_id, provider, include_tls, use_responses_api, effort) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:684-697
  In source order: Retain source documentation literal source_literal_684_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness import OneShotOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import credential_env_overrides; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.deepagents import build_harness_env, markers_on, run_oneshot, think_in_prompt_enabled; preserve alias and import-time effects. Then Evaluate once getattr(cfg, 'sdk', None); assign in source target order to sdk_cfg.
  // Source: vvaharness/orchestrator/preflight.py:698-698
  In source order: Evaluate once getattr(cfg, 'openai', None); assign in source target order to openai_cfg.
  // Source: vvaharness/orchestrator/preflight.py:699-711
  if (the source predicate include_tls is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:700-703
    In source order: Evaluate once build_harness_env(model_id, provider, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg, cfg_dir=getattr(cfg, '_data', {}).get('_config_dir')); assign in source target order to env.
  }
  else {
    // Source: vvaharness/orchestrator/preflight.py:706-711
    In source order: Evaluate once {**os.environ, **credential_env_overrides(model_id, provider, sdk_cfg=sdk_cfg, openai_cfg=openai_cfg)}; assign in source target order to env.
  }
  // Source: vvaharness/orchestrator/preflight.py:712-734
  Enter source context managers left-to-right: tempfile.TemporaryDirectory(prefix='vva-preflight-deepagents-') bound to workdir {
    // Source: vvaharness/orchestrator/preflight.py:715-734
    In source order: Evaluate once run_oneshot('reply with the single word ok', OneShotOptions(model=model_id, cwd=Path(workdir), env=env, model_provider=provider, use_responses_api=use_responses_api, max_turns=2, graph_name='preflight', cache_markers=markers_on(sdk_cfg), effort=effort, think_in_prompt=think_in_prompt_enabled(cfg)), tag='preflight', timeout=effort_scaled_seconds(_PROBE_PING_TIMEOUT_S, effort, kind=ClockKind.REQUEST)); assign in source target order to result.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/orchestrator/preflight.py:735-737
  if (the source predicate result.is_error is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:736-737
    Raise RuntimeError(source_template_737_12).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:740-820
// Source signature: probe_backends(cfg, *, skip_roles: Iterable[str]=()) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn probe_backends(cfg, skip_roles) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:741-748
  In source order: Retain source documentation literal source_literal_741_4; it is not a model call. Then Resolve source import from vvaharness.backends.llm.registry import prompt as _probe; preserve alias and import-time effects. Then Evaluate once set(skip_roles); assign in source target order to skip. Then Evaluate once sorted((role for role, model in _iter_model_roles(cfg) if role not in skip and resolve_model(model).via == 'deepagents' and (role not in DEEPAGENTS_ROLES))); assign in source target order to invalid_deepagents.
  // Source: vvaharness/orchestrator/preflight.py:749-756
  if (the source predicate invalid_deepagents is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:751-755
    In source order: Evaluate console.write('ERROR: refusing DeepAgents probe for unsupported role(s): ' + ', '.join(invalid_deepagents) + source_template_754_14); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/preflight.py:756-756
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/preflight.py:757-763
  In source order: Evaluate once _probe_targets(cfg, skip_roles=skip); assign in source target order to targets. Then Evaluate console.write(source_template_759_18); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to ok. Then For skipped, assign set(); source annotation set[str].
  // Source: vvaharness/orchestrator/preflight.py:764-807
  for each ((mid, via, provider), (mcfg, roles)) in targets.items() {
    // Source: vvaharness/orchestrator/preflight.py:765-767
    In source order: Evaluate once ','.join(roles); assign in source target order to role_list. Then Evaluate once highest_effort((role_effort(cfg, r) for r in roles)); assign in source target order to effort. Then Evaluate once time.time(); assign in source target order to t0.
    // Source: vvaharness/orchestrator/preflight.py:768-807
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/preflight.py:769-785
      if (the source predicate via == 'deepagents' is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:771-775
        In source order: Evaluate _probe_deepagents_harness(cfg, mid, provider, include_tls=not _post_scan_only(roles), use_responses_api=use_responses_api_of(mcfg), effort=effort); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/preflight.py:778-785
        Enter source context managers left-to-right: stage_floors('preflight', min_chars=_PROBE_PING_MIN_CHARS, min_tokens=_PROBE_PING_MIN_TOKENS) {
          // Source: vvaharness/orchestrator/preflight.py:781-785
          In source order: Evaluate _probe('ping', model=mcfg, max_tokens=_PROBE_PING_MAX_TOKENS, timeout=_PROBE_PING_TIMEOUT_S, tag='preflight', **{'effort': effort} if via != 'cli' else {}); retain side effects and discard the expression result.
        }
        Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      }
      // Source: vvaharness/orchestrator/preflight.py:786-786
      In source order: Evaluate console.mark('ok', '  '.join((via, mid, source_template_786_52, role_list, ''))); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/preflight.py:787-807
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/orchestrator/preflight.py:788-793
      if (the source predicate _reachable_despite_token_cap(str(e)) or _reachable_despite_degenerate_reply(e) or _reachable_despite_truncated_reply(e) is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:791-792
        In source order: Evaluate console.mark('ok', '  '.join((via, mid, source_template_791_56, role_list, 'reachable; terse or token-capped reply'))); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/preflight.py:793-793
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/preflight.py:795-802
      if (the source predicate _post_scan_only(roles) is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:796-801
        In source order: Evaluate once source_template_796_23; assign in source target order to note. Then Evaluate console.mark('warn', '  '.join((via, mid, source_template_797_58, role_list, note))); retain side effects and discard the expression result. Then Evaluate log.warning(Event.PREFLIGHT_PROBE_FAILED, model=mid, route=via, effort=effort, cause=_upstream_message(e)); retain side effects and discard the expression result. Then Evaluate skipped.update(roles); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/preflight.py:802-802
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/preflight.py:803-807
      In source order: Evaluate once source_template_803_19; assign in source target order to note. Then Evaluate console.mark('fail', '  '.join((via, mid, source_template_804_54, role_list, note))); retain side effects and discard the expression result. Then Evaluate log.error(Event.PREFLIGHT_PROBE_FAILED, model=mid, route=via, effort=effort, cause=_upstream_message(e)); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to ok.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:810-810
  In source order: Evaluate once _probe_agentic_roles(cfg) and ok; assign in source target order to ok.
  // Source: vvaharness/orchestrator/preflight.py:812-819
  if (the source predicate ok and skipped is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:813-815
    In source order: Evaluate console.mark('ok', source_template_813_27); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/orchestrator/preflight.py:816-819
    if (the source predicate ok is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:817-817
      In source order: Evaluate console.mark('ok', '[probe] all model backends reachable'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/orchestrator/preflight.py:819-819
      In source order: Evaluate log.error(Event.PREFLIGHT_BACKENDS_UNREACHABLE); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:820-820
  End this invocation with ok.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:826-833
In source order: Evaluate once frozenset({'sdk', 'openai', 'cli'}); assign in source target order to _PROMPT_VIAS. Then Evaluate once 8192; assign in source target order to _FILLER_MIN_TOKENS. Then Evaluate once 4; assign in source target order to _FILLER_CHARS_PER_TOKEN. Then Evaluate once 1.25; assign in source target order to _FILLER_MARGIN. Then Evaluate once 256; assign in source target order to _PROBE_MAX_TOKENS.
// Source: vvaharness/orchestrator/preflight.py:834-849
In source order: Evaluate once 120; assign in source target order to _PROBE_TIMEOUT_S. Then Evaluate once 5.0; assign in source target order to _CALL_B_DEADLINE_S. Then Evaluate once 1024; assign in source target order to _PROBE_THINKING_BUDGET. Then Evaluate once source_literal_841_4; assign in source target order to _USER_MSG_A. Then Evaluate once source_literal_846_4; assign in source target order to _USER_MSG_B.
// Source: vvaharness/orchestrator/preflight.py:852-856
In source order: Evaluate once 'anthropic_works'; assign in source target order to V_ANTHROPIC_WORKS. Then Evaluate once 'anthropic_write_ok_read_fails'; assign in source target order to V_ANTHROPIC_ROUTING_GAP. Then Evaluate once 'anthropic_marker_not_honoured'; assign in source target order to V_ANTHROPIC_NOT_HONOURED. Then Evaluate once 'anthropic_works_prefix_already_cached'; assign in source target order to V_ANTHROPIC_ALREADY_WARM. Then Evaluate once 'openai_implicit_working'; assign in source target order to V_OPENAI_WORKING.
// Source: vvaharness/orchestrator/preflight.py:857-896
In source order: Evaluate once 'openai_below_minimum_or_unstable'; assign in source target order to V_OPENAI_BELOW_MIN. Then Evaluate once 'no_cache_fields_treat_as_implicit'; assign in source target order to V_NO_CACHE_FIELDS. Then Evaluate once 'anthropic_marker_withheld_by_gate'; assign in source target order to V_MARKER_WITHHELD. Then Evaluate once {V_ANTHROPIC_WORKS: 'cache markers are honoured on this route; explicit breakpoints are an optimisation here, not a fix.', V_ANTHROPIC_ROUTING_GAP: 'writes succeed but reads do not — investigate request routing or cache-key affinity, not marker placement.', V_ANTHROPIC_NOT_HONOURED: source_literal_870_8, V_ANTHROPIC_ALREADY_WARM: source_literal_875_8, V_OPENAI_WORKING: 'the implicit prefix cache is working normally; no explicit marker is needed or available on this route.', V_OPENAI_BELOW_MIN: source_literal_882_8, V_NO_CACHE_FIELDS: source_literal_886_8, V_MARKER_WITHHELD: source_literal_890_8}; assign in source target order to _VERDICT_TEXT.
// Source: vvaharness/orchestrator/preflight.py:898-911
// Source signature: cache_probe_filler(min_tokens: int=_FILLER_MIN_TOKENS) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn cache_probe_filler(min_tokens) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:899-904
  In source order: Retain source documentation literal source_literal_899_4; it is not a model call. Then Evaluate once int(min_tokens * _FILLER_CHARS_PER_TOKEN * _FILLER_MARGIN); assign in source target order to target_chars. Then Evaluate once ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sierra', 'tango', 'uniform', 'victor', 'whiskey', 'xray', 'yankee', 'zulu']; assign in source target order to words. Then For lines, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to total.
  // Source: vvaharness/orchestrator/preflight.py:905-905
  In source order: Evaluate once 0; assign in source target order to i.
  // Source: vvaharness/orchestrator/preflight.py:906-910
  while (the source predicate total < target_chars is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:907-910
    In source order: Evaluate once source_template_907_15 + ' '.join(words) + source_template_907_71; assign in source target order to line. Then Evaluate lines.append(line); retain side effects and discard the expression result. Then Apply source augmented assignment total += len(line) with source evaluation/in-place semantics. Then Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/orchestrator/preflight.py:911-911
  End this invocation with ''.join(lines).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:914-932
// Source signature: _scheme_host(url: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scheme_host(url) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:915-915
  In source order: Retain source documentation literal source_literal_915_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:916-917
  if (the source predicate not url is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:917-917
    End this invocation with '(default)'.
  }
  // Source: vvaharness/orchestrator/preflight.py:918-931
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/preflight.py:919-920
    In source order: Evaluate once urlsplit(url); assign in source target order to parts. Then Evaluate once parts.hostname or ''; assign in source target order to host.
    // Source: vvaharness/orchestrator/preflight.py:922-923
    if (the source predicate ':' in host is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:923-923
      In source order: Evaluate once source_template_923_19; assign in source target order to host.
    }
    // Source: vvaharness/orchestrator/preflight.py:924-925
    if (the source predicate parts.port is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:925-925
      In source order: Evaluate once source_template_925_19; assign in source target order to host.
    }
    // Source: vvaharness/orchestrator/preflight.py:926-929
    if (the source predicate parts.scheme and host is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:927-927
      In source order: Evaluate once source_template_927_18; assign in source target order to out.
    }
    else {
      // Source: vvaharness/orchestrator/preflight.py:929-929
      In source order: Evaluate once host or '(unparseable)'; assign in source target order to out.
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:930-931
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/orchestrator/preflight.py:931-931
    In source order: Evaluate once '(unparseable)'; assign in source target order to out.
  }
  // Source: vvaharness/orchestrator/preflight.py:932-932
  End this invocation with redact(out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:935-947
// Source signature: _resolved_base_url_scheme_host(via: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolved_base_url_scheme_host(via) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:936-936
  In source order: Retain source documentation literal source_literal_936_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:938-946
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/preflight.py:939-944
    if (the source predicate via == 'sdk' is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:940-940
      In source order: Evaluate once str(sdk._get_client().base_url); assign in source target order to raw.
    }
    else {
      // Source: vvaharness/orchestrator/preflight.py:941-944
      if (the source predicate via == 'openai' is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:942-942
        In source order: Evaluate once str(oai._get_client().base_url); assign in source target order to raw.
      }
      else {
        // Source: vvaharness/orchestrator/preflight.py:944-944
        End this invocation with '(cli subprocess — no base_url)'.
      }
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:945-946
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/orchestrator/preflight.py:946-946
    End this invocation with '(unresolved)'.
  }
  // Source: vvaharness/orchestrator/preflight.py:947-947
  End this invocation with _scheme_host(raw).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:950-955
// Source signature: _thinking_actually_sent(model_id: str, requested_budget: int | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _thinking_actually_sent(model_id, requested_budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:951-951
  In source order: Retain source documentation literal source_literal_951_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:953-954
  if (the source predicate not requested_budget is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:954-954
    End this invocation with False.
  }
  // Source: vvaharness/orchestrator/preflight.py:955-955
  End this invocation with model_id not in sdk._NO_THINK_MODELS.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:958-971
// Source signature: _marker_would_be_placed(via: str, system_prompt: str, model_id: str) -> bool | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _marker_would_be_placed(via, system_prompt, model_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:960-960
  In source order: Retain source documentation literal source_literal_960_4; it is not a model call.
  // Source: vvaharness/orchestrator/preflight.py:962-963
  if (the source predicate via != 'sdk' is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:963-963
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/preflight.py:964-971
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/preflight.py:965-966
    if (the source predicate not sdk._cache_markers_enabled() is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:966-966
      End this invocation with False.
    }
    // Source: vvaharness/orchestrator/preflight.py:967-968
    if (the source predicate sdk._cache_route(sdk._get_client()) not in sdk._CACHE_CONTROL_ROUTES is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:968-968
      End this invocation with False.
    }
    // Source: vvaharness/orchestrator/preflight.py:969-969
    End this invocation with bool(sdk._cache_prefix_meets_minimum(system_prompt, model_id)).
  }
  // Source: vvaharness/orchestrator/preflight.py:970-971
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/orchestrator/preflight.py:971-971
    End this invocation with None.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:974-985
// Source signature: usage_dict_for_classifier(*, cache_write: int, cache_read: int, write_present: bool, read_present: bool) -> tuple[dict, dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn usage_dict_for_classifier(cache_write, cache_read, write_present, read_present) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:977-980
  In source order: Retain source documentation literal source_literal_977_4; it is not a model call. Then For usage_a, assign {}; source annotation dict. Then For usage_b, assign {}; source annotation dict.
  // Source: vvaharness/orchestrator/preflight.py:981-982
  if (the source predicate write_present is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:982-982
    In source order: Evaluate once cache_write; assign in source target order to usage_a['cache_creation_input_tokens'].
  }
  // Source: vvaharness/orchestrator/preflight.py:983-984
  if (the source predicate read_present is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:984-984
    In source order: Evaluate once cache_read; assign in source target order to usage_b['cache_read_input_tokens'].
  }
  // Source: vvaharness/orchestrator/preflight.py:985-985
  End this invocation with (usage_a, usage_b).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:988-1006
// Source signature: classify_cache_verdict(usage_a: dict, usage_b: dict) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn classify_cache_verdict(usage_a, usage_b) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:989-992
  In source order: Retain source documentation literal source_literal_989_4; it is not a model call. Then Evaluate once 'cache_creation_input_tokens' in usage_a; assign in source target order to creation_present. Then Evaluate once 'cache_read_input_tokens' in usage_b; assign in source target order to read_present.
  // Source: vvaharness/orchestrator/preflight.py:993-994
  if (the source predicate not creation_present and (not read_present) is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:994-994
    End this invocation with V_NO_CACHE_FIELDS.
  }
  // Source: vvaharness/orchestrator/preflight.py:995-995
  In source order: Evaluate once int(usage_b.get('cache_read_input_tokens', 0) or 0); assign in source target order to read.
  // Source: vvaharness/orchestrator/preflight.py:996-1005
  if (the source predicate creation_present is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:997-997
    In source order: Evaluate once int(usage_a.get('cache_creation_input_tokens', 0) or 0); assign in source target order to creation.
    // Source: vvaharness/orchestrator/preflight.py:998-999
    if (the source predicate creation > 0 and read > 0 is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:999-999
      End this invocation with V_ANTHROPIC_WORKS.
    }
    // Source: vvaharness/orchestrator/preflight.py:1000-1001
    if (the source predicate creation > 0 and read == 0 is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:1001-1001
      End this invocation with V_ANTHROPIC_ROUTING_GAP.
    }
    // Source: vvaharness/orchestrator/preflight.py:1002-1004
    if (the source predicate creation == 0 and read > 0 is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:1004-1004
      End this invocation with V_ANTHROPIC_ALREADY_WARM.
    }
    // Source: vvaharness/orchestrator/preflight.py:1005-1005
    End this invocation with V_ANTHROPIC_NOT_HONOURED.
  }
  // Source: vvaharness/orchestrator/preflight.py:1006-1006
  End this invocation with V_OPENAI_WORKING if read > 0 else V_OPENAI_BELOW_MIN.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1009-1012
// Source signature: _deepdive_system_prompt() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deepdive_system_prompt() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1010-1011
  In source order: Retain source documentation literal source_literal_1010_4; it is not a model call. Then Resolve source import from vvaharness.pipeline.stages.s4.prompts import build_system_prompt; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/preflight.py:1012-1012
  End this invocation with build_system_prompt().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1015-1023
// Source signature: _cache_probe_targets(cfg) -> dict[tuple[str, str], object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cache_probe_targets(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1016-1017
  In source order: Retain source documentation literal source_literal_1016_4; it is not a model call. Then For targets, assign {}; source annotation dict[tuple[str, str], object].
  // Source: vvaharness/orchestrator/preflight.py:1018-1022
  for each (_role, m) in _iter_model_roles(cfg) {
    // Source: vvaharness/orchestrator/preflight.py:1019-1019
    In source order: Evaluate once resolve_model(m); assign in source target order to (mid, via, _extras).
    // Source: vvaharness/orchestrator/preflight.py:1020-1021
    if (the source predicate via not in _PROMPT_VIAS is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:1021-1021
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:1022-1022
    In source order: Evaluate targets.setdefault((mid, via), m); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1023-1023
  End this invocation with targets.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1026-1058
// Source signature: _observe_call(phase_label: str, invoke) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _observe_call(phase_label, invoke) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1027-1032
  In source order: Retain source documentation literal source_literal_1027_4; it is not a model call. Then For observed, assign []; source annotation list[dict]. Then Evaluate once object(); assign in source target order to _sentinel. Then Evaluate once TOKENS.__dict__.get('add', _sentinel); assign in source target order to prev_add. Then Evaluate once TOKENS.add; assign in source target order to real_add.
  // Source: vvaharness/orchestrator/preflight.py:1034-1037
  // Source signature: _observing_add(usage, **kw)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _observing_add(usage, kw) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/preflight.py:1035-1036
    if (the source predicate isinstance(usage, dict) and TOKENS.current_phase() == phase_label is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:1036-1036
      In source order: Evaluate observed.append(dict(usage)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/preflight.py:1037-1037
    End this invocation with real_add(usage, **kw).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1039-1049
  Enter source context managers left-to-right: TOKENS.phase(phase_label) {
    // Source: vvaharness/orchestrator/preflight.py:1040-1041
    In source order: Evaluate once dict(TOKENS.snapshot()['by_phase'].get(phase_label, {})); assign in source target order to before. Then Evaluate once _observing_add; assign in source target order to TOKENS.add.
    // Source: vvaharness/orchestrator/preflight.py:1042-1048
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/preflight.py:1043-1043
      In source order: Evaluate invoke(); retain side effects and discard the expression result.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/orchestrator/preflight.py:1045-1048
      if (the source predicate prev_add is _sentinel is truthy) {
        // Source: vvaharness/orchestrator/preflight.py:1046-1046
        In source order: Evaluate TOKENS.__dict__.pop('add', None); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/orchestrator/preflight.py:1048-1048
        In source order: Evaluate once prev_add; assign in source target order to TOKENS.add.
      }
    }
    // Source: vvaharness/orchestrator/preflight.py:1049-1049
    In source order: Evaluate once dict(TOKENS.snapshot()['by_phase'].get(phase_label, {})); assign in source target order to after.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/orchestrator/preflight.py:1050-1058
  End this invocation with {'cache_read': after.get('cache_read', 0) - before.get('cache_read', 0), 'cache_write': after.get('cache_write', 0) - before.get('cache_write', 0), 'cache_read_present': any(('cache_read_input_tokens' in u for u in observed)), 'cache_write_present': any(('cache_creation_input_tokens' in u for u in observed))}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1061-1076
// Source signature: _call_and_diff(*, model, system_prompt: str, user_prompt: str, thinking_budget: int | None, phase_label: str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _call_and_diff(model, system_prompt, user_prompt, thinking_budget, phase_label) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1063-1064
  In source order: Retain source documentation literal source_literal_1063_4; it is not a model call. Then Resolve source import from vvaharness.backends.llm.registry import prompt as _prompt; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/preflight.py:1066-1074
  // Source signature: _invoke()
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _invoke() {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/preflight.py:1068-1074
    Enter source context managers left-to-right: stage_floors('cache-probe', min_chars=_PROBE_PING_MIN_CHARS, min_tokens=_PROBE_PING_MIN_TOKENS) {
      // Source: vvaharness/orchestrator/preflight.py:1071-1074
      In source order: Evaluate _prompt(user_prompt, model=model, system_prompt=system_prompt, thinking_budget=thinking_budget, max_tokens=_PROBE_MAX_TOKENS, timeout=_PROBE_TIMEOUT_S, tag='cache-probe'); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1076-1076
  End this invocation with _observe_call(phase_label, _invoke).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1079-1087
// Source signature: _deepagents_cache_probe_targets(cfg) -> dict[tuple[str, str], object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deepagents_cache_probe_targets(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1080-1081
  In source order: Retain source documentation literal source_literal_1080_4; it is not a model call. Then For targets, assign {}; source annotation dict[tuple[str, str], object].
  // Source: vvaharness/orchestrator/preflight.py:1082-1086
  for each (_role, m) in _iter_model_roles(cfg) {
    // Source: vvaharness/orchestrator/preflight.py:1083-1083
    In source order: Evaluate once resolve_model(m); assign in source target order to (mid, via, _extras).
    // Source: vvaharness/orchestrator/preflight.py:1084-1085
    if (the source predicate via != 'deepagents' is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:1085-1085
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:1086-1086
    In source order: Evaluate targets.setdefault((mid, via), m); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1087-1087
  End this invocation with targets.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1090-1096
// Source signature: _deepagents_marker_would_be_placed(cfg, model_id: str, provider: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deepagents_marker_would_be_placed(cfg, model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1092-1094
  In source order: Retain source documentation literal source_literal_1092_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.deepagents import markers_on; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/preflight.py:1095-1096
  End this invocation with markers_on(getattr(cfg, 'sdk', None)) and routes_to_anthropic(model_id, provider).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1099-1118
// Source signature: _deepagents_base_url(cfg, model_id: str, provider: str | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deepagents_base_url(cfg, model_id, provider) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1100-1106
  In source order: Retain source documentation literal source_literal_1100_4; it is not a model call. Then Resolve source import from vvaharness.backends.harness.deepagents.models import anthropic_base, openai_base; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.llm.deepagents import build_harness_env; preserve alias and import-time effects.
  // Source: vvaharness/orchestrator/preflight.py:1107-1117
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/preflight.py:1108-1115
    In source order: Evaluate once build_harness_env(model_id, provider, sdk_cfg=getattr(cfg, 'sdk', None), openai_cfg=getattr(cfg, 'openai', None), cfg_dir=getattr(cfg, '_data', {}).get('_config_dir')); assign in source target order to env. Then Evaluate once anthropic_base(env) if routes_to_anthropic(model_id, provider) else openai_base(env); assign in source target order to raw.
  }
  // Source: vvaharness/orchestrator/preflight.py:1116-1117
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/orchestrator/preflight.py:1117-1117
    End this invocation with '(unresolved)'.
  }
  // Source: vvaharness/orchestrator/preflight.py:1118-1118
  End this invocation with _scheme_host(raw).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1121-1141
// Source signature: _probe_deepagents_cache(cfg, model_node, *, label_base: str) -> tuple[dict, dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _probe_deepagents_cache(cfg, model_node, label_base) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1122-1124
  In source order: Retain source documentation literal source_literal_1122_4; it is not a model call. Then Resolve source import from vvaharness.backends.llm.deepagents import dispatch_prompt; preserve alias and import-time effects. Then Evaluate once cache_probe_filler(); assign in source target order to system_prompt.
  // Source: vvaharness/orchestrator/preflight.py:1126-1136
  // Source signature: _call(user_prompt: str, phase_label: str, workdir: str) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _call(user_prompt, phase_label, workdir) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/orchestrator/preflight.py:1127-1134
    // Source signature: _invoke()
    Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
    fn _invoke() {
      Bind arguments/defaults/annotations exactly as the source signature specifies.
      // Source: vvaharness/orchestrator/preflight.py:1129-1134
      Enter source context managers left-to-right: stage_floors('cache-probe', min_chars=_PROBE_PING_MIN_CHARS, min_tokens=_PROBE_PING_MIN_TOKENS) {
        // Source: vvaharness/orchestrator/preflight.py:1132-1134
        In source order: Evaluate dispatch_prompt(user_prompt, model=model_node, cfg=cfg, cwd=workdir, system_prompt=system_prompt, max_tokens=_PROBE_MAX_TOKENS, tag='cache-probe'); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      If execution reaches this end, finish with the source implicit None result.
    }
    // Source: vvaharness/orchestrator/preflight.py:1136-1136
    End this invocation with _observe_call(phase_label, _invoke).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1138-1140
  Enter source context managers left-to-right: tempfile.TemporaryDirectory(prefix='vva-cache-probe-deepagents-') bound to workdir {
    // Source: vvaharness/orchestrator/preflight.py:1139-1140
    In source order: Evaluate once _call(_USER_MSG_A, source_template_1139_35, workdir); assign in source target order to write. Then Evaluate once _call(_USER_MSG_B, source_template_1140_34, workdir); assign in source target order to read.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/orchestrator/preflight.py:1141-1141
  End this invocation with (write, read).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/preflight.py:1144-1268
// Source signature: run_cache_probe(cfg) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_cache_probe(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/preflight.py:1145-1151
  In source order: Retain source documentation literal source_literal_1145_4; it is not a model call. Then Evaluate once _cache_probe_targets(cfg); assign in source target order to targets. Then Evaluate once _deepagents_cache_probe_targets(cfg); assign in source target order to deepagents_targets. Then Evaluate once (('synthetic', cache_probe_filler()), ('deepdive-system', _deepdive_system_prompt())); assign in source target order to shapes. Then Evaluate once len(targets); assign in source target order to n_models.
  // Source: vvaharness/orchestrator/preflight.py:1152-1154
  In source order: Evaluate once len(deepagents_targets); assign in source target order to n_deepagents. Then Evaluate once n_models * len(shapes) * 2 * 2 + n_deepagents * 2; assign in source target order to n_calls.
  // Source: vvaharness/orchestrator/preflight.py:1155-1158
  if (the source predicate not n_calls is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:1156-1157
    In source order: Evaluate console.write('  [cache-probe] no sdk/openai/cli/deepagents model roles configured — nothing to probe'); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/preflight.py:1158-1158
    End this invocation with True.
  }
  // Source: vvaharness/orchestrator/preflight.py:1159-1169
  In source order: Evaluate console.write(source_template_1159_18); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to ok. Then For rows, assign []; source annotation list[dict]. Then Evaluate once console.status_table(title='  [cache-probe] measurements:', columns=('', 'via', 'model', 'filler', 'thinking_sent', 'base_url', 'creation', 'read', 'verdict')); assign in source target order to measured.
  // Source: vvaharness/orchestrator/preflight.py:1170-1218
  for each ((model_id, via), model_node) in sorted(targets.items()) {
    // Source: vvaharness/orchestrator/preflight.py:1171-1171
    In source order: Evaluate once _resolved_base_url_scheme_host(via); assign in source target order to base_url.
    // Source: vvaharness/orchestrator/preflight.py:1172-1218
    for each (shape_name, system_prompt) in shapes {
      // Source: vvaharness/orchestrator/preflight.py:1173-1218
      for each (think_label, budget) in (('on', _PROBE_THINKING_BUDGET), ('off', None)) {
        // Source: vvaharness/orchestrator/preflight.py:1174-1174
        In source order: Evaluate once source_template_1174_29; assign in source target order to label_base.
        // Source: vvaharness/orchestrator/preflight.py:1175-1192
        Perform the following protected operations {
          // Source: vvaharness/orchestrator/preflight.py:1176-1185
          In source order: Evaluate once time.time(); assign in source target order to t0. Then Evaluate once _call_and_diff(model=model_node, system_prompt=system_prompt, user_prompt=_USER_MSG_A, thinking_budget=budget, phase_label=source_template_1180_36); assign in source target order to write. Then Evaluate once _call_and_diff(model=model_node, system_prompt=system_prompt, user_prompt=_USER_MSG_B, thinking_budget=budget, phase_label=source_template_1184_36); assign in source target order to read. Then Evaluate once time.time() - t0; assign in source target order to elapsed.
        }
        // Source: vvaharness/orchestrator/preflight.py:1186-1192
        On the first matching source exception Exception as e, in handler order {
          // Source: vvaharness/orchestrator/preflight.py:1187-1191
          In source order: Evaluate console.status_row(measured, 'fail', via, model_id, shape_name, '—', '', '', '', source_template_1189_24); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to ok.
          // Source: vvaharness/orchestrator/preflight.py:1192-1192
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/orchestrator/preflight.py:1193-1196
        if (the source predicate elapsed > _CALL_B_DEADLINE_S is truthy) {
          // Source: vvaharness/orchestrator/preflight.py:1194-1196
          In source order: Evaluate log.warning(Event.PREFLIGHT_CACHE_PROBE_SLOW, via=via, model=model_id, filler=shape_name, thinking=think_label, elapsed=source_template_1195_81, target=source_template_1196_39); retain side effects and discard the expression result.
        }
        // Source: vvaharness/orchestrator/preflight.py:1197-1203
        In source order: Evaluate once _thinking_actually_sent(model_id, budget); assign in source target order to thinking_sent. Then Evaluate once usage_dict_for_classifier(cache_write=write['cache_write'], cache_read=read['cache_read'], write_present=write['cache_write_present'], read_present=read['cache_read_present']); assign in source target order to (usage_a, usage_b). Then Evaluate once classify_cache_verdict(usage_a, usage_b); assign in source target order to verdict.
        // Source: vvaharness/orchestrator/preflight.py:1204-1208
        if (the source predicate verdict == V_ANTHROPIC_NOT_HONOURED and _marker_would_be_placed(via, system_prompt, model_id) is False is truthy) {
          // Source: vvaharness/orchestrator/preflight.py:1208-1208
          In source order: Evaluate once V_MARKER_WITHHELD; assign in source target order to verdict.
        }
        // Source: vvaharness/orchestrator/preflight.py:1209-1218
        In source order: Evaluate rows.append({'model_id': model_id, 'via': via, 'filler': shape_name, 'thinking_requested': think_label, 'thinking_sent': thinking_sent, 'base_url': base_url, 'cache_creation': write['cache_write'], 'cache_read': read['cache_read'], 'verdict': verdict}); retain side effects and discard the expression result. Then Evaluate console.status_row(measured, 'ok', via, model_id, shape_name, 'yes' if thinking_sent else 'no', base_url, write['cache_write'], read['cache_read'], verdict); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/orchestrator/preflight.py:1220-1258
  for each ((model_id, via), model_node) in sorted(deepagents_targets.items()) {
    // Source: vvaharness/orchestrator/preflight.py:1221-1223
    In source order: Evaluate once getattr(model_node, 'provider', None); assign in source target order to provider. Then Evaluate once _deepagents_base_url(cfg, model_id, provider); assign in source target order to base_url. Then Evaluate once source_template_1223_21; assign in source target order to label_base.
    // Source: vvaharness/orchestrator/preflight.py:1224-1234
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/preflight.py:1225-1228
      In source order: Evaluate once time.time(); assign in source target order to t0. Then Evaluate once _probe_deepagents_cache(cfg, model_node, label_base=label_base); assign in source target order to (write, read). Then Evaluate once time.time() - t0; assign in source target order to elapsed.
    }
    // Source: vvaharness/orchestrator/preflight.py:1229-1234
    On the first matching source exception Exception as e, in handler order {
      // Source: vvaharness/orchestrator/preflight.py:1230-1233
      In source order: Evaluate console.status_row(measured, 'fail', via, model_id, 'synthetic', '—', '', '', '', source_template_1232_16); retain side effects and discard the expression result. Then Evaluate once False; assign in source target order to ok.
      // Source: vvaharness/orchestrator/preflight.py:1234-1234
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/preflight.py:1235-1239
    if (the source predicate elapsed > _CALL_B_DEADLINE_S is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:1237-1239
      In source order: Evaluate log.warning(Event.PREFLIGHT_CACHE_PROBE_SLOW, via=via, model=model_id, filler='synthetic', elapsed=source_template_1238_52, target=source_template_1239_31); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/preflight.py:1240-1245
    In source order: Evaluate once usage_dict_for_classifier(cache_write=write['cache_write'], cache_read=read['cache_read'], write_present=write['cache_write_present'], read_present=read['cache_read_present']); assign in source target order to (usage_a, usage_b). Then Evaluate once classify_cache_verdict(usage_a, usage_b); assign in source target order to verdict.
    // Source: vvaharness/orchestrator/preflight.py:1246-1249
    if (the source predicate verdict == V_ANTHROPIC_NOT_HONOURED and (not _deepagents_marker_would_be_placed(cfg, model_id, provider)) is truthy) {
      // Source: vvaharness/orchestrator/preflight.py:1249-1249
      In source order: Evaluate once V_MARKER_WITHHELD; assign in source target order to verdict.
    }
    // Source: vvaharness/orchestrator/preflight.py:1250-1258
    In source order: Evaluate rows.append({'model_id': model_id, 'via': via, 'filler': 'synthetic', 'thinking_requested': 'off', 'thinking_sent': False, 'base_url': base_url, 'cache_creation': write['cache_write'], 'cache_read': read['cache_read'], 'verdict': verdict}); retain side effects and discard the expression result. Then Evaluate console.status_row(measured, 'ok', via, model_id, 'synthetic', 'no', base_url, write['cache_write'], read['cache_read'], verdict); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1260-1261
  In source order: Evaluate console.console().print(measured); retain side effects and discard the expression result. Then Evaluate console.write(source_literal_1261_18); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/preflight.py:1262-1265
  for each r in rows {
    // Source: vvaharness/orchestrator/preflight.py:1263-1265
    In source order: Evaluate console.write(source_template_1263_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1266-1267
  if (the source predicate not rows is truthy) {
    // Source: vvaharness/orchestrator/preflight.py:1267-1267
    In source order: Evaluate console.write('    (no successful calls — see the FAILED rows above)'); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/preflight.py:1268-1268
  End this invocation with ok.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.backends.harness.models import DegenerateResponseError, HarnessJSONDecodeError, HarnessMessageParseError, TruncatedResponseError` at source line 30: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import cli, sdk` at source line 36: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli, sdk` at source line 36: `source_detail/vvaharness/backends/llm/cli/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli, sdk` at source line 36: `source_detail/vvaharness/backends/llm/sdk.py.sudo.md`.
- `from vvaharness.backends.llm import openai as oai` at source line 37: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import openai as oai` at source line 37: `source_detail/vvaharness/backends/llm/openai.py.sudo.md`.
- `from vvaharness.backends.llm.models import ClockKind, effort_scaled_seconds, rejection_text, validate_detection_tools` at source line 38: `source_detail/vvaharness/backends/llm/models.py.sudo.md`.
- `from vvaharness.backends.llm.registry import DEEPAGENTS_ROLES, POST_SCAN_ROLES, unrecognized_model_keys, use_responses_api_of` at source line 44: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.llm.registry import resolve as resolve_model` at source line 50: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.llm.tls import coerce_verify` at source line 51: `source_detail/vvaharness/backends/llm/tls.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _iter_model_roles, _resolve_against, highest_effort, role_effort` at source line 52: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.report.redact import redact` at source line 58: `source_detail/vvaharness/report/redact.py.sudo.md`.
- `from vvaharness.util import console` at source line 59: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 59: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 60: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.util.exceptions import exception_chain` at source line 61: `source_detail/vvaharness/util/exceptions.py.sudo.md`.
- `from vvaharness.util.response_quality import stage_floors` at source line 62: `source_detail/vvaharness/util/response_quality.py.sudo.md`.
- `from vvaharness.util.tokens import TOKENS` at source line 63: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.tokens import estimate_tokens as estimate_tokens` at source line 64: `source_detail/vvaharness/util/tokens.py.sudo.md`.
- `from vvaharness.util.environment import WARN as _WARN` at source line 266: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.util.environment import langsmith_tracing_check` at source line 267: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 390: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import route_carries_tools` at source line 474: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.harness.models import ToolStateNotRoundTrippedError` at source line 515: `source_detail/vvaharness/backends/harness/models.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 516: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _deepagents` at source line 516: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.registry import agentic as _probe_agentic` at source line 517: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.pipeline.stages.replay import start_daemon` at source line 627: `source_detail/vvaharness/pipeline/stages/replay.py.sudo.md`.
- `from vvaharness.backends.llm import cli_mcp` at source line 637: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import cli_mcp` at source line 637: `source_detail/vvaharness/backends/llm/cli_mcp.py.sudo.md`.
- `from vvaharness.backends.harness import OneShotOptions` at source line 686: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import credential_env_overrides` at source line 687: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import build_harness_env, markers_on, run_oneshot, think_in_prompt_enabled` at source line 690: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.registry import prompt as _probe` at source line 742: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.pipeline.stages.s4.prompts import build_system_prompt` at source line 1011: `source_detail/vvaharness/pipeline/stages/s4/prompts.py.sudo.md`.
- `from vvaharness.backends.llm.registry import prompt as _prompt` at source line 1064: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 1093: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import markers_on` at source line 1094: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.models import anthropic_base, openai_base` at source line 1101: `source_detail/vvaharness/backends/harness/deepagents/models.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 1105: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import build_harness_env` at source line 1106: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm.deepagents import dispatch_prompt` at source line 1123: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _da_routes` at source line 239: `source_detail/vvaharness/backends/llm/__init__.py.sudo.md`.
- `from vvaharness.backends.llm import deepagents as _da_routes` at source line 239: `source_detail/vvaharness/backends/llm/deepagents.py.sudo.md`.
- `from vvaharness.util.environment import _backend_credential_ok` at source line 365: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.util.environment import FAIL as _FAIL` at source line 397: `source_detail/vvaharness/util/environment.py.sudo.md`.
- `from vvaharness.util.environment import _gateway_check` at source line 398: `source_detail/vvaharness/util/environment.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/orchestrator/preflight.py.sudo.md). Exact strings in the evidence asset support this conversion.
