# vvaharness/config/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/config/__init__.py.evidence.json`. SHA-256: `dd6175165204eaa18c04aaf60172be1399cd901dcd7bfb21181462d1d568200b`.

```sudo
// Source: vvaharness/config/__init__.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import stat; preserve alias and import-time effects.
// Source: vvaharness/config/__init__.py:21-34
In source order: Resolve source import from pathlib import Path, PureWindowsPath; preserve alias and import-time effects. Then Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from urllib.parse import urlsplit; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects. Then Resolve source import from vvaharness.config.constants import CREDENTIAL_DESTINATIONS, ENDPOINT_KEYS, LOCAL_OVERLAY_NAME, NO_LOCAL_CONFIG_ENV, TLS_ROUTING_KEYS, is_secret_var_name; preserve alias and import-time effects.
// Source: vvaharness/config/__init__.py:35-37
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once re.compile('\\$\\{([A-Z_][A-Z0-9_]*)(?::-([^}]*))?\\}'); assign in source target order to _ENV_PAT.
// Source: vvaharness/config/__init__.py:40-41
interface ConfigPolicyError {
  Describe the source Python type, preserving its base/metaclass expression order: ValueError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/config/__init__.py:41-41
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call.
}
// Source: vvaharness/config/__init__.py:44-52
interface ConfigPathError {
  Describe the source Python type, preserving its base/metaclass expression order: ConfigPolicyError.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/config/__init__.py:45-52
  In source order: Retain source documentation literal source_literal_45_4; it is not a model call.
}
// Source: vvaharness/config/__init__.py:58-58
In source order: For _logged_overlays, assign set(); source annotation set[str].
// Source: vvaharness/config/__init__.py:61-78
// Source signature: _expand_env(m: re.Match[str], path: tuple[str, ...]) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _expand_env(m, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:62-63
  In source order: Evaluate once (m.group(1), m.group(2)); assign in source target order to (name, default). Then Evaluate once '.'.join(path); assign in source target order to key_path.
  // Source: vvaharness/config/__init__.py:66-73
  if (the source predicate is_secret_var_name(name) and key_path not in CREDENTIAL_DESTINATIONS is truthy) {
    // Source: vvaharness/config/__init__.py:67-67
    In source order: Evaluate once ', '.join(sorted(CREDENTIAL_DESTINATIONS)); assign in source target order to allowed.
    // Source: vvaharness/config/__init__.py:68-73
    Raise ConfigPolicyError(source_template_69_12).
  }
  // Source: vvaharness/config/__init__.py:75-75
  In source order: Evaluate once os.environ.get(name); assign in source target order to val.
  // Source: vvaharness/config/__init__.py:76-77
  if (the source predicate val is truthy) {
    // Source: vvaharness/config/__init__.py:77-77
    End this invocation with val.
  }
  // Source: vvaharness/config/__init__.py:78-78
  End this invocation with default if default is not None else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:81-88
// Source signature: _expand(val: object, path: tuple[str, ...]=()) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _expand(val, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:82-83
  if (the source predicate isinstance(val, str) is truthy) {
    // Source: vvaharness/config/__init__.py:83-83
    End this invocation with _ENV_PAT.sub(lambda m: _expand_env(m, path), val).
  }
  // Source: vvaharness/config/__init__.py:84-85
  if (the source predicate isinstance(val, dict) is truthy) {
    // Source: vvaharness/config/__init__.py:85-85
    End this invocation with {k: _expand(v, (*path, str(k))) for k, v in val.items()}.
  }
  // Source: vvaharness/config/__init__.py:86-87
  if (the source predicate isinstance(val, list) is truthy) {
    // Source: vvaharness/config/__init__.py:87-87
    End this invocation with [_expand(v, path) for v in val].
  }
  // Source: vvaharness/config/__init__.py:88-88
  End this invocation with val.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:91-93
// Source signature: _expand_tree(tree: dict, path: tuple[str, ...]=()) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _expand_tree(tree, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:93-93
  End this invocation with {k: _expand(v, (*path, str(k))) for k, v in tree.items()}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:96-118
interface Config {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/config/__init__.py:97-97
  In source order: Retain source documentation literal source_literal_97_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:98-99
  // Source signature: __init__(self, data: dict)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, data) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/config/__init__.py:99-99
    In source order: Evaluate once data; assign in source target order to self._data.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/config/__init__.py:101-112
  // Source signature: __getattr__(self, name)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __getattr__(self, name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/config/__init__.py:105-106
    if (the source predicate name.startswith('__') and name.endswith('__') or name == '_data' is truthy) {
      // Source: vvaharness/config/__init__.py:106-106
      Raise AttributeError(name).
    }
    // Source: vvaharness/config/__init__.py:107-107
    In source order: Evaluate once self.__dict__.get('_data'); assign in source target order to data.
    // Source: vvaharness/config/__init__.py:108-111
    Perform the following protected operations {
      // Source: vvaharness/config/__init__.py:109-109
      In source order: Evaluate once data[name]; assign in source target order to v.
    }
    // Source: vvaharness/config/__init__.py:110-111
    On the first matching source exception (KeyError, TypeError) as e, in handler order {
      // Source: vvaharness/config/__init__.py:111-111
      Raise AttributeError(name) with explicit source cause e.
    }
    // Source: vvaharness/config/__init__.py:112-112
    End this invocation with Config(v) if isinstance(v, dict) else v.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/config/__init__.py:114-115
  // Source signature: __getitem__(self, k)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __getitem__(self, k) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/config/__init__.py:115-115
    End this invocation with self._data[k].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/config/__init__.py:117-118
  // Source signature: __repr__(self)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __repr__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/config/__init__.py:118-118
    End this invocation with source_template_118_15.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/config/__init__.py:121-128
// Source signature: _deep_merge(base: dict, over: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _deep_merge(base, over) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:122-122
  In source order: Evaluate once dict(base); assign in source target order to out.
  // Source: vvaharness/config/__init__.py:123-127
  for each (k, v) in over.items() {
    // Source: vvaharness/config/__init__.py:124-127
    if (the source predicate isinstance(v, dict) and isinstance(out.get(k), dict) is truthy) {
      // Source: vvaharness/config/__init__.py:125-125
      In source order: Evaluate once _deep_merge(out[k], v); assign in source target order to out[k].
    }
    else {
      // Source: vvaharness/config/__init__.py:127-127
      In source order: Evaluate once v; assign in source target order to out[k].
    }
  }
  // Source: vvaharness/config/__init__.py:128-128
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:147-713
In source order: For _STEP_DEFAULTS, assign {'step0': {'callgraph_detection': 'rules', 'languages': None, 'min_graph_nodes_for_gate': 10}, 'step1': {'max_file_kb': 1024, 'auto_exclude': False, 'auto_exclude_max_tokens': 8000, 'auto_exclude_effort': 'high', 'auto_exclude_protect_templates': True, 'auto_exclude_protect_key_material': True, 'auto_exclude_protect_secrets': True, 'auto_exclude_protect_client_sinks': True, 'follow_symlinks': False}, 'step2': {'max_tokens': 64000, 'max_threats': 50, 'empty_retry': True, 'baseline': 'auto', 'max_doc_chars': 20000, 'max_manifest_chars': 4000, 'max_modules': 100, 'max_entry_points': 400, 'max_config_reps': 80, 'max_api_artefacts': 100, 'max_graph_files': 220, 'max_graph_sinks': 80, 'max_graph_edges': 100, 'max_prompt_modules': 100, 'max_prompt_entry_points': 400, 'max_inventory_files': 1200, 'bash': False, 'timeout': 1800, 'max_assets': 40, 'max_trust_boundaries': 60, 'max_manifest_depth': 3, 'max_manifests': 12, 'max_manifests_per_kind': 2, 'max_manifest_total_chars': 24000, 'max_config_rep_chars': 2000, 'max_config_rep_bodies': 12, 'allowed_tools': ('Read', 'Grep'), 'max_turns': 12, 'graph_tools': True, 'graph_tool_budget': 6, 'require_graph': True, 'require_graph_rejections': 2, 'planning': True, 'skills': True, 'effort': 'high', 'deadline': 400, 'replay_timeout': 300, 'replay_max_tokens': 16000, 'resume_timeout': 300, 'max_model_calls': 0}, 'step3': {}, 'step4': {'parallel': 12, 'max_turns': 15, 'deadline': 400, 'replay_timeout': 60, 'replay_max_tokens': 16000, 'resume_timeout': 60, 'max_model_calls': 0, 'batch_size': 1, 'split_retry': True, 'allowed_tools': ('Read', 'Glob', 'Grep'), 'bash': False, 'line_bucket': 10, 'max_findings_per_run': 10, 'max_tokens': 64000, 'cwe_tools': True, 'cwe_tool_budget': 6, 'graph_tool_budget': 6, 'planning': True, 'inline_source': False, 'evidence_gate': True, 'evidence_gate_refusals': 3, 'skills': True, 'effort': 'high', 'require_graph': True, 'max_extra_cwes': 2}, 'step5_prefilter': {'sink_reanchor': True, 'sink_reanchor_max_move_lines': 40}, 'step5_detectors': {'enabled': True, 'max_rows': 200}, 'step6_verify': {'max_tokens': 32000, 'parallel': 5, 'min_confidence': 7, 'max_budget_usd': 10.0, 'tool_timeout_s': None, 'max_turns': 20, 'batch_size': 12, 'inline_source': True, 'graph_tools': True, 'graph_tool_budget': 4, 'require_graph': False, 'evidence_gate_refusals': 3, 'max_model_calls': 0, 'batch_wall_clock_ceiling': 900, 'batch_deadline': 400, 'replay_timeout': 60, 'replay_max_tokens': 12000, 'resume_timeout': 60, 'trait_stamps': True, 'reframe_enabled': False, 'split_retry': True, 'effort': 'high', 'progress_file': False}, 'step6_exploit_verification': {'enabled': 'auto', 'on_unreachable': 'drop', 'ev_overrides_static': False, 'parallel': 4, 'store_probes': False, 'timeout_s': 15, 'safe_mode': True, 'allow_state_changing_methods': False, 'rate_limit_rps': 0, 'max_concurrency_target': 8, 'max_concurrency_endpoint': 4, 'max_requests_per_finding': 20, 'max_payloads_per_finding': 15, 'oob': 'auto', 'on_auth_failure': 'degrade', 'auth_expiry_skew_s': 60, 'max_reauth': 3, 'ev_replay_variants': True, 'classify': {'batch': 10, 'parallel': 4, 'effort': 'high'}, 'mapper': {'max_turns': 20, 'parallel': 4, 'effort': 'high', 'endpoint_index': {'chunk': 20}, 'finding_map': {'chunk': 6, 'max_endpoints': 5}}, 'attacker': {'enabled': True, 'max_turns': 15, 'max_tool_result_chars': 12000, 'effort': 'high'}, 'judge': {'max_tokens': 4000, 'max_records': 24, 'effort': 'high'}}, 'step7_dedup': {'line_tolerance': 3, 'semantic': False, 'max_tokens': 64000, 'effort': 'high', 'per_sink_keep': True}, 'step8': {'max_tokens': 64000, 'timeout': 3600, 'effort': 'high', 'prompt_token_budget': 100000, 'max_model_calls': 1, 'max_turns': 2, 'deadline': 600, 'replay_timeout': 300, 'replay_max_tokens': 16000, 'resume_timeout': 300, 'hop_text': False, 'severity_lift_gate': True, 'chain_quality_checks': True, 'chain_dedup': True, 'prompt_fact_blocks': True}, 'step9': {'duplicate_result_guard': True}, 'step_remediate': {'max_budget_usd': 10.0, 'max_turns': 40, 'max_model_calls': 20, 'timeout': 3600, 'top_n_findings': 20, 'policy_file': None, 'playbook_file': None}, 'step_validate': {'enabled': False, 'effort': 'high', 'max_turns': 50, 'max_budget_usd': 15.0, 'max_findings': 20, 'timeout': 3600, 'max_model_calls': 60, 'orchestrator_max_model_calls': 40}, 'output': {'emit_unreachable_appendix': False, 'posture_channel': True}, 'cli': {'mcp_tools': True, 'restricted': True}, 'cache_min_block_tokens': None, 'cache_markers': 'on', 'cache_route': 'auto', 'think_in_prompt': True, 'refusal_retries': 1, 'pricing': {'file': None}}; source annotation dict.
// Source: vvaharness/config/__init__.py:716-727
// Source signature: _local_overlay_trusted(path: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _local_overlay_trusted(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:717-717
  In source order: Retain source documentation literal source_literal_717_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:718-721
  Perform the following protected operations {
    // Source: vvaharness/config/__init__.py:719-719
    In source order: Evaluate once path.stat(); assign in source target order to st.
  }
  // Source: vvaharness/config/__init__.py:720-721
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/config/__init__.py:721-721
    End this invocation with False.
  }
  // Source: vvaharness/config/__init__.py:722-722
  In source order: Evaluate once getattr(os, 'geteuid', None); assign in source target order to get_euid.
  // Source: vvaharness/config/__init__.py:725-726
  if (the source predicate get_euid is not None and st.st_uid not in (get_euid(), 0) is truthy) {
    // Source: vvaharness/config/__init__.py:726-726
    End this invocation with False.
  }
  // Source: vvaharness/config/__init__.py:727-727
  End this invocation with get_euid is None or not st.st_mode & (stat.S_IWGRP | stat.S_IWOTH).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:730-743
// Source signature: _require_overlay_trust(local: Path, log_overlay: bool) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _require_overlay_trust(local, log_overlay) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:731-731
  In source order: Retain source documentation literal source_literal_731_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:732-736
  if (the source predicate getattr(os, 'geteuid', None) is None is truthy) {
    // Source: vvaharness/config/__init__.py:733-735
    if (the source predicate log_overlay is truthy) {
      // Source: vvaharness/config/__init__.py:734-735
      In source order: Evaluate console.write(source_template_734_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/config/__init__.py:736-736
    End this invocation with None.
  }
  // Source: vvaharness/config/__init__.py:737-743
  if (the source predicate not _local_overlay_trusted(local) is truthy) {
    // Source: vvaharness/config/__init__.py:738-743
    Raise ConfigPolicyError(source_template_739_12).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:746-764
// Source signature: _local_overlay(local: Path) -> tuple[dict | None, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _local_overlay(local) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:747-747
  In source order: Retain source documentation literal source_literal_747_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:748-749
  if (the source predicate not local.exists() is truthy) {
    // Source: vvaharness/config/__init__.py:749-749
    End this invocation with (None, False).
  }
  // Source: vvaharness/config/__init__.py:750-752
  In source order: Evaluate once str(local.resolve()); assign in source target order to key. Then Evaluate once key not in _logged_overlays; assign in source target order to log_overlay. Then Evaluate _logged_overlays.add(key); retain side effects and discard the expression result.
  // Source: vvaharness/config/__init__.py:753-757
  if (the source predicate os.environ.get(NO_LOCAL_CONFIG_ENV) is truthy) {
    // Source: vvaharness/config/__init__.py:754-756
    if (the source predicate log_overlay is truthy) {
      // Source: vvaharness/config/__init__.py:755-756
      In source order: Evaluate console.write(source_template_755_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/config/__init__.py:757-757
    End this invocation with (None, log_overlay).
  }
  // Source: vvaharness/config/__init__.py:758-759
  In source order: Evaluate _require_overlay_trust(local, log_overlay); retain side effects and discard the expression result. Then Evaluate once yaml.safe_load(local.read_text(encoding='utf-8')) or {}; assign in source target order to over.
  // Source: vvaharness/config/__init__.py:760-763
  if (the source predicate not isinstance(over, dict) is truthy) {
    // Source: vvaharness/config/__init__.py:762-763
    Raise ValueError(source_template_763_12).
  }
  // Source: vvaharness/config/__init__.py:764-764
  End this invocation with (over, log_overlay).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:767-776
// Source signature: _leaf_paths(tree: dict, prefix: tuple[str, ...]=()) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _leaf_paths(tree, prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:768-769
  In source order: Retain source documentation literal source_literal_768_4; it is not a model call. Then For out, assign []; source annotation list[str].
  // Source: vvaharness/config/__init__.py:770-775
  for each (k, v) in tree.items() {
    // Source: vvaharness/config/__init__.py:771-771
    In source order: Evaluate once (*prefix, str(k)); assign in source target order to path.
    // Source: vvaharness/config/__init__.py:772-775
    if (the source predicate isinstance(v, dict) and v is truthy) {
      // Source: vvaharness/config/__init__.py:773-773
      In source order: Evaluate out.extend(_leaf_paths(v, path)); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/config/__init__.py:775-775
      In source order: Evaluate out.append('.'.join(path)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/config/__init__.py:776-776
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:779-785
// Source signature: _resolved_leaf(data: dict, path: str) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolved_leaf(data, path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:780-780
  In source order: For node, assign data; source annotation object.
  // Source: vvaharness/config/__init__.py:781-784
  for each seg in path.split('.') {
    // Source: vvaharness/config/__init__.py:782-783
    if (the source predicate not isinstance(node, dict) is truthy) {
      // Source: vvaharness/config/__init__.py:783-783
      End this invocation with None.
    }
    // Source: vvaharness/config/__init__.py:784-784
    In source order: Evaluate once node.get(seg); assign in source target order to node.
  }
  // Source: vvaharness/config/__init__.py:785-785
  End this invocation with node.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:788-809
// Source signature: _endpoint_display(value: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _endpoint_display(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:789-799
  In source order: Retain source documentation literal source_literal_789_4; it is not a model call. Then Evaluate once str(value or '').strip(); assign in source target order to raw.
  // Source: vvaharness/config/__init__.py:800-801
  if (the source predicate not raw is truthy) {
    // Source: vvaharness/config/__init__.py:801-801
    End this invocation with '(unset)'.
  }
  // Source: vvaharness/config/__init__.py:802-806
  Perform the following protected operations {
    // Source: vvaharness/config/__init__.py:803-804
    In source order: Evaluate once urlsplit(raw if '//' in raw else source_template_803_49); assign in source target order to parts. Then Evaluate once (parts.hostname, parts.port); assign in source target order to (host, port).
  }
  // Source: vvaharness/config/__init__.py:805-806
  On the first matching source exception ValueError, in handler order {
    // Source: vvaharness/config/__init__.py:806-806
    End this invocation with '(unparseable)'.
  }
  // Source: vvaharness/config/__init__.py:807-808
  if (the source predicate not host is truthy) {
    // Source: vvaharness/config/__init__.py:808-808
    End this invocation with '(unparseable)'.
  }
  // Source: vvaharness/config/__init__.py:809-809
  End this invocation with source_template_809_11 if port else host.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:812-824
// Source signature: _override_entry(path: str, resolved: dict) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _override_entry(path, resolved) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:813-814
  In source order: Retain source documentation literal source_literal_813_4; it is not a model call. Then Evaluate once _resolved_leaf(resolved, path); assign in source target order to value.
  // Source: vvaharness/config/__init__.py:815-823
  if (the source predicate path in CREDENTIAL_DESTINATIONS is truthy) {
    // Source: vvaharness/config/__init__.py:816-816
    In source order: Evaluate once source_template_816_16; assign in source target order to entry.
  }
  else {
    // Source: vvaharness/config/__init__.py:817-823
    if (the source predicate path in ENDPOINT_KEYS is truthy) {
      // Source: vvaharness/config/__init__.py:819-819
      In source order: Evaluate once source_template_819_16; assign in source target order to entry.
    }
    else {
      // Source: vvaharness/config/__init__.py:820-823
      if (the source predicate path in TLS_ROUTING_KEYS or path.rsplit('.', 1)[-1] in TLS_ROUTING_KEYS is truthy) {
        // Source: vvaharness/config/__init__.py:821-821
        In source order: Evaluate once source_template_821_16; assign in source target order to entry.
      }
      else {
        // Source: vvaharness/config/__init__.py:823-823
        In source order: Evaluate once path; assign in source target order to entry.
      }
    }
  }
  // Source: vvaharness/config/__init__.py:824-824
  End this invocation with entry.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:827-829
// Source signature: _overlay_override_entries(leaves: list[str], resolved: dict) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _overlay_override_entries(leaves, resolved) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:828-828
  In source order: Retain source documentation literal source_literal_828_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:829-829
  End this invocation with [_override_entry(path, resolved) for path in sorted(leaves)].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:832-836
// Source signature: _path_context(p: Path) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _path_context(p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:833-833
  In source order: Retain source documentation literal source_literal_833_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:834-835
  if (the source predicate p.is_absolute() is truthy) {
    // Source: vvaharness/config/__init__.py:835-835
    End this invocation with ''.
  }
  // Source: vvaharness/config/__init__.py:836-836
  End this invocation with source_template_836_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:839-865
// Source signature: read_primary(path: str | Path) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn read_primary(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:840-841
  In source order: Retain source documentation literal source_literal_840_4; it is not a model call. Then Evaluate once Path(path); assign in source target order to p.
  // Source: vvaharness/config/__init__.py:845-846
  if (the source predicate not p.exists() is truthy) {
    // Source: vvaharness/config/__init__.py:846-846
    Raise ConfigPathError(source_template_846_30).
  }
  // Source: vvaharness/config/__init__.py:847-848
  if (the source predicate not p.is_file() is truthy) {
    // Source: vvaharness/config/__init__.py:848-848
    Raise ConfigPathError(source_template_848_30).
  }
  // Source: vvaharness/config/__init__.py:849-850
  if (the source predicate not os.access(p, os.R_OK) is truthy) {
    // Source: vvaharness/config/__init__.py:850-850
    Raise ConfigPathError(source_template_850_30).
  }
  // Source: vvaharness/config/__init__.py:853-862
  Perform the following protected operations {
    // Source: vvaharness/config/__init__.py:854-854
    In source order: Evaluate once yaml.safe_load(p.read_text(encoding='utf-8')) or {}; assign in source target order to raw.
  }
  // Source: vvaharness/config/__init__.py:855-859
  On the first matching source exception yaml.YAMLError as e, in handler order {
    // Source: vvaharness/config/__init__.py:859-859
    Raise ConfigPathError(source_template_859_30) with explicit source cause e.
  }
  // Source: vvaharness/config/__init__.py:860-862
  On the first matching source exception UnicodeDecodeError as e, in handler order {
    // Source: vvaharness/config/__init__.py:862-862
    Raise ConfigPathError(source_template_862_30) with explicit source cause e.
  }
  // Source: vvaharness/config/__init__.py:863-864
  if (the source predicate not isinstance(raw, dict) is truthy) {
    // Source: vvaharness/config/__init__.py:864-864
    Raise ConfigPathError(source_template_864_30).
  }
  // Source: vvaharness/config/__init__.py:865-865
  End this invocation with raw.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:868-900
// Source signature: load(path: str | Path='config.yaml') -> Config
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:869-885
  In source order: Evaluate once Path(path); assign in source target order to p. Then Evaluate once read_primary(p); assign in source target order to raw. Then Evaluate once _deep_merge(_STEP_DEFAULTS, raw); assign in source target order to raw. Then Evaluate once p.with_name(LOCAL_OVERLAY_NAME); assign in source target order to local. Then Evaluate once _local_overlay(local); assign in source target order to (over, log_overlay).
  // Source: vvaharness/config/__init__.py:886-887
  if (the source predicate over is not None is truthy) {
    // Source: vvaharness/config/__init__.py:887-887
    In source order: Evaluate once _deep_merge(raw, over); assign in source target order to raw.
  }
  // Source: vvaharness/config/__init__.py:888-889
  In source order: Evaluate once _expand_tree(raw); assign in source target order to data. Then Evaluate _check_refusal_retries(data.get('refusal_retries'), p); retain side effects and discard the expression result.
  // Source: vvaharness/config/__init__.py:891-894
  if (the source predicate over is not None and log_overlay is truthy) {
    // Source: vvaharness/config/__init__.py:892-894
    In source order: Evaluate once ', '.join(_overlay_override_entries(_leaf_paths(over), data)) or '(empty)'; assign in source target order to overrides. Then Evaluate console.write(source_template_893_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/config/__init__.py:895-899
  In source order: Evaluate once Config(data); assign in source target order to cfg. Then Evaluate once str(p.resolve().parent); assign in source target order to cfg._data['_config_dir'].
  // Source: vvaharness/config/__init__.py:900-900
  End this invocation with cfg.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:904-904
In source order: For _REFUSAL_RETRIES_MAX, assign 1; source annotation Final.
// Source: vvaharness/config/__init__.py:907-915
// Source signature: _check_refusal_retries(value: object, p: Path) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _check_refusal_retries(value, p) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:908-908
  In source order: Retain source documentation literal source_literal_908_4; it is not a model call.
  // Source: vvaharness/config/__init__.py:910-912
  if (the source predicate value is None or (isinstance(value, int) and (not isinstance(value, bool)) and (0 <= value <= _REFUSAL_RETRIES_MAX)) is truthy) {
    // Source: vvaharness/config/__init__.py:912-912
    End this invocation with None.
  }
  // Source: vvaharness/config/__init__.py:913-915
  Raise ConfigPolicyError(source_template_914_8).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:918-929
// Source signature: _replace_merge(base: dict, over: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _replace_merge(base, over) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:919-922
  In source order: Retain source documentation literal source_literal_919_4; it is not a model call. Then Evaluate once dict(base); assign in source target order to out.
  // Source: vvaharness/config/__init__.py:923-928
  for each (k, v) in over.items() {
    // Source: vvaharness/config/__init__.py:924-924
    In source order: Evaluate once out.get(k); assign in source target order to cur.
    // Source: vvaharness/config/__init__.py:925-928
    if (the source predicate isinstance(v, dict) and isinstance(cur, dict) is truthy) {
      // Source: vvaharness/config/__init__.py:926-926
      In source order: Evaluate once _replace_merge(cur, v); assign in source target order to out[k].
    }
    else {
      // Source: vvaharness/config/__init__.py:928-928
      In source order: Evaluate once v; assign in source target order to out[k].
    }
  }
  // Source: vvaharness/config/__init__.py:929-929
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:932-946
// Source signature: _append_merge(base: dict, over: dict) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _append_merge(base, over) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:933-937
  In source order: Retain source documentation literal source_literal_933_4; it is not a model call. Then Evaluate once dict(base); assign in source target order to out.
  // Source: vvaharness/config/__init__.py:938-945
  for each (k, v) in over.items() {
    // Source: vvaharness/config/__init__.py:939-939
    In source order: Evaluate once out.get(k); assign in source target order to cur.
    // Source: vvaharness/config/__init__.py:940-945
    if (the source predicate isinstance(v, dict) and isinstance(cur, dict) is truthy) {
      // Source: vvaharness/config/__init__.py:941-941
      In source order: Evaluate once _replace_merge(cur, v); assign in source target order to out[k].
    }
    else {
      // Source: vvaharness/config/__init__.py:942-945
      if (the source predicate isinstance(v, list) and isinstance(cur, list) is truthy) {
        // Source: vvaharness/config/__init__.py:943-943
        In source order: Evaluate once list(cur) + [x for x in v if x not in cur]; assign in source target order to out[k].
      }
      else {
        // Source: vvaharness/config/__init__.py:945-945
        In source order: Evaluate once v; assign in source target order to out[k].
      }
    }
  }
  // Source: vvaharness/config/__init__.py:946-946
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:949-960
// Source signature: is_network_path(path: str | Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_network_path(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:950-956
  In source order: Retain source documentation literal source_literal_950_4; it is not a model call. Then Evaluate once str(path).strip(); assign in source target order to s.
  // Source: vvaharness/config/__init__.py:957-958
  if (the source predicate s.startswith('\\\\') or s.startswith('//') is truthy) {
    // Source: vvaharness/config/__init__.py:958-958
    End this invocation with True.
  }
  // Source: vvaharness/config/__init__.py:960-960
  End this invocation with PureWindowsPath(s).drive.startswith('\\\\').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/config/__init__.py:966-966
In source order: For _MAX_STEP1_OVERLAY_BYTES, assign 1 * 1024 * 1024; source annotation Final.
// Source: vvaharness/config/__init__.py:969-1008
// Source signature: apply_step1_overlay(cfg: Config, path: str | Path, *, expand: bool=True) -> tuple[Config, bool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn apply_step1_overlay(cfg, path, expand) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/config/__init__.py:971-976
  In source order: Retain source documentation literal source_literal_971_4; it is not a model call. Then Evaluate once Path(path); assign in source target order to p.
  // Source: vvaharness/config/__init__.py:979-982
  if (the source predicate is_network_path(p) is truthy) {
    // Source: vvaharness/config/__init__.py:980-982
    Raise ValueError(source_template_981_12).
  }
  // Source: vvaharness/config/__init__.py:983-984
  if (the source predicate not p.is_file() is truthy) {
    // Source: vvaharness/config/__init__.py:984-984
    End this invocation with (cfg, False).
  }
  // Source: vvaharness/config/__init__.py:985-985
  In source order: Evaluate once p.stat().st_size; assign in source target order to size.
  // Source: vvaharness/config/__init__.py:986-990
  if (the source predicate size > _MAX_STEP1_OVERLAY_BYTES is truthy) {
    // Source: vvaharness/config/__init__.py:987-990
    Raise ValueError(source_template_988_12).
  }
  // Source: vvaharness/config/__init__.py:991-996
  Perform the following protected operations {
    // Source: vvaharness/config/__init__.py:992-992
    In source order: Evaluate once p.read_text(encoding='utf-8'); assign in source target order to text.
  }
  // Source: vvaharness/config/__init__.py:993-996
  On the first matching source exception UnicodeDecodeError as e, in handler order {
    // Source: vvaharness/config/__init__.py:994-996
    Raise ValueError(source_template_995_12) with explicit source cause e.
  }
  // Source: vvaharness/config/__init__.py:997-1000
  Perform the following protected operations {
    // Source: vvaharness/config/__init__.py:998-998
    In source order: Evaluate once yaml.safe_load(text) or {}; assign in source target order to over.
  }
  // Source: vvaharness/config/__init__.py:999-1000
  On the first matching source exception yaml.YAMLError as e, in handler order {
    // Source: vvaharness/config/__init__.py:1000-1000
    Raise ValueError(source_template_1000_25) with explicit source cause e.
  }
  // Source: vvaharness/config/__init__.py:1001-1002
  if (the source predicate not isinstance(over, dict) is truthy) {
    // Source: vvaharness/config/__init__.py:1002-1002
    Raise ValueError(source_template_1002_25).
  }
  // Source: vvaharness/config/__init__.py:1003-1004
  if (the source predicate set(over) == {'step1'} and isinstance(over['step1'], dict) is truthy) {
    // Source: vvaharness/config/__init__.py:1004-1004
    In source order: Evaluate once over['step1']; assign in source target order to over.
  }
  // Source: vvaharness/config/__init__.py:1005-1007
  In source order: Evaluate once _expand_tree(over, ('step1',)) if expand else over; assign in source target order to over. Then Evaluate once cfg._data.get('step1') or {}; assign in source target order to base1. Then Evaluate once _append_merge(base1, over); assign in source target order to cfg._data['step1'].
  // Source: vvaharness/config/__init__.py:1008-1008
  End this invocation with (cfg, True).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.config.constants import CREDENTIAL_DESTINATIONS, ENDPOINT_KEYS, LOCAL_OVERLAY_NAME, NO_LOCAL_CONFIG_ENV, TLS_ROUTING_KEYS, is_secret_var_name` at source line 27: `source_detail/vvaharness/config/constants.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 35: `source_detail/vvaharness/util/console.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/config/__init__.py.sudo.md). Exact strings in the evidence asset support this conversion.
