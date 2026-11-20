# vvaharness/util/environment.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/environment.py.evidence.json`. SHA-256: `721e85a6bee1ba09033bc62594e2715f5caa1c12fafe732c5a4a6944deecd515`.

```sudo
// Source: vvaharness/util/environment.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import importlib.metadata; preserve alias and import-time effects. Then Resolve source import import importlib.util; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects.
// Source: vvaharness/util/environment.py:22-26
In source order: Resolve source import import shutil; preserve alias and import-time effects. Then Resolve source import import socket; preserve alias and import-time effects. Then Resolve source import import ssl; preserve alias and import-time effects. Then Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vvaharness/util/environment.py:27-33
In source order: Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from urllib.parse import urlparse; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects. Then Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.provider_routing import routes_to_anthropic; preserve alias and import-time effects.
// Source: vvaharness/util/environment.py:34-46
In source order: Resolve source import from vvaharness.backends.llm.registry import DEEPAGENTS_ROLES, POST_SCAN_ROLES, unrecognized_model_keys; preserve alias and import-time effects. Then Resolve source import from vvaharness.config.constants import LOCAL_OVERLAY_NAME, NO_LOCAL_CONFIG_ENV; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator.config_paths import _iter_model_roles; preserve alias and import-time effects. Then Resolve source import from vvaharness.validation.config.validate_role import normalize_validate_backend, validate_model_spec; preserve alias and import-time effects. Then Evaluate once 'ok'; assign in source target order to OK.
// Source: vvaharness/util/environment.py:47-48
In source order: Evaluate once 'warn'; assign in source target order to WARN. Then Evaluate once 'fail'; assign in source target order to FAIL.
// Source: vvaharness/util/environment.py:52-57
// Source: vvaharness/util/environment.py:51-51
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/util/environment.py:52-57
interface Check {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/environment.py:53-57
  In source order: For name, declare without assigning a value; source annotation str. Then For status, declare without assigning a value; source annotation str. Then For detail, declare without assigning a value; source annotation str. Then For required, assign False; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/util/environment.py:60-61
// Source signature: _is_set(env: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_set(env) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:61-61
  End this invocation with bool(os.environ.get(env)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:64-74
// Source signature: _looks_like_jwt(v: str | None) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _looks_like_jwt(v) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:65-65
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call.
  // Source: vvaharness/util/environment.py:66-67
  if (the source predicate not v is truthy) {
    // Source: vvaharness/util/environment.py:67-67
    End this invocation with False.
  }
  // Source: vvaharness/util/environment.py:68-69
  if (the source predicate v.startswith('eyJ') is truthy) {
    // Source: vvaharness/util/environment.py:69-69
    End this invocation with True.
  }
  // Source: vvaharness/util/environment.py:71-71
  In source order: Evaluate once v.split('.'); assign in source target order to parts.
  // Source: vvaharness/util/environment.py:72-73
  if (the source predicate len(parts) == 3 and v.startswith('ey') is truthy) {
    // Source: vvaharness/util/environment.py:73-73
    End this invocation with all((bool(p) for p in parts)).
  }
  // Source: vvaharness/util/environment.py:74-74
  End this invocation with False.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:77-94
// Source signature: python_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn python_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:78-80
  In source order: Retain source documentation literal source_literal_78_4; it is not a model call. Then Evaluate once (3, 10); assign in source target order to floor.
  // Source: vvaharness/util/environment.py:81-89
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:82-85
    In source order: Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from importlib.metadata import metadata; preserve alias and import-time effects. Then Evaluate once metadata('vvaharness').get('Requires-Python') or ''; assign in source target order to req. Then Evaluate once re.search('>=\\s*(\\d+)\\.(\\d+)', req); assign in source target order to m.
    // Source: vvaharness/util/environment.py:86-87
    if (the source predicate m is truthy) {
      // Source: vvaharness/util/environment.py:87-87
      In source order: Evaluate once (int(m.group(1)), int(m.group(2))); assign in source target order to floor.
    }
  }
  // Source: vvaharness/util/environment.py:88-89
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/util/environment.py:89-89
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/util/environment.py:90-90
  In source order: Evaluate once '.'.join((str(v) for v in sys.version_info[:3])); assign in source target order to cur.
  // Source: vvaharness/util/environment.py:91-92
  if (the source predicate sys.version_info[:2] >= floor is truthy) {
    // Source: vvaharness/util/environment.py:92-92
    End this invocation with Check('Python', OK, source_template_92_35).
  }
  // Source: vvaharness/util/environment.py:93-94
  End this invocation with Check('Python', FAIL, source_template_94_17, required=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:97-102
// Source signature: tool_check(cmd: str, why: str, *, required: bool=False) -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn tool_check(cmd, why, required) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:98-98
  In source order: Evaluate once shutil.which(cmd); assign in source target order to path.
  // Source: vvaharness/util/environment.py:99-100
  if (the source predicate path is truthy) {
    // Source: vvaharness/util/environment.py:100-100
    End this invocation with Check(cmd, OK, path).
  }
  // Source: vvaharness/util/environment.py:101-102
  End this invocation with Check(cmd, FAIL if required else WARN, source_template_101_50, required=required).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:106-113
In source order: Evaluate once [('Claude Code', 'claude', ('ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN', 'CLAUDE_CODE_OAUTH_TOKEN'), 'via:cli'), ('OpenAI Codex', 'codex', ('OPENAI_API_KEY',), 'via:openai'), ('Gemini CLI', 'gemini', ('GEMINI_API_KEY', 'GOOGLE_API_KEY'), '—'), ('Cursor Agent', 'cursor-agent', (), '—'), ('GitHub Copilot CLI', 'copilot', (), 'via:cli')]; assign in source target order to _AGENTS.
// Source: vvaharness/util/environment.py:116-129
// Source signature: _claude_code_login_present() -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _claude_code_login_present() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:117-117
  In source order: Retain source documentation literal source_literal_117_4; it is not a model call.
  // Source: vvaharness/util/environment.py:119-120
  if (the source predicate (Path.home() / '.claude' / '.credentials.json').exists() is truthy) {
    // Source: vvaharness/util/environment.py:120-120
    End this invocation with True.
  }
  // Source: vvaharness/util/environment.py:121-121
  In source order: Evaluate once Path.home() / '.claude.json'; assign in source target order to state.
  // Source: vvaharness/util/environment.py:122-123
  if (the source predicate not state.exists() is truthy) {
    // Source: vvaharness/util/environment.py:123-123
    End this invocation with False.
  }
  // Source: vvaharness/util/environment.py:124-128
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:125-126
    In source order: Resolve source import import json; preserve alias and import-time effects. Then Evaluate once json.loads(state.read_text(encoding='utf-8')); assign in source target order to data.
  }
  // Source: vvaharness/util/environment.py:127-128
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/util/environment.py:128-128
    End this invocation with False.
  }
  // Source: vvaharness/util/environment.py:129-129
  End this invocation with bool(data.get('oauthAccount')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:132-154
// Source signature: agent_checks() -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn agent_checks() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:133-135
  In source order: Retain source documentation literal source_literal_133_4; it is not a model call. Then For out, assign []; source annotation list[Check]. Then Evaluate once _claude_code_login_present(); assign in source target order to oauth.
  // Source: vvaharness/util/environment.py:136-153
  for each (display, cmd, keys, backend) in _AGENTS {
    // Source: vvaharness/util/environment.py:137-137
    In source order: Evaluate once shutil.which(cmd); assign in source target order to path.
    // Source: vvaharness/util/environment.py:138-140
    if (the source predicate not path is truthy) {
      // Source: vvaharness/util/environment.py:139-139
      In source order: Evaluate out.append(Check(source_template_139_29, WARN, 'not installed')); retain side effects and discard the expression result.
      // Source: vvaharness/util/environment.py:140-140
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/util/environment.py:141-141
    In source order: Evaluate once not keys or any((_is_set(k) for k in keys)) or (cmd == 'claude' and oauth); assign in source target order to has_auth.
    // Source: vvaharness/util/environment.py:142-150
    if (the source predicate not keys is truthy) {
      // Source: vvaharness/util/environment.py:143-143
      In source order: Evaluate once 'installed'; assign in source target order to keyinfo.
    }
    else {
      // Source: vvaharness/util/environment.py:146-150
      In source order: Evaluate once 'installed and logged in' if has_auth else 'installed; login not detected' + (' (a macOS Keychain-only `claude` login is not visible here — try `claude` once to confirm)' if cmd == 'claude' else ''); assign in source target order to keyinfo.
    }
    // Source: vvaharness/util/environment.py:151-153
    In source order: Evaluate once OK if has_auth else WARN; assign in source target order to status. Then Evaluate out.append(Check(source_template_152_25, status, source_template_153_25)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:154-154
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:158-165
In source order: Evaluate once [('pydantic', True), ('yaml', True), ('anthropic', True), ('tree_sitter', False), ('tree_sitter_language_pack', False), ('openai', False)]; assign in source target order to _DEPS.
// Source: vvaharness/util/environment.py:168-197
// Source signature: dep_checks() -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dep_checks() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:169-169
  In source order: For out, assign []; source annotation list[Check].
  // Source: vvaharness/util/environment.py:170-195
  for each (mod, required) in _DEPS {
    // Source: vvaharness/util/environment.py:171-176
    In source order: Evaluate once importlib.util.find_spec(mod) is not None; assign in source target order to present. Then Evaluate once {'yaml': 'PyYAML', 'tree_sitter': 'tree-sitter', 'tree_sitter_language_pack': 'tree-sitter-language-pack'}.get(mod, mod); assign in source target order to label.
    // Source: vvaharness/util/environment.py:177-195
    if (the source predicate present is truthy) {
      // Source: vvaharness/util/environment.py:178-178
      In source order: Evaluate out.append(Check(source_template_178_29, OK, 'importable')); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/util/environment.py:179-195
      if (the source predicate required is truthy) {
        // Source: vvaharness/util/environment.py:180-180
        In source order: Evaluate out.append(Check(source_template_180_29, FAIL, 'missing', required=True)); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/util/environment.py:181-195
        if (the source predicate mod == 'tree_sitter' is truthy) {
          // Source: vvaharness/util/environment.py:182-186
          In source order: Evaluate out.append(Check(source_template_183_16, WARN, 'NOT INSTALLED — call graph falls back to regex (degraded taint coverage)')); retain side effects and discard the expression result.
        }
        else {
          // Source: vvaharness/util/environment.py:187-195
          if (the source predicate mod == 'tree_sitter_language_pack' is truthy) {
            // Source: vvaharness/util/environment.py:188-192
            In source order: Evaluate out.append(Check(source_template_189_16, WARN, 'NOT INSTALLED — tree-sitter AST plugins unavailable; call graph degrades')); retain side effects and discard the expression result.
          }
          else {
            // Source: vvaharness/util/environment.py:194-195
            In source order: Evaluate out.append(Check(source_template_194_29, WARN, 'missing (optional — needed only for via:openai)')); retain side effects and discard the expression result.
          }
        }
      }
    }
  }
  // Source: vvaharness/util/environment.py:196-196
  In source order: Evaluate out.append(graph_sdk_check()); retain side effects and discard the expression result.
  // Source: vvaharness/util/environment.py:197-197
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:200-200
In source order: Evaluate once ('vendor', 'context_graph_sdk', 'src', 'context_graph_sdk'); assign in source target order to _SDK_VENDOR_PARTS.
// Source: vvaharness/util/environment.py:203-210
// Source signature: _module_dir(name: str) -> Path | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _module_dir(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:204-204
  In source order: Retain source documentation literal source_literal_204_4; it is not a model call.
  // Source: vvaharness/util/environment.py:205-208
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:206-206
    In source order: Evaluate once importlib.util.find_spec(name); assign in source target order to spec.
  }
  // Source: vvaharness/util/environment.py:207-208
  On the first matching source exception (ImportError, ValueError), in handler order {
    // Source: vvaharness/util/environment.py:208-208
    End this invocation with None.
  }
  // Source: vvaharness/util/environment.py:209-209
  In source order: Evaluate once getattr(spec, 'origin', None) if spec else None; assign in source target order to origin.
  // Source: vvaharness/util/environment.py:210-210
  End this invocation with Path(origin).resolve().parent if origin else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:213-218
// Source signature: _separately_installed_sdk() -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _separately_installed_sdk() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:214-214
  In source order: Retain source documentation literal source_literal_214_4; it is not a model call.
  // Source: vvaharness/util/environment.py:215-218
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:216-216
    End this invocation with importlib.metadata.version('context-graph-sdk').
  }
  // Source: vvaharness/util/environment.py:217-218
  On the first matching source exception importlib.metadata.PackageNotFoundError, in handler order {
    // Source: vvaharness/util/environment.py:218-218
    End this invocation with ''.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:221-241
// Source signature: graph_sdk_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn graph_sdk_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:222-223
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call. Then Evaluate once _module_dir('context_graph_sdk'); assign in source target order to sdk.
  // Source: vvaharness/util/environment.py:224-226
  if (the source predicate sdk is None is truthy) {
    // Source: vvaharness/util/environment.py:225-226
    End this invocation with Check('dep: context-graph-sdk', FAIL, 'not importable — S0/S1 cannot build the code graph', required=True).
  }
  // Source: vvaharness/util/environment.py:227-227
  In source order: Evaluate once _separately_installed_sdk(); assign in source target order to stray.
  // Source: vvaharness/util/environment.py:228-233
  if (the source predicate stray is truthy) {
    // Source: vvaharness/util/environment.py:229-233
    End this invocation with Check('dep: context-graph-sdk', FAIL, source_template_230_21, required=True).
  }
  // Source: vvaharness/util/environment.py:234-234
  In source order: Evaluate once _module_dir('vvaharness'); assign in source target order to own.
  // Source: vvaharness/util/environment.py:235-236
  if (the source predicate own is None or sdk.parent == own.parent or sdk == own.parent / Path(*_SDK_VENDOR_PARTS) is truthy) {
    // Source: vvaharness/util/environment.py:236-236
    End this invocation with Check('dep: context-graph-sdk', OK, source_template_236_51).
  }
  // Source: vvaharness/util/environment.py:237-241
  End this invocation with Check('dep: context-graph-sdk', FAIL, source_template_238_17, required=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:244-250
// Source signature: _release(version: str) -> tuple[int, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _release(version) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:245-249
  In source order: Retain source documentation literal source_literal_245_4; it is not a model call. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once version.split('!')[-1].split('+')[0]; assign in source target order to core.
  // Source: vvaharness/util/environment.py:250-250
  End this invocation with tuple((int(n) for n in re.findall('\\d+', core))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:253-285
// Source signature: anthropic_version_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn anthropic_version_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:254-257
  In source order: Retain source documentation literal source_literal_254_4; it is not a model call. Then Resolve source import import re; preserve alias and import-time effects.
  // Source: vvaharness/util/environment.py:259-264
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:260-260
    In source order: Evaluate once importlib.metadata.version('anthropic'); assign in source target order to installed.
  }
  // Source: vvaharness/util/environment.py:261-264
  On the first matching source exception importlib.metadata.PackageNotFoundError, in handler order {
    // Source: vvaharness/util/environment.py:263-264
    End this invocation with Check('anthropic version', OK, 'no version metadata found (see dep: anthropic)').
  }
  // Source: vvaharness/util/environment.py:265-268
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:266-266
    In source order: Evaluate once importlib.metadata.requires('vvaharness') or []; assign in source target order to reqs.
  }
  // Source: vvaharness/util/environment.py:267-268
  On the first matching source exception importlib.metadata.PackageNotFoundError, in handler order {
    // Source: vvaharness/util/environment.py:268-268
    In source order: Evaluate once []; assign in source target order to reqs.
  }
  // Source: vvaharness/util/environment.py:270-272
  In source order: Evaluate once next((r for r in reqs if re.match('anthropic\\s*[\\[<>=!~]', r)), ''); assign in source target order to spec. Then Evaluate once re.search('<\\s*(\\d[^,\\s]*)', spec); assign in source target order to ceiling.
  // Source: vvaharness/util/environment.py:273-275
  if (the source predicate not ceiling is truthy) {
    // Source: vvaharness/util/environment.py:274-275
    End this invocation with Check('anthropic version', OK, source_template_275_21).
  }
  // Source: vvaharness/util/environment.py:276-278
  if (the source predicate _release(installed) < _release(ceiling.group(1)) is truthy) {
    // Source: vvaharness/util/environment.py:277-278
    End this invocation with Check('anthropic version', OK, source_template_278_21).
  }
  // Source: vvaharness/util/environment.py:279-285
  End this invocation with Check('anthropic version', FAIL, source_template_281_8, required=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:289-293
In source order: Evaluate once ['ANTHROPIC_SDK_API_KEY', 'ANTHROPIC_API_KEY', 'ANTHROPIC_AUTH_TOKEN', 'CLAUDE_CODE_OAUTH_TOKEN', 'OPENAI_API_KEY', 'GEMINI_API_KEY', 'GITHUB_TOKEN']; assign in source target order to _CRED_ENVS.
// Source: vvaharness/util/environment.py:296-301
// Source signature: credential_checks() -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn credential_checks() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:297-297
  In source order: For out, assign []; source annotation list[Check].
  // Source: vvaharness/util/environment.py:298-300
  for each env in _CRED_ENVS {
    // Source: vvaharness/util/environment.py:299-300
    In source order: Evaluate out.append(Check(source_template_299_25, OK if _is_set(env) else WARN, 'set' if _is_set(env) else 'unset')); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:301-301
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:305-310
In source order: Evaluate once (('LANGSMITH_TRACING_V2', 'LANGCHAIN_TRACING_V2'), ('LANGSMITH_TRACING', 'LANGCHAIN_TRACING')); assign in source target order to _TRACING_GATE_ENVS. Then Evaluate once ('LANGSMITH_API_KEY', 'LANGCHAIN_API_KEY'); assign in source target order to _TRACING_KEY_ENVS.
// Source: vvaharness/util/environment.py:313-322
// Source signature: _langsmith_tracing_gate() -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _langsmith_tracing_gate() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:314-314
  In source order: Retain source documentation literal source_literal_314_4; it is not a model call.
  // Source: vvaharness/util/environment.py:316-321
  for each group in _TRACING_GATE_ENVS {
    // Source: vvaharness/util/environment.py:317-321
    for each name in group {
      // Source: vvaharness/util/environment.py:318-318
      In source order: Evaluate once os.environ.get(name); assign in source target order to v.
      // Source: vvaharness/util/environment.py:319-321
      if (the source predicate v is not None and v.strip() != '' is truthy) {
        // Source: vvaharness/util/environment.py:321-321
        End this invocation with name if v == 'true' else None.
      }
    }
  }
  // Source: vvaharness/util/environment.py:322-322
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:325-349
// Source signature: langsmith_tracing_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn langsmith_tracing_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:326-328
  In source order: Retain source documentation literal source_literal_326_4; it is not a model call. Then Evaluate once _langsmith_tracing_gate(); assign in source target order to gate.
  // Source: vvaharness/util/environment.py:329-332
  if (the source predicate gate is None is truthy) {
    // Source: vvaharness/util/environment.py:330-332
    End this invocation with Check('LangSmith tracing', OK, 'disabled (no LANGSMITH_TRACING* / LANGCHAIN_TRACING* gate variable is "true")').
  }
  // Source: vvaharness/util/environment.py:333-336
  if (the source predicate importlib.util.find_spec('langsmith') is None is truthy) {
    // Source: vvaharness/util/environment.py:334-336
    End this invocation with Check('LangSmith tracing', OK, source_template_335_21).
  }
  // Source: vvaharness/util/environment.py:337-342
  In source order: Evaluate once next((k for k in _TRACING_KEY_ENVS if _is_set(k)), None); assign in source target order to key. Then Evaluate once source_template_338_16 if key else source_literal_340_16; assign in source target order to key_note.
  // Source: vvaharness/util/environment.py:343-349
  End this invocation with Check('LangSmith tracing', WARN, source_template_345_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:352-368
// Source signature: _gateway_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _gateway_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:353-355
  In source order: Retain source documentation literal source_literal_353_4; it is not a model call. Then Evaluate once os.environ.get('ANTHROPIC_BASE_URL'); assign in source target order to base. Then Evaluate once os.environ.get('ANTHROPIC_API_KEY'); assign in source target order to key.
  // Source: vvaharness/util/environment.py:356-359
  if (the source predicate base is truthy) {
    // Source: vvaharness/util/environment.py:358-359
    End this invocation with Check('via:sdk endpoint', OK, source_template_359_21).
  }
  // Source: vvaharness/util/environment.py:360-367
  if (the source predicate _looks_like_jwt(key) is truthy) {
    // Source: vvaharness/util/environment.py:361-367
    End this invocation with Check('via:sdk endpoint', FAIL, source_literal_362_21, required=True).
  }
  // Source: vvaharness/util/environment.py:368-368
  End this invocation with Check('via:sdk endpoint', OK, 'public api.anthropic.com (default)').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:371-372
In source order: Evaluate once ('.zshrc', '.zprofile', '.bashrc', '.bash_profile', '.profile'); assign in source target order to _RC_FILES. Then Evaluate once None; assign in source target order to _BASE_URL_RX.
// Source: vvaharness/util/environment.py:375-394
// Source signature: detect_gateway() -> tuple[str | None, str | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_gateway() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:376-378
  In source order: Retain source documentation literal source_literal_376_4; it is not a model call. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once os.environ.get('ANTHROPIC_BASE_URL'); assign in source target order to live.
  // Source: vvaharness/util/environment.py:379-380
  if (the source predicate live is truthy) {
    // Source: vvaharness/util/environment.py:380-380
    End this invocation with (live, 'environment').
  }
  // Source: vvaharness/util/environment.py:381-381
  In source order: Evaluate once re.compile('ANTHROPIC_BASE_URL\\s*=\\s*["\\\']?(https?://[^"\\\'\\s]+)'); assign in source target order to rx.
  // Source: vvaharness/util/environment.py:382-393
  for each name in _RC_FILES {
    // Source: vvaharness/util/environment.py:383-383
    In source order: Evaluate once Path.home() / name; assign in source target order to p.
    // Source: vvaharness/util/environment.py:384-385
    if (the source predicate not p.is_file() is truthy) {
      // Source: vvaharness/util/environment.py:385-385
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/util/environment.py:386-393
    Perform the following protected operations {
      // Source: vvaharness/util/environment.py:387-390
      for each line in p.read_text(encoding='utf-8', errors='ignore').splitlines() {
        // Source: vvaharness/util/environment.py:388-388
        In source order: Evaluate once rx.search(line); assign in source target order to m.
        // Source: vvaharness/util/environment.py:389-390
        if (the source predicate m is truthy) {
          // Source: vvaharness/util/environment.py:390-390
          End this invocation with (m.group(1), source_template_390_39).
        }
      }
    }
    // Source: vvaharness/util/environment.py:392-393
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/util/environment.py:393-393
      Continue the immediately enclosing source loop at its next iteration.
    }
  }
  // Source: vvaharness/util/environment.py:394-394
  End this invocation with (None, None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:397-403
// Source signature: detect_ca_cert() -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_ca_cert() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:398-399
  In source order: Retain source documentation literal source_literal_398_4; it is not a model call. Then Evaluate once os.environ.get('NODE_EXTRA_CA_CERTS'); assign in source target order to env_cert.
  // Source: vvaharness/util/environment.py:400-401
  if (the source predicate env_cert and Path(env_cert).is_file() is truthy) {
    // Source: vvaharness/util/environment.py:401-401
    End this invocation with env_cert.
  }
  // Source: vvaharness/util/environment.py:402-402
  In source order: Evaluate once Path.home() / 'cacerts.pem'; assign in source target order to default.
  // Source: vvaharness/util/environment.py:403-403
  End this invocation with str(default) if default.is_file() else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:406-430
// Source signature: recommend_profile() -> tuple[str | None, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn recommend_profile() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:407-413
  In source order: Retain source documentation literal source_literal_407_4; it is not a model call. Then Evaluate once shutil.which('claude') and (_looks_like_jwt(os.environ.get('ANTHROPIC_API_KEY')) or _is_set('ANTHROPIC_AUTH_TOKEN') or _is_set('CLAUDE_CODE_OAUTH_TOKEN') or _claude_code_login_present()); assign in source target order to cli_auth.
  // Source: vvaharness/util/environment.py:414-418
  if (the source predicate cli_auth and _is_set('ANTHROPIC_SDK_API_KEY') is truthy) {
    // Source: vvaharness/util/environment.py:415-418
    End this invocation with ('default', source_literal_415_27).
  }
  // Source: vvaharness/util/environment.py:419-423
  if (the source predicate cli_auth is truthy) {
    // Source: vvaharness/util/environment.py:420-423
    End this invocation with ('default', source_literal_420_27).
  }
  // Source: vvaharness/util/environment.py:424-426
  if (the source predicate _is_set('ANTHROPIC_SDK_API_KEY') is truthy) {
    // Source: vvaharness/util/environment.py:425-426
    End this invocation with ('sdk', 'ANTHROPIC_SDK_API_KEY is set — sdk.yaml routes model roles via sdk; setup checks the S11 credential separately').
  }
  // Source: vvaharness/util/environment.py:427-429
  if (the source predicate _is_set('OPENAI_API_KEY') is truthy) {
    // Source: vvaharness/util/environment.py:428-429
    End this invocation with ('full', 'OPENAI_API_KEY is set — full.yaml includes OpenAI roles; setup checks its other backends separately').
  }
  // Source: vvaharness/util/environment.py:430-430
  End this invocation with (None, 'no usable credential detected yet').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:433-446
// Source signature: dotenv_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn dotenv_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:434-438
  In source order: Retain source documentation literal source_literal_434_4; it is not a model call. Then Resolve source import from vvaharness.cli import _dotenv_selection; preserve alias and import-time effects. Then Evaluate once _dotenv_selection(); assign in source target order to (path, source, rejected). Then Evaluate once ', '.join((str(p) for p in rejected)); assign in source target order to ignored.
  // Source: vvaharness/util/environment.py:439-442
  if (the source predicate path is None is truthy) {
    // Source: vvaharness/util/environment.py:440-441
    if (the source predicate rejected is truthy) {
      // Source: vvaharness/util/environment.py:441-441
      End this invocation with Check('.env', WARN, source_template_441_39).
    }
    // Source: vvaharness/util/environment.py:442-442
    End this invocation with Check('.env', OK, 'not found (optional; use setup --write-env)').
  }
  // Source: vvaharness/util/environment.py:443-443
  In source order: Evaluate once '.env found' if source == 'cwd' else source_template_443_50; assign in source target order to detail.
  // Source: vvaharness/util/environment.py:444-445
  if (the source predicate rejected is truthy) {
    // Source: vvaharness/util/environment.py:445-445
    End this invocation with Check('.env', WARN, source_template_445_35).
  }
  // Source: vvaharness/util/environment.py:446-446
  End this invocation with Check('.env', OK, detail).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:449-460
// Source signature: _applied_overlay_check(name: str, local: Path, cfg_path: str | Path) -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _applied_overlay_check(name, local, cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:450-450
  In source order: Retain source documentation literal source_literal_450_4; it is not a model call.
  // Source: vvaharness/util/environment.py:451-455
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:452-453
    In source order: Evaluate once yaml.safe_load(local.read_text(encoding='utf-8')) or {}; assign in source target order to over. Then Evaluate once config_mod.load(cfg_path); assign in source target order to cfg.
  }
  // Source: vvaharness/util/environment.py:454-455
  On the first matching source exception (OSError, ValueError, yaml.YAMLError) as e, in handler order {
    // Source: vvaharness/util/environment.py:455-455
    End this invocation with Check(name, FAIL, source_template_455_33, required=True).
  }
  // Source: vvaharness/util/environment.py:456-457
  if (the source predicate not isinstance(over, dict) is truthy) {
    // Source: vvaharness/util/environment.py:457-457
    End this invocation with Check(name, FAIL, source_template_457_33, required=True).
  }
  // Source: vvaharness/util/environment.py:458-459
  In source order: Evaluate once ', '.join(config_mod._overlay_override_entries(config_mod._leaf_paths(over), cfg._data)) or '(empty)'; assign in source target order to detail.
  // Source: vvaharness/util/environment.py:460-460
  End this invocation with Check(name, OK, source_template_460_27).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:463-482
// Source signature: overlay_check(cfg_path: str | Path) -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn overlay_check(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:464-466
  In source order: Retain source documentation literal source_literal_464_4; it is not a model call. Then Evaluate once 'config overlay'; assign in source target order to name. Then Evaluate once Path(cfg_path).with_name(LOCAL_OVERLAY_NAME); assign in source target order to local.
  // Source: vvaharness/util/environment.py:467-481
  if (the source predicate not local.exists() is truthy) {
    // Source: vvaharness/util/environment.py:468-468
    In source order: Evaluate once Check(name, OK, source_template_468_32); assign in source target order to check.
  }
  else {
    // Source: vvaharness/util/environment.py:469-481
    if (the source predicate os.environ.get(NO_LOCAL_CONFIG_ENV) is truthy) {
      // Source: vvaharness/util/environment.py:470-471
      In source order: Evaluate once Check(name, OK, source_template_471_22); assign in source target order to check.
    }
    else {
      // Source: vvaharness/util/environment.py:472-481
      if (the source predicate getattr(os, 'geteuid', None) is not None and (not config_mod._local_overlay_trusted(local)) is truthy) {
        // Source: vvaharness/util/environment.py:474-479
        In source order: Evaluate once Check(name, FAIL, source_template_476_12, required=True); assign in source target order to check.
      }
      else {
        // Source: vvaharness/util/environment.py:481-481
        In source order: Evaluate once _applied_overlay_check(name, local, cfg_path); assign in source target order to check.
      }
    }
  }
  // Source: vvaharness/util/environment.py:482-482
  End this invocation with check.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:485-494
// Source signature: _via_gap_check(name: str, gap: str, roles: set[str], *, hint: str='') -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _via_gap_check(name, gap, roles, hint) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:487-487
  In source order: Retain source documentation literal source_literal_487_4; it is not a model call.
  // Source: vvaharness/util/environment.py:489-491
  if (the source predicate not roles <= POST_SCAN_ROLES is truthy) {
    // Source: vvaharness/util/environment.py:490-491
    End this invocation with Check(name, FAIL, source_template_490_33, required=True).
  }
  // Source: vvaharness/util/environment.py:492-494
  End this invocation with Check(name, WARN, source_template_493_17).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:497-596
// Source signature: config_check(cfg_path: str | Path) -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn config_check(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:498-499
  In source order: Retain source documentation literal source_literal_498_4; it is not a model call. Then Evaluate once Path(cfg_path); assign in source target order to p.
  // Source: vvaharness/util/environment.py:500-501
  if (the source predicate not p.exists() is truthy) {
    // Source: vvaharness/util/environment.py:501-501
    End this invocation with [Check('config', FAIL, source_template_501_38, required=True)].
  }
  // Source: vvaharness/util/environment.py:502-506
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:503-504
    In source order: Resolve source import from vvaharness import config as config_mod; preserve alias and import-time effects. Then Evaluate once config_mod.load(p); assign in source target order to cfg.
  }
  // Source: vvaharness/util/environment.py:505-506
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/util/environment.py:506-506
    End this invocation with [Check('config', FAIL, source_template_506_38, required=True)].
  }
  // Source: vvaharness/util/environment.py:507-507
  In source order: Evaluate once Path.cwd() / 'config.yaml'; assign in source target order to cwd_cfg.
  // Source: vvaharness/util/environment.py:508-514
  if (the source predicate p.resolve() == cwd_cfg.resolve() is truthy) {
    // Source: vvaharness/util/environment.py:509-509
    In source order: Evaluate once 'config.yaml loads'; assign in source target order to detail.
  }
  else {
    // Source: vvaharness/util/environment.py:510-514
    if (the source predicate not cwd_cfg.exists() is truthy) {
      // Source: vvaharness/util/environment.py:511-512
      In source order: Evaluate once source_template_511_18; assign in source target order to detail.
    }
    else {
      // Source: vvaharness/util/environment.py:514-514
      In source order: Evaluate once source_template_514_17; assign in source target order to detail.
    }
  }
  // Source: vvaharness/util/environment.py:515-518
  In source order: Evaluate once [Check('config', OK, detail)]; assign in source target order to out. Then For nodes, assign dict(_iter_model_roles(cfg)); source annotation dict[str, object]. Then For roles_by_via, assign {}; source annotation dict[str, set[str]].
  // Source: vvaharness/util/environment.py:519-520
  for each (r, node) in nodes.items() {
    // Source: vvaharness/util/environment.py:520-520
    In source order: Evaluate roles_by_via.setdefault(getattr(node, 'via', None) or 'cli', set()).add(r); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:521-527
  In source order: Evaluate once set(roles_by_via); assign in source target order to vias. Then Evaluate out.append(Check('active backends', OK, ', '.join(sorted(vias)) or '(none)')); retain side effects and discard the expression result. Then Evaluate once sorted((r for r, node in nodes.items() if (getattr(node, 'via', None) or 'cli') == 'deepagents' and r not in DEEPAGENTS_ROLES)); assign in source target order to invalid_deepagents.
  // Source: vvaharness/util/environment.py:528-537
  if (the source predicate invalid_deepagents is truthy) {
    // Source: vvaharness/util/environment.py:530-537
    In source order: Evaluate once ', '.join((source_template_530_30 for r in sorted(DEEPAGENTS_ROLES))); assign in source target order to supported. Then Evaluate out.append(Check('via:deepagents roles', FAIL, source_template_534_12, required=True)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:539-543
  In source order: Evaluate once [source_template_540_8 for r, node in nodes.items() for key in unrecognized_model_keys(node)]; assign in source target order to unknown_keys.
  // Source: vvaharness/util/environment.py:544-549
  if (the source predicate unknown_keys is truthy) {
    // Source: vvaharness/util/environment.py:545-549
    In source order: Evaluate out.append(Check('model config keys', WARN, source_template_548_12)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:550-583
  if (the source predicate 'sdk' in vias is truthy) {
    // Source: vvaharness/util/environment.py:551-558
    In source order: Evaluate out.append(_gateway_check()); retain side effects and discard the expression result. Then Evaluate once getattr(cfg, 'sdk', None); assign in source target order to sdk_cfg. Then Evaluate once _is_set('ANTHROPIC_SDK_API_KEY') or bool(getattr(sdk_cfg, 'api_key', None)); assign in source target order to has_sdk_key. Then Evaluate once vias <= {'sdk', 'deepagents'}; assign in source target order to sdk_sole. Then Evaluate once sdk_sole and (_is_set('ANTHROPIC_API_KEY') or _is_set('ANTHROPIC_AUTH_TOKEN')); assign in source target order to fallback.
    // Source: vvaharness/util/environment.py:559-571
    if (the source predicate has_sdk_key is truthy) {
      // Source: vvaharness/util/environment.py:560-560
      In source order: Perform no operation at this source statement.
    }
    else {
      // Source: vvaharness/util/environment.py:561-571
      if (the source predicate fallback is truthy) {
        // Source: vvaharness/util/environment.py:562-565
        In source order: Evaluate out.append(Check('via:sdk credential', OK, 'ANTHROPIC_SDK_API_KEY unset — using ANTHROPIC_API_KEY/ANTHROPIC_AUTH_TOKEN fallback (no via:cli role in this profile)')); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/util/environment.py:567-571
        In source order: Evaluate once ' — or set ANTHROPIC_API_KEY (accepted as a fallback)' if sdk_sole else ''; assign in source target order to hint. Then Evaluate out.append(_via_gap_check('via:sdk credential', 'ANTHROPIC_SDK_API_KEY not set', roles_by_via['sdk'], hint=hint)); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/util/environment.py:573-583
    for each (env_name, attr, note) in (('ANTHROPIC_SDK_BASE_URL', 'base_url', 'gateway endpoint — defaults to public api.anthropic.com'), ('ANTHROPIC_SDK_CA_CERT', 'ca_cert', 'gateway CA bundle — only for a private-CA gateway'), ('ANTHROPIC_SDK_CLIENT_CERT', 'client_cert', 'client cert for mTLS — off when unset')) {
      // Source: vvaharness/util/environment.py:581-583
      In source order: Evaluate once _is_set(env_name) or bool(getattr(sdk_cfg, attr, None)); assign in source target order to present. Then Evaluate out.append(Check(source_template_582_29, OK if present else WARN, 'set' if present else source_template_583_51)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/util/environment.py:584-587
  if (the source predicate 'openai' in vias and (not _is_set('OPENAI_API_KEY')) is truthy) {
    // Source: vvaharness/util/environment.py:585-587
    In source order: Evaluate out.append(_via_gap_check('via:openai credential', 'OPENAI_API_KEY not set', roles_by_via['openai'])); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:588-591
  if (the source predicate 'cli' in vias and (not shutil.which('claude')) is truthy) {
    // Source: vvaharness/util/environment.py:589-591
    In source order: Evaluate out.append(_via_gap_check('via:cli backend', '`claude` CLI not on PATH', roles_by_via['cli'])); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:592-595
  In source order: Apply source augmented assignment out += _deepagents_checks(nodes, cfg=cfg, gateway_done='sdk' in vias) with source evaluation/in-place semantics. Then Apply source augmented assignment out += _remediate_checks(cfg) with source evaluation/in-place semantics. Then Apply source augmented assignment out += _validate_checks(cfg) with source evaluation/in-place semantics.
  // Source: vvaharness/util/environment.py:596-596
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:599-611
// Source signature: remediation_inputs_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn remediation_inputs_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:600-603
  In source order: Retain source documentation literal source_literal_600_4; it is not a model call. Then Resolve source import from vvaharness.remediation_agent import rule_paths; preserve alias and import-time effects. Then Evaluate once rule_paths.missing_rules(rule_paths.__file__); assign in source target order to missing. Then Evaluate once rule_paths.configured_inputs_dir(); assign in source target order to configured.
  // Source: vvaharness/util/environment.py:604-607
  if (the source predicate not missing is truthy) {
    // Source: vvaharness/util/environment.py:605-606
    In source order: Evaluate once source_template_605_18 if configured else 'bundled policy and playbook available'; assign in source target order to detail.
    // Source: vvaharness/util/environment.py:607-607
    End this invocation with Check('remediation inputs', OK, detail).
  }
  // Source: vvaharness/util/environment.py:608-611
  End this invocation with Check('remediation inputs', FAIL, source_template_610_8, required=True).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:614-636
// Source signature: _backend_credential_ok(via: str, model_id: str='', provider: str | None=None, *, cfg: object | None=None) -> tuple[bool, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _backend_credential_ok(via, model_id, provider, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:618-618
  In source order: Retain source documentation literal source_literal_618_4; it is not a model call.
  // Source: vvaharness/util/environment.py:620-623
  if (the source predicate via == 'cli' is truthy) {
    // Source: vvaharness/util/environment.py:621-622
    if (the source predicate shutil.which('claude') is truthy) {
      // Source: vvaharness/util/environment.py:622-622
      End this invocation with (True, '`claude` CLI on PATH').
    }
    // Source: vvaharness/util/environment.py:623-623
    End this invocation with (False, '`claude` CLI not on PATH').
  }
  // Source: vvaharness/util/environment.py:624-629
  if (the source predicate via == 'sdk' is truthy) {
    // Source: vvaharness/util/environment.py:625-627
    if (the source predicate _is_set('ANTHROPIC_SDK_API_KEY') or _is_set('ANTHROPIC_API_KEY') or _is_set('ANTHROPIC_AUTH_TOKEN') is truthy) {
      // Source: vvaharness/util/environment.py:627-627
      End this invocation with (True, 'Anthropic SDK credential present').
    }
    // Source: vvaharness/util/environment.py:628-629
    End this invocation with (False, 'ANTHROPIC_SDK_API_KEY not set (or ANTHROPIC_API_KEY/ANTHROPIC_AUTH_TOKEN)').
  }
  // Source: vvaharness/util/environment.py:630-633
  if (the source predicate via == 'openai' is truthy) {
    // Source: vvaharness/util/environment.py:631-632
    if (the source predicate _is_set('OPENAI_API_KEY') is truthy) {
      // Source: vvaharness/util/environment.py:632-632
      End this invocation with (True, 'OPENAI_API_KEY set').
    }
    // Source: vvaharness/util/environment.py:633-633
    End this invocation with (False, 'OPENAI_API_KEY not set').
  }
  // Source: vvaharness/util/environment.py:634-635
  if (the source predicate via == 'deepagents' is truthy) {
    // Source: vvaharness/util/environment.py:635-635
    End this invocation with _deepagents_credential_ok(model_id, provider, cfg).
  }
  // Source: vvaharness/util/environment.py:636-636
  End this invocation with (True, source_template_636_17).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:639-641
// Source signature: _cfg_api_key_present(cfg: object | None, block: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cfg_api_key_present(cfg, block) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:640-640
  In source order: Retain source documentation literal source_literal_640_4; it is not a model call.
  // Source: vvaharness/util/environment.py:641-641
  End this invocation with bool(getattr(getattr(cfg, block, None), 'api_key', None)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:644-657
// Source signature: _deepagents_credential_ok(model_id: str, provider: str | None, cfg: object | None) -> tuple[bool, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deepagents_credential_ok(model_id, provider, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:647-647
  In source order: Retain source documentation literal source_literal_647_4; it is not a model call.
  // Source: vvaharness/util/environment.py:649-653
  if (the source predicate not routes_to_anthropic(model_id, provider) is truthy) {
    // Source: vvaharness/util/environment.py:650-651
    if (the source predicate _cfg_api_key_present(cfg, 'openai') or _is_set('OPENAI_API_KEY') is truthy) {
      // Source: vvaharness/util/environment.py:651-651
      End this invocation with (True, 'OpenAI-compatible DeepAgents credential present').
    }
    // Source: vvaharness/util/environment.py:652-653
    End this invocation with (False, 'OPENAI_API_KEY not set (set OPENAI_BASE_URL for a custom endpoint)').
  }
  // Source: vvaharness/util/environment.py:654-656
  if (the source predicate _cfg_api_key_present(cfg, 'sdk') or _is_set('ANTHROPIC_API_KEY') or _is_set('ANTHROPIC_AUTH_TOKEN') is truthy) {
    // Source: vvaharness/util/environment.py:656-656
    End this invocation with (True, 'Anthropic-compatible DeepAgents credential present').
  }
  // Source: vvaharness/util/environment.py:657-657
  End this invocation with (False, 'ANTHROPIC_API_KEY or ANTHROPIC_AUTH_TOKEN not set').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:660-671
// Source signature: _deepagents_targets(nodes: dict[str, object]) -> dict[tuple[str, str | None], set[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deepagents_targets(nodes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:663-665
  In source order: Retain source documentation literal source_literal_663_4; it is not a model call. Then For targets, assign {}; source annotation dict[tuple[str, str | None], set[str]].
  // Source: vvaharness/util/environment.py:666-670
  for each (role, node) in nodes.items() {
    // Source: vvaharness/util/environment.py:667-668
    if (the source predicate (getattr(node, 'via', None) or 'cli') != 'deepagents' is truthy) {
      // Source: vvaharness/util/environment.py:668-668
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/util/environment.py:669-670
    In source order: Evaluate once (str(getattr(node, 'id', '') or ''), getattr(node, 'provider', None)); assign in source target order to key. Then Evaluate targets.setdefault(key, set()).add(role); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:671-671
  End this invocation with targets.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:674-699
// Source signature: _deepagents_checks(nodes: dict[str, object], *, cfg: object | None, gateway_done: bool) -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deepagents_checks(nodes, cfg, gateway_done) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:676-680
  In source order: Retain source documentation literal source_literal_676_4; it is not a model call. Then For out, assign []; source annotation list[Check]. Then Evaluate once False; assign in source target order to anthropic_route. Then Evaluate once _deepagents_targets(nodes); assign in source target order to targets.
  // Source: vvaharness/util/environment.py:682-693
  for each ((model_id, provider), roles) in sorted(targets.items(), key=lambda kv: (kv[0][0], kv[0][1] or '')) {
    // Source: vvaharness/util/environment.py:684-693
    In source order: Evaluate once anthropic_route or routes_to_anthropic(model_id, provider); assign in source target order to anthropic_route. Then Evaluate once _backend_credential_ok('deepagents', model_id, provider, cfg=cfg); assign in source target order to (ready, detail). Then Evaluate once not roles <= POST_SCAN_ROLES; assign in source target order to blocking. Then Evaluate once OK if ready else FAIL if blocking else WARN; assign in source target order to status. Then Evaluate out.append(Check(source_template_690_12, status, detail + ('' if ready else source_template_691_39), required=blocking and (not ready))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:694-698
  if (the source predicate anthropic_route and (not gateway_done) is truthy) {
    // Source: vvaharness/util/environment.py:696-698
    In source order: Evaluate once _gateway_check(); assign in source target order to gw. Then Evaluate out.append(Check('via:deepagents endpoint', gw.status, gw.detail, required=gw.required)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:699-699
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:702-717
// Source signature: _remediate_checks(cfg) -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _remediate_checks(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:703-703
  In source order: Retain source documentation literal source_literal_703_4; it is not a model call.
  // Source: vvaharness/util/environment.py:705-706
  if (the source predicate not getattr(getattr(cfg, 'step_remediate', None), 'enabled', False) is truthy) {
    // Source: vvaharness/util/environment.py:706-706
    End this invocation with [].
  }
  // Source: vvaharness/util/environment.py:707-707
  In source order: Evaluate once getattr(getattr(cfg, 'models', None), 'remediate', None); assign in source target order to rem.
  // Source: vvaharness/util/environment.py:708-711
  if (the source predicate rem is None is truthy) {
    // Source: vvaharness/util/environment.py:709-711
    End this invocation with [Check('step10: remediate', WARN, 'step_remediate.enabled but models.remediate is unset — remediation will be skipped')].
  }
  // Source: vvaharness/util/environment.py:712-714
  In source order: Evaluate once getattr(rem, 'via', 'cli'); assign in source target order to via. Then Evaluate once _backend_credential_ok(via, getattr(rem, 'id', ''), getattr(rem, 'provider', None), cfg=cfg); assign in source target order to (ready, detail).
  // Source: vvaharness/util/environment.py:715-717
  End this invocation with [Check('step10: remediate', OK if ready else WARN, source_template_716_18 + ('' if ready else ' — remediation will be skipped'))].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:720-746
// Source signature: _validate_checks(cfg) -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_checks(cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:721-721
  In source order: Retain source documentation literal source_literal_721_4; it is not a model call.
  // Source: vvaharness/util/environment.py:723-724
  if (the source predicate not getattr(getattr(cfg, 'step_validate', None), 'enabled', False) is truthy) {
    // Source: vvaharness/util/environment.py:724-724
    End this invocation with [].
  }
  // Source: vvaharness/util/environment.py:725-726
  In source order: For out, assign []; source annotation list[Check]. Then Evaluate once validate_model_spec(cfg); assign in source target order to val.
  // Source: vvaharness/util/environment.py:727-739
  if (the source predicate val is None is truthy) {
    // Source: vvaharness/util/environment.py:728-730
    In source order: Evaluate out.append(Check('step11: validate', WARN, 'step_validate.enabled but models.validate.orchestrator is unset — validation will be skipped')); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/util/environment.py:732-739
    In source order: Evaluate once getattr(val, 'via', 'cli'); assign in source target order to raw_via. Then Evaluate once normalize_validate_backend(raw_via, getattr(val, 'provider', None)); assign in source target order to (via, provider). Then Evaluate once _backend_credential_ok(via, getattr(val, 'id', ''), provider, cfg=cfg); assign in source target order to (ready, detail). Then Evaluate once source_template_736_17 if via != raw_via else ''; assign in source target order to routed. Then Evaluate out.append(Check('step11: validate', OK if ready else WARN, source_template_738_25 + ('' if ready else ' — validation will be skipped'))); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:740-745
  if (the source predicate importlib.util.find_spec('claude_agent_sdk') is not None is truthy) {
    // Source: vvaharness/util/environment.py:741-742
    In source order: Evaluate out.append(Check('step11: claude_agent_sdk', OK, 'claude_agent_sdk importable')); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/util/environment.py:744-745
    In source order: Evaluate out.append(Check('step11: claude_agent_sdk', WARN, 'claude_agent_sdk missing — reinstall vvaharness (pip install .)')); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:746-746
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:749-788
// Source signature: tls_check() -> Check
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn tls_check() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:750-755
  In source order: Retain source documentation literal source_literal_750_4; it is not a model call. Then Evaluate once os.environ.get('ANTHROPIC_BASE_URL') or 'https://api.anthropic.com'; assign in source target order to base. Then Evaluate once urlparse(base if '://' in base else source_template_753_44); assign in source target order to u. Then Evaluate once (u.hostname or 'api.anthropic.com', u.port or 443); assign in source target order to (host, port). Then Evaluate once os.environ.get('NODE_EXTRA_CA_CERTS'); assign in source target order to cafile.
  // Source: vvaharness/util/environment.py:756-756
  In source order: Evaluate once bool(cafile and Path(cafile).is_file()); assign in source target order to use_bundle.
  // Source: vvaharness/util/environment.py:757-788
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:758-758
    In source order: Evaluate once ssl.create_default_context(cafile=cafile if use_bundle else None); assign in source target order to ctx.
    // Source: vvaharness/util/environment.py:759-761
    Enter source context managers left-to-right: socket.create_connection((host, port), timeout=8) bound to sock {
      // Source: vvaharness/util/environment.py:760-761
      Enter source context managers left-to-right: ctx.wrap_socket(sock, server_hostname=host) {
        // Source: vvaharness/util/environment.py:761-761
        In source order: Perform no operation at this source statement.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    // Source: vvaharness/util/environment.py:763-766
    In source order: Evaluate once source_literal_763_15 if use_bundle else ' (system trust store)'; assign in source target order to src.
    // Source: vvaharness/util/environment.py:767-769
    End this invocation with Check('TLS / CA cert', OK, source_template_768_21 if not use_bundle else source_template_769_44).
  }
  // Source: vvaharness/util/environment.py:770-784
  On the first matching source exception ssl.SSLCertVerificationError, in handler order {
    // Source: vvaharness/util/environment.py:772-779
    In source order: Evaluate once detect_ca_cert(); assign in source target order to ca. Then Evaluate once source_template_773_17 if ca else source_literal_777_16; assign in source target order to hint.
    // Source: vvaharness/util/environment.py:780-784
    End this invocation with Check('TLS / CA cert', WARN, source_template_781_21).
  }
  // Source: vvaharness/util/environment.py:785-788
  On the first matching source exception Exception as e, in handler order {
    // Source: vvaharness/util/environment.py:786-788
    End this invocation with Check('TLS / CA cert', WARN, source_template_787_21).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:791-794
// Source signature: _handshake(ctx: ssl.SSLContext, host: str, port: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _handshake(ctx, host, port) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:792-794
  Enter source context managers left-to-right: socket.create_connection((host, port), timeout=8) bound to sock {
    // Source: vvaharness/util/environment.py:793-794
    Enter source context managers left-to-right: ctx.wrap_socket(sock, server_hostname=host) {
      // Source: vvaharness/util/environment.py:794-794
      In source order: Perform no operation at this source statement.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:797-815
// Source signature: _client_trust(sdk_cfg: object | None, cfg_path: str | Path) -> tuple[ssl.SSLContext, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _client_trust(sdk_cfg, cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:798-800
  In source order: Retain source documentation literal source_literal_798_4; it is not a model call. Then Evaluate once getattr(sdk_cfg, 'ca_cert', None); assign in source target order to ca.
  // Source: vvaharness/util/environment.py:801-805
  if (the source predicate ca is truthy) {
    // Source: vvaharness/util/environment.py:802-803
    In source order: Resolve source import from vvaharness.orchestrator.config_paths import _resolve_against; preserve alias and import-time effects. Then Evaluate once _resolve_against(Path(cfg_path).resolve().parent, str(ca)); assign in source target order to path.
    // Source: vvaharness/util/environment.py:804-805
    if (the source predicate Path(path).is_file() is truthy) {
      // Source: vvaharness/util/environment.py:805-805
      End this invocation with (ssl.create_default_context(cafile=path), 'sdk.ca_cert').
    }
  }
  // Source: vvaharness/util/environment.py:806-810
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:807-808
    In source order: Resolve source import import httpx2; preserve alias and import-time effects. Then Evaluate once httpx2.create_ssl_context(verify=True, trust_env=True); assign in source target order to ctx.
  }
  // Source: vvaharness/util/environment.py:809-810
  On the first matching source exception ImportError, in handler order {
    // Source: vvaharness/util/environment.py:810-810
    In source order: Evaluate once ssl.create_default_context(cafile=os.environ.get('SSL_CERT_FILE') or None); assign in source target order to ctx.
  }
  // Source: vvaharness/util/environment.py:811-812
  if (the source predicate os.environ.get('SSL_CERT_FILE') is truthy) {
    // Source: vvaharness/util/environment.py:812-812
    End this invocation with (ctx, 'SSL_CERT_FILE').
  }
  // Source: vvaharness/util/environment.py:813-814
  if (the source predicate os.environ.get('SSL_CERT_DIR') is truthy) {
    // Source: vvaharness/util/environment.py:814-814
    End this invocation with (ctx, 'SSL_CERT_DIR').
  }
  // Source: vvaharness/util/environment.py:815-815
  End this invocation with (ctx, 'the OS trust store').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:818-868
// Source signature: client_tls_check(cfg_path: str | Path) -> Check | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn client_tls_check(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:819-819
  In source order: Retain source documentation literal source_literal_819_4; it is not a model call.
  // Source: vvaharness/util/environment.py:821-825
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:822-823
    In source order: Evaluate once config_mod.load(Path(cfg_path)); assign in source target order to cfg. Then Evaluate once dict(_iter_model_roles(cfg)); assign in source target order to nodes.
  }
  // Source: vvaharness/util/environment.py:824-825
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/util/environment.py:825-825
    End this invocation with None.
  }
  // Source: vvaharness/util/environment.py:826-830
  In source order: Evaluate once {role for role, node in nodes.items() if (getattr(node, 'via', None) or 'cli') == 'sdk' or ((getattr(node, 'via', None) or 'cli') == 'deepagents' and routes_to_anthropic(str(getattr(node, 'id', '') or ''), getattr(node, 'provider', None)))}; assign in source target order to roles.
  // Source: vvaharness/util/environment.py:831-832
  if (the source predicate not roles is truthy) {
    // Source: vvaharness/util/environment.py:832-832
    End this invocation with None.
  }
  // Source: vvaharness/util/environment.py:833-837
  In source order: Evaluate once getattr(cfg, 'sdk', None); assign in source target order to sdk_cfg. Then Evaluate once getattr(sdk_cfg, 'base_url', None) or os.environ.get('ANTHROPIC_BASE_URL') or 'https://api.anthropic.com'; assign in source target order to base. Then Evaluate once urlparse(str(base) if '://' in str(base) else source_template_836_54); assign in source target order to u. Then Evaluate once (u.hostname or 'api.anthropic.com', u.port or 443); assign in source target order to (host, port).
  // Source: vvaharness/util/environment.py:838-847
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:839-840
    In source order: Evaluate once _client_trust(sdk_cfg, cfg_path); assign in source target order to (ctx, source). Then Evaluate _handshake(ctx, host, port); retain side effects and discard the expression result.
    // Source: vvaharness/util/environment.py:841-843
    End this invocation with Check('TLS / client trust', OK, source_template_842_21).
  }
  // Source: vvaharness/util/environment.py:844-845
  On the first matching source exception ssl.SSLCertVerificationError, in handler order {
    // Source: vvaharness/util/environment.py:845-845
    In source order: Perform no operation at this source statement.
  }
  // Source: vvaharness/util/environment.py:846-847
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/util/environment.py:847-847
    End this invocation with None.
  }
  // Source: vvaharness/util/environment.py:849-850
  In source order: Evaluate once not roles <= POST_SCAN_ROLES; assign in source target order to blocking. Then Evaluate once os.environ.get('NODE_EXTRA_CA_CERTS'); assign in source target order to node_ca.
  // Source: vvaharness/util/environment.py:851-860
  Perform the following protected operations {
    // Source: vvaharness/util/environment.py:852-853
    if (the source predicate not (node_ca and Path(node_ca).is_file()) is truthy) {
      // Source: vvaharness/util/environment.py:853-853
      Raise ssl.SSLError('no NODE_EXTRA_CA_CERTS bundle').
    }
    // Source: vvaharness/util/environment.py:854-854
    In source order: Evaluate _handshake(ssl.create_default_context(cafile=node_ca), host, port); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:855-860
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/util/environment.py:856-860
    End this invocation with Check('TLS / client trust', WARN, source_template_857_21).
  }
  // Source: vvaharness/util/environment.py:861-868
  End this invocation with Check('TLS / client trust', FAIL if blocking else WARN, source_template_863_8, required=blocking).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:871-893
// Source signature: run_checks(cfg_path: str | Path) -> list[Check]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_checks(cfg_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:872-879
  In source order: Retain source documentation literal source_literal_872_4; it is not a model call. Then For checks, assign [python_check(), tool_check('git', 'batch --repo-file cloning'), tool_check('pip3', 'installing optional extras')]; source annotation list[Check]. Then Apply source augmented assignment checks += agent_checks() with source evaluation/in-place semantics. Then Apply source augmented assignment checks += credential_checks() with source evaluation/in-place semantics. Then Evaluate checks.append(langsmith_tracing_check()); retain side effects and discard the expression result.
  // Source: vvaharness/util/environment.py:880-883
  In source order: Apply source augmented assignment checks += dep_checks() with source evaluation/in-place semantics. Then Evaluate checks.append(anthropic_version_check()); retain side effects and discard the expression result. Then Evaluate checks.append(tls_check()); retain side effects and discard the expression result. Then Evaluate once client_tls_check(cfg_path); assign in source target order to client_tls.
  // Source: vvaharness/util/environment.py:884-885
  if (the source predicate client_tls is not None is truthy) {
    // Source: vvaharness/util/environment.py:885-885
    In source order: Evaluate checks.append(client_tls); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/environment.py:886-887
  In source order: Evaluate checks.append(remediation_inputs_check()); retain side effects and discard the expression result. Then Evaluate once config_check(cfg_path); assign in source target order to cfg_checks.
  // Source: vvaharness/util/environment.py:888-892
  if (the source predicate cfg_checks is truthy) {
    // Source: vvaharness/util/environment.py:889-892
    In source order: Evaluate checks.append(cfg_checks[0]); retain side effects and discard the expression result. Then Evaluate checks.append(dotenv_check()); retain side effects and discard the expression result. Then Evaluate checks.append(overlay_check(cfg_path)); retain side effects and discard the expression result. Then Apply source augmented assignment checks += cfg_checks[1:] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/util/environment.py:893-893
  End this invocation with checks.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/environment.py:896-901
// Source signature: summarize(checks: list[Check]) -> tuple[int, int, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn summarize(checks) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/environment.py:897-900
  In source order: Retain source documentation literal source_literal_897_4; it is not a model call. Then Evaluate once sum((1 for c in checks if c.status == OK)); assign in source target order to n_ok. Then Evaluate once sum((1 for c in checks if c.status == WARN)); assign in source target order to n_warn. Then Evaluate once sum((1 for c in checks if c.status == FAIL and c.required)); assign in source target order to n_blocking.
  // Source: vvaharness/util/environment.py:901-901
  End this invocation with (n_ok, n_warn, n_blocking).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness import config as config_mod` at source line 32: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 32: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.provider_routing import routes_to_anthropic` at source line 33: `source_detail/vvaharness/backends/harness/provider_routing.py.sudo.md`.
- `from vvaharness.backends.llm.registry import DEEPAGENTS_ROLES, POST_SCAN_ROLES, unrecognized_model_keys` at source line 34: `source_detail/vvaharness/backends/llm/registry.py.sudo.md`.
- `from vvaharness.config.constants import LOCAL_OVERLAY_NAME, NO_LOCAL_CONFIG_ENV` at source line 39: `source_detail/vvaharness/config/constants.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _iter_model_roles` at source line 40: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.
- `from vvaharness.validation.config.validate_role import normalize_validate_backend, validate_model_spec` at source line 41: `source_detail/vvaharness/validation/config/validate_role.py.sudo.md`.
- `from vvaharness.cli import _dotenv_selection` at source line 435: `source_detail/vvaharness/cli/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import rule_paths` at source line 601: `source_detail/vvaharness/remediation_agent/__init__.py.sudo.md`.
- `from vvaharness.remediation_agent import rule_paths` at source line 601: `source_detail/vvaharness/remediation_agent/rule_paths.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 503: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import config as config_mod` at source line 503: `source_detail/vvaharness/config/__init__.py.sudo.md`.
- `from vvaharness.orchestrator.config_paths import _resolve_against` at source line 802: `source_detail/vvaharness/orchestrator/config_paths.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/util/environment.py.sudo.md). Exact strings in the evidence asset support this conversion.
