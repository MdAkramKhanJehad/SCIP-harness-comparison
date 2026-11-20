# vvaharness/models/scan/threat.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/models/scan/threat.py.evidence.json`. SHA-256: `b7edbae10bf1c4fbe625a3a81a4197803c2d3aa7f6adada4ba5259aa4d9a770a`.

```sudo
// Source: vvaharness/models/scan/threat.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import logging; preserve alias and import-time effects. Then Resolve source import from typing import Any, Literal; preserve alias and import-time effects. Then Resolve source import from pydantic import BaseModel, Field, field_validator; preserve alias and import-time effects.
// Source: vvaharness/models/scan/threat.py:23-33
In source order: Resolve source import from vvaharness.models.scan._coerce import _coerce_enum, _coerce_str_list; preserve alias and import-time effects. Then Evaluate once logging.getLogger(__name__); assign in source target order to log. Then Evaluate once {'low', 'medium', 'high', 'critical'}; assign in source target order to _SENSITIVITY. Then Evaluate once {'none': 'low', 'info': 'low', 'informational': 'low', 'minor': 'low', 'moderate': 'medium', 'med': 'medium', 'normal': 'medium', 'major': 'high', 'severe': 'high', 'important': 'high', 'crit': 'critical', 'blocker': 'critical', 'extreme': 'critical'}; assign in source target order to _SENSITIVITY_ALIAS.
// Source: vvaharness/models/scan/threat.py:36-44
interface Asset {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/threat.py:37-39
  In source order: For name, declare without assigning a value; source annotation str. Then For description, assign ''; source annotation str. Then For sensitivity, assign 'medium'; source annotation Literal['low', 'medium', 'high', 'critical'].
  // Source: vvaharness/models/scan/threat.py:43-44
  // Source: vvaharness/models/scan/threat.py:41-42
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('sensitivity', mode='before'), classmethod.
  // Source: vvaharness/models/scan/threat.py:43-44
  // Source signature: _v_sensitivity(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_sensitivity(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:44-44
    End this invocation with _coerce_enum(v, _SENSITIVITY, _SENSITIVITY_ALIAS, 'medium').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/scan/threat.py:47-50
interface TrustBoundary {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/threat.py:48-50
  In source order: For entry_point, declare without assigning a value; source annotation str. Then For crossing, declare without assigning a value; source annotation str. Then For reachable_assets, assign []; source annotation list[str].
}
// Source: vvaharness/models/scan/threat.py:53-73
In source order: Evaluate once {'remote_unauth', 'remote_auth', 'adjacent_network', 'local_user', 'local_admin', 'supply_chain', 'insider'}; assign in source target order to _ACTORS. Then Evaluate once {'external': 'remote_unauth', 'anonymous': 'remote_unauth', 'unauthenticated': 'remote_unauth', 'internet': 'remote_unauth', 'public': 'remote_unauth', 'attacker': 'remote_unauth', 'authenticated': 'remote_auth', 'user': 'remote_auth', 'tenant': 'remote_auth', 'customer': 'remote_auth', 'internal': 'adjacent_network', 'network': 'adjacent_network', 'lan': 'adjacent_network', 'adjacent': 'adjacent_network', 'local': 'local_user', 'physical': 'local_user', 'admin': 'local_admin', 'root': 'local_admin', 'operator': 'local_admin', 'privileged': 'local_admin', 'supply': 'supply_chain', 'dependency': 'supply_chain', 'third_party': 'supply_chain', 'vendor': 'supply_chain', 'employee': 'insider', 'developer': 'insider', 'malicious_insider': 'insider'}; assign in source target order to _ACTOR_ALIAS. Then Evaluate once {'low', 'medium', 'high', 'critical', 'existential'}; assign in source target order to _IMPACTS. Then Evaluate once {**_SENSITIVITY_ALIAS, 'catastrophic': 'existential', 'fatal': 'existential'}; assign in source target order to _IMPACT_ALIAS. Then Evaluate once {'very_rare', 'rare', 'possible', 'likely', 'almost_certain'}; assign in source target order to _LIKELIHOODS.
// Source: vvaharness/models/scan/threat.py:74-82
In source order: Evaluate once {'very_unlikely': 'very_rare', 'negligible': 'very_rare', 'remote': 'very_rare', 'improbable': 'very_rare', 'unlikely': 'rare', 'low': 'rare', 'moderate': 'possible', 'medium': 'possible', 'occasional': 'possible', 'probable': 'likely', 'high': 'likely', 'frequent': 'likely', 'very_likely': 'almost_certain', 'certain': 'almost_certain', 'definite': 'almost_certain', 'inevitable': 'almost_certain'}; assign in source target order to _LIKELIHOOD_ALIAS.
// Source: vvaharness/models/scan/threat.py:85-126
interface Threat {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/threat.py:87-101
  In source order: For id, assign ''; source annotation str. Then For threat, declare without assigning a value; source annotation str. Then For actor, declare without assigning a value; source annotation Literal['remote_unauth', 'remote_auth', 'adjacent_network', 'local_user', 'local_admin', 'supply_chain', 'insider']. Then For surface, declare without assigning a value; source annotation str. Then For surface_files, assign Field(description=source_literal_94_12); source annotation list[str].
  // Source: vvaharness/models/scan/threat.py:102-106
  In source order: For asset, declare without assigning a value; source annotation str. Then For impact, declare without assigning a value; source annotation Literal['low', 'medium', 'high', 'critical', 'existential']. Then For likelihood, declare without assigning a value; source annotation Literal['very_rare', 'rare', 'possible', 'likely', 'almost_certain']. Then For controls, assign ''; source annotation str. Then For evidence, assign ''; source annotation str.
  // Source: vvaharness/models/scan/threat.py:110-111
  // Source: vvaharness/models/scan/threat.py:108-109
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('actor', mode='before'), classmethod.
  // Source: vvaharness/models/scan/threat.py:110-111
  // Source signature: _v_actor(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_actor(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:111-111
    End this invocation with _coerce_enum(v, _ACTORS, _ACTOR_ALIAS, 'remote_auth').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/threat.py:115-116
  // Source: vvaharness/models/scan/threat.py:113-114
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('impact', mode='before'), classmethod.
  // Source: vvaharness/models/scan/threat.py:115-116
  // Source signature: _v_impact(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_impact(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:116-116
    End this invocation with _coerce_enum(v, _IMPACTS, _IMPACT_ALIAS, 'medium').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/threat.py:120-121
  // Source: vvaharness/models/scan/threat.py:118-119
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('likelihood', mode='before'), classmethod.
  // Source: vvaharness/models/scan/threat.py:120-121
  // Source signature: _v_likelihood(cls, v)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_likelihood(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:121-121
    End this invocation with _coerce_enum(v, _LIKELIHOODS, _LIKELIHOOD_ALIAS, 'possible').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/models/scan/threat.py:125-126
  // Source: vvaharness/models/scan/threat.py:123-124
  Before creating this callable, evaluate and retain decorators top-to-bottom: field_validator('surface_files', mode='before'), classmethod.
  // Source: vvaharness/models/scan/threat.py:125-126
  // Source signature: _v_surface_files(cls, v: Any) -> Any
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _v_surface_files(cls, v) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:126-126
    End this invocation with _coerce_str_list(v, 'Threat.surface_files').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
// Source: vvaharness/models/scan/threat.py:129-206
interface ThreatModel {
  Describe the source Python type, preserving its base/metaclass expression order: BaseModel.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/models/scan/threat.py:130-134
  In source order: For system_context, assign ''; source annotation str. Then For assets, assign []; source annotation list[Asset]. Then For trust_boundaries, assign []; source annotation list[TrustBoundary]. Then For threats, assign []; source annotation list[Threat]. Then For open_questions, assign []; source annotation list[str].
  // Source: vvaharness/models/scan/threat.py:136-138
  // Source signature: threat_ids(self) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn threat_ids(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:137-137
    In source order: Retain source documentation literal source_literal_137_8; it is not a model call.
    // Source: vvaharness/models/scan/threat.py:138-138
    End this invocation with [t.id or source_template_138_24 for i, t in enumerate(self.threats, 1)].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/threat.py:140-163
  // Source signature: to_prompt_block(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn to_prompt_block(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:141-141
    In source order: Evaluate once ['THREAT MODEL:', '', 'System context:', self.system_context, '']; assign in source target order to lines.
    // Source: vvaharness/models/scan/threat.py:142-146
    if (the source predicate self.assets is truthy) {
      // Source: vvaharness/models/scan/threat.py:143-143
      In source order: Evaluate lines.append(source_template_143_25); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/threat.py:144-145
      for each a in self.assets {
        // Source: vvaharness/models/scan/threat.py:145-145
        In source order: Evaluate lines.append(source_template_145_29); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:146-146
      In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/threat.py:147-152
    if (the source predicate self.trust_boundaries is truthy) {
      // Source: vvaharness/models/scan/threat.py:148-148
      In source order: Evaluate lines.append(source_template_148_25); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/threat.py:149-151
      for each b in self.trust_boundaries {
        // Source: vvaharness/models/scan/threat.py:150-151
        In source order: Evaluate once ', '.join(b.reachable_assets) or '-'; assign in source target order to ra. Then Evaluate lines.append(source_template_151_29); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:152-152
      In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/threat.py:153-162
    if (the source predicate self.threats is truthy) {
      // Source: vvaharness/models/scan/threat.py:154-154
      In source order: Evaluate lines.append(source_template_154_25); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/threat.py:155-161
      for each t in self.threats {
        // Source: vvaharness/models/scan/threat.py:156-161
        In source order: Evaluate lines.append(source_template_157_20 + (source_template_159_23 if t.controls and t.controls != 'none' else '') + ')'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:162-162
      In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/threat.py:163-163
    End this invocation with source_literal_163_15.join(lines).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/models/scan/threat.py:165-206
  // Source signature: to_compact_prompt_block(self, *, max_assets: int=8, max_boundaries: int=12, max_threats: int=12, max_context_chars: int=2500) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn to_compact_prompt_block(self, max_assets, max_boundaries, max_threats, max_context_chars) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/models/scan/threat.py:169-175
    In source order: Evaluate once ['THREAT MODEL:', '', 'System context:', self.system_context[:max_context_chars], '']; assign in source target order to lines.
    // Source: vvaharness/models/scan/threat.py:176-183
    if (the source predicate self.assets is truthy) {
      // Source: vvaharness/models/scan/threat.py:177-178
      In source order: Evaluate once self.assets[:max_assets]; assign in source target order to assets. Then Evaluate lines.append(source_template_178_25); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/threat.py:179-180
      for each a in assets {
        // Source: vvaharness/models/scan/threat.py:180-180
        In source order: Evaluate lines.append(source_template_180_29); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:181-182
      if (the source predicate len(self.assets) > len(assets) is truthy) {
        // Source: vvaharness/models/scan/threat.py:182-182
        In source order: Evaluate lines.append('  …(truncated)'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:183-183
      In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/threat.py:184-192
    if (the source predicate self.trust_boundaries is truthy) {
      // Source: vvaharness/models/scan/threat.py:185-186
      In source order: Evaluate once self.trust_boundaries[:max_boundaries]; assign in source target order to bounds. Then Evaluate lines.append(source_template_186_25); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/threat.py:187-189
      for each b in bounds {
        // Source: vvaharness/models/scan/threat.py:188-189
        In source order: Evaluate once ', '.join(b.reachable_assets) or '-'; assign in source target order to ra. Then Evaluate lines.append(source_template_189_29); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:190-191
      if (the source predicate len(self.trust_boundaries) > len(bounds) is truthy) {
        // Source: vvaharness/models/scan/threat.py:191-191
        In source order: Evaluate lines.append('  …(truncated)'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:192-192
      In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/threat.py:193-205
    if (the source predicate self.threats is truthy) {
      // Source: vvaharness/models/scan/threat.py:194-195
      In source order: Evaluate once self.threats[:max_threats]; assign in source target order to threats. Then Evaluate lines.append(source_template_195_25); retain side effects and discard the expression result.
      // Source: vvaharness/models/scan/threat.py:196-202
      for each t in threats {
        // Source: vvaharness/models/scan/threat.py:197-202
        In source order: Evaluate lines.append(source_template_198_20 + (source_template_200_23 if t.controls and t.controls != 'none' else '') + ')'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:203-204
      if (the source predicate len(self.threats) > len(threats) is truthy) {
        // Source: vvaharness/models/scan/threat.py:204-204
        In source order: Evaluate lines.append('  …(truncated)'); retain side effects and discard the expression result.
      }
      // Source: vvaharness/models/scan/threat.py:205-205
      In source order: Evaluate lines.append(''); retain side effects and discard the expression result.
    }
    // Source: vvaharness/models/scan/threat.py:206-206
    End this invocation with source_literal_206_15.join(lines).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/models/scan/threat.py:209-213
In source order: Evaluate once {'existential': 5, 'critical': 4, 'high': 3, 'medium': 2, 'low': 1}; assign in source target order to _IMPACT_RANK. Then Evaluate once {'almost_certain': 5, 'likely': 4, 'possible': 3, 'rare': 2, 'very_rare': 1}; assign in source target order to _LIKELIHOOD_RANK. Then Evaluate once {'critical': 4, 'high': 3, 'medium': 2, 'low': 1}; assign in source target order to _SENSITIVITY_RANK. Then Evaluate once {'remote_unauth': 6, 'remote_auth': 5, 'adjacent_network': 4, 'local_admin': 3, 'local_user': 2, 'supply_chain': 1, 'insider': 1}; assign in source target order to _ACTOR_RANK.
// Source: vvaharness/models/scan/threat.py:216-219
// Source signature: _sensitivity_of(t: Threat, tm: ThreatModel) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sensitivity_of(t, tm) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:217-218
  In source order: Evaluate once t.asset.strip().lower(); assign in source target order to key. Then Evaluate once next((x for x in tm.assets if x.name.strip().lower() == key), None); assign in source target order to a.
  // Source: vvaharness/models/scan/threat.py:219-219
  End this invocation with _SENSITIVITY_RANK.get(a.sensitivity, 0) if a else 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:222-231
// Source signature: _rank_key(t: Threat, tm: ThreatModel) -> tuple
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rank_key(t, tm) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:223-223
  In source order: Retain source documentation literal source_literal_223_4; it is not a model call.
  // Source: vvaharness/models/scan/threat.py:225-231
  End this invocation with (-_IMPACT_RANK.get(t.impact, 0), -_sensitivity_of(t, tm), -_LIKELIHOOD_RANK.get(t.likelihood, 0), -_ACTOR_RANK.get(t.actor, 0), 0 if not t.controls or t.controls == 'none' else 1, _id_ordinal(t.id), t.id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:234-240
// Source signature: _id_ordinal(threat_id: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _id_ordinal(threat_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:235-235
  In source order: Retain source documentation literal source_literal_235_4; it is not a model call.
  // Source: vvaharness/models/scan/threat.py:237-240
  Perform the following protected operations {
    // Source: vvaharness/models/scan/threat.py:238-238
    End this invocation with int(threat_id[1:]).
  }
  // Source: vvaharness/models/scan/threat.py:239-240
  On the first matching source exception (TypeError, ValueError), in handler order {
    // Source: vvaharness/models/scan/threat.py:240-240
    End this invocation with 1000000.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:243-254
// Source signature: _covered_boundaries(threats: list[Threat], pool: set[int], boundaries: list[TrustBoundary]) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _covered_boundaries(threats, pool, boundaries) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:245-247
  In source order: Retain source documentation literal source_literal_245_4; it is not a model call. Then For covered, assign set(); source annotation set[str].
  // Source: vvaharness/models/scan/threat.py:248-253
  for each b in boundaries {
    // Source: vvaharness/models/scan/threat.py:249-249
    In source order: Evaluate once b.entry_point.strip().casefold(); assign in source target order to bnorm.
    // Source: vvaharness/models/scan/threat.py:250-253
    for each i in pool {
      // Source: vvaharness/models/scan/threat.py:251-253
      if (the source predicate threats[i].surface.strip().casefold() == bnorm is truthy) {
        // Source: vvaharness/models/scan/threat.py:252-252
        In source order: Evaluate covered.add(b.entry_point); retain side effects and discard the expression result.
        // Source: vvaharness/models/scan/threat.py:253-253
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
  }
  // Source: vvaharness/models/scan/threat.py:254-254
  End this invocation with covered.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:257-264
// Source signature: _next_covering_candidate(threats: list[Threat], kept: set[int], evicted_idx: list[int], boundary: str) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _next_covering_candidate(threats, kept, evicted_idx, boundary) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:259-259
  In source order: Evaluate once boundary.strip().casefold(); assign in source target order to bnorm.
  // Source: vvaharness/models/scan/threat.py:260-264
  End this invocation with next((i for i in evicted_idx if i not in kept and threats[i].surface.strip().casefold() == bnorm), None).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:267-275
// Source signature: _best_evictable(threats: list[Threat], kept: set[int], kept_order: list[int], boundaries: list[TrustBoundary]) -> int | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _best_evictable(threats, kept, kept_order, boundaries) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:269-270
  In source order: Retain source documentation literal source_literal_269_4; it is not a model call. Then Evaluate once _covered_boundaries(threats, kept, boundaries); assign in source target order to current_coverage.
  // Source: vvaharness/models/scan/threat.py:271-274
  for each i in reversed(kept_order) {
    // Source: vvaharness/models/scan/threat.py:272-272
    In source order: Evaluate once _covered_boundaries(threats, kept - {i}, boundaries); assign in source target order to trial_coverage.
    // Source: vvaharness/models/scan/threat.py:273-274
    if (the source predicate len(trial_coverage) >= len(current_coverage) is truthy) {
      // Source: vvaharness/models/scan/threat.py:274-274
      End this invocation with i.
    }
  }
  // Source: vvaharness/models/scan/threat.py:275-275
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:278-303
// Source signature: _promote_for_coverage(threats: list[Threat], kept: set[int], evicted_idx: list[int], boundaries: list[TrustBoundary]) -> tuple[set[int], int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _promote_for_coverage(threats, kept, evicted_idx, boundaries) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:281-285
  In source order: Retain source documentation literal source_literal_281_4; it is not a model call. Then Evaluate once {b.entry_point for b in boundaries}; assign in source target order to all_boundary_names. Then Evaluate once all_boundary_names - _covered_boundaries(threats, kept, boundaries); assign in source target order to uncovered. Then Evaluate once sorted(kept); assign in source target order to kept_order. Then Evaluate once 0; assign in source target order to promoted.
  // Source: vvaharness/models/scan/threat.py:286-286
  In source order: Evaluate once True; assign in source target order to progressed.
  // Source: vvaharness/models/scan/threat.py:287-302
  while (the source predicate uncovered and progressed is truthy) {
    // Source: vvaharness/models/scan/threat.py:288-288
    In source order: Evaluate once False; assign in source target order to progressed.
    // Source: vvaharness/models/scan/threat.py:289-302
    for each boundary in list(uncovered) {
      // Source: vvaharness/models/scan/threat.py:290-290
      In source order: Evaluate once _next_covering_candidate(threats, kept, evicted_idx, boundary); assign in source target order to candidate.
      // Source: vvaharness/models/scan/threat.py:291-292
      if (the source predicate candidate is None is truthy) {
        // Source: vvaharness/models/scan/threat.py:292-292
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/models/scan/threat.py:293-293
      In source order: Evaluate once _best_evictable(threats, kept, kept_order, boundaries); assign in source target order to evict_at.
      // Source: vvaharness/models/scan/threat.py:294-295
      if (the source predicate evict_at is None is truthy) {
        // Source: vvaharness/models/scan/threat.py:295-295
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/models/scan/threat.py:296-300
      In source order: Evaluate kept.discard(evict_at); retain side effects and discard the expression result. Then Evaluate kept_order.remove(evict_at); retain side effects and discard the expression result. Then Evaluate kept.add(candidate); retain side effects and discard the expression result. Then Evaluate kept_order.append(candidate); retain side effects and discard the expression result. Then Apply source augmented assignment promoted += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/models/scan/threat.py:301-302
      In source order: Evaluate uncovered.discard(boundary); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to progressed.
    }
  }
  // Source: vvaharness/models/scan/threat.py:303-303
  End this invocation with (kept, promoted).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:306-330
// Source signature: _cap_threats(tm: ThreatModel, max_threats: int) -> ThreatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap_threats(tm, max_threats) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:307-312
  In source order: Retain source documentation literal source_literal_307_4; it is not a model call. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once sorted(tm.threats, key=lambda t: _rank_key(t, tm)); assign in source target order to threats. Then Evaluate COUNTERS.bump('s2_threats_raw', len(threats)); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/threat.py:313-314
  if (the source predicate len(threats) <= max_threats is truthy) {
    // Source: vvaharness/models/scan/threat.py:314-314
    End this invocation with tm.model_copy(update={'threats': threats}).
  }
  // Source: vvaharness/models/scan/threat.py:317-323
  In source order: For kept, assign set(range(min(max_threats, len(threats)))); source annotation set[int]. Then Evaluate once list(range(len(kept), len(threats))); assign in source target order to evicted_idx. Then Evaluate once len(evicted_idx); assign in source target order to truncated_n. Then Evaluate once _promote_for_coverage(threats, kept, evicted_idx, tm.trust_boundaries); assign in source target order to (kept, promoted). Then Evaluate COUNTERS.bump('s2_threats_truncated', truncated_n); retain side effects and discard the expression result.
  // Source: vvaharness/models/scan/threat.py:324-326
  In source order: Evaluate COUNTERS.bump('s2_threats_promoted', promoted); retain side effects and discard the expression result. Then Evaluate once [threats[i].id or source_template_326_32 for i in range(len(threats)) if i not in kept]; assign in source target order to evicted.
  // Source: vvaharness/models/scan/threat.py:327-328
  if (the source predicate evicted is truthy) {
    // Source: vvaharness/models/scan/threat.py:328-328
    In source order: Evaluate COUNTERS.note('s2_threats_evicted_ids', ','.join(evicted)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/models/scan/threat.py:329-329
  In source order: Evaluate once [threats[i] for i in sorted(kept)]; assign in source target order to final.
  // Source: vvaharness/models/scan/threat.py:330-330
  End this invocation with tm.model_copy(update={'threats': final}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:333-338
// Source signature: _cap_assets(tm: ThreatModel, max_assets: int) -> ThreatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap_assets(tm, max_assets) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:334-335
  if (the source predicate len(tm.assets) <= max_assets is truthy) {
    // Source: vvaharness/models/scan/threat.py:335-335
    End this invocation with tm.
  }
  // Source: vvaharness/models/scan/threat.py:336-337
  In source order: Evaluate once sorted(tm.assets, key=lambda a: (-_SENSITIVITY_RANK.get(a.sensitivity, 0), a.name)); assign in source target order to ranked.
  // Source: vvaharness/models/scan/threat.py:338-338
  End this invocation with tm.model_copy(update={'assets': ranked[:max_assets]}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/models/scan/threat.py:341-346
// Source signature: _cap_boundaries(tm: ThreatModel, max_boundaries: int) -> ThreatModel
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cap_boundaries(tm, max_boundaries) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/models/scan/threat.py:342-343
  if (the source predicate len(tm.trust_boundaries) <= max_boundaries is truthy) {
    // Source: vvaharness/models/scan/threat.py:343-343
    End this invocation with tm.
  }
  // Source: vvaharness/models/scan/threat.py:344-345
  In source order: Evaluate once sorted(tm.trust_boundaries, key=lambda b: (-len(b.reachable_assets), b.entry_point)); assign in source target order to ranked.
  // Source: vvaharness/models/scan/threat.py:346-346
  End this invocation with tm.model_copy(update={'trust_boundaries': ranked[:max_boundaries]}).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.models.scan._coerce import _coerce_enum, _coerce_str_list` at source line 23: `source_detail/vvaharness/models/scan/_coerce.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 308: `source_detail/vvaharness/util/counters.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/models/scan/threat.py.sudo.md). Exact strings in the evidence asset support this conversion.
