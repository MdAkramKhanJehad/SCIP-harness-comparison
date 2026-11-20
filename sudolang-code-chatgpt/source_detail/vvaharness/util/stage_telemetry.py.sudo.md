# vvaharness/util/stage_telemetry.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/stage_telemetry.py.evidence.json`. SHA-256: `dae3ac168c4de01957afec846870594e24539f9fe55cd2b542c378e0e29be035`.

```sudo
// Source: vvaharness/util/stage_telemetry.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from typing import TYPE_CHECKING, TypedDict, cast; preserve alias and import-time effects.
// Source: vvaharness/util/stage_telemetry.py:24-29
In source order: Resolve source import from vvaharness.util.pricing import ModelPricing, PricingTable, TokenBucket, bucket_cost_usd; preserve alias and import-time effects.
// Source: vvaharness/util/stage_telemetry.py:31-32
if (the source predicate TYPE_CHECKING is truthy) {
  // Source: vvaharness/util/stage_telemetry.py:32-32
  In source order: Resolve source import from vvaharness.orchestrator.checkpoints import StageProvenance; preserve alias and import-time effects.
}
// Source: vvaharness/util/stage_telemetry.py:34-73
In source order: For STAGE_IDS, assign ('s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11'); source annotation tuple[str, ...]. Then For PHASE_MAP, assign {'s0-seed': ('s0', None), 's1-autoexclude': ('s1', 'autoexclude'), 's1-preprocess': ('s1', 'preprocess'), 's2-threatmodel': ('s2', 'threatmodel'), 's3-decompose': ('s3', 'decompose'), 's4-deepdive': ('s4', 'deepdive'), 's5-prefilter': ('s5', 'dedup'), 's6-verify': ('s6', 'verify'), 's6-ev': ('s6', 'exploit_verification.attacker'), 's7-dedup': ('s7', 'dedup'), 's8-chain': ('s8', 'chain'), 's10-remediate': ('s10', 'remediate'), 'remediation-agent-remediate': ('s10', 'remediate'), 's11-validate': ('s11', 'validate')}; source annotation dict[str, tuple[str, str | None]]. Then For STAGE_ROLES, assign {'s0': None, 's1': 'preprocess', 's2': 'threatmodel', 's3': 'decompose', 's4': 'deepdive', 's5': 'dedup', 's6': 'verify', 's7': 'dedup', 's8': 'chain', 's9': None, 's10': 'remediate', 's11': 'validate'}; source annotation dict[str, str | None]. Then For ESTIMATED_COST_STAGES, assign frozenset({'s11'}); source annotation frozenset[str]. Then For ESTIMATED_COST_ROLES, assign frozenset({'exploit_verification.attacker'}); source annotation frozenset[str].
// Source: vvaharness/util/stage_telemetry.py:75-82
In source order: For _ROLE_FALLBACKS, assign {'exploit_verification.attacker': ('exploit_verification.judge', 'exploit_verification.mapper', 'exploit_verification.classify')}; source annotation dict[str, tuple[str, ...]]. Then Evaluate once 'not_run'; assign in source target order to _NOT_RUN. Then Evaluate once 'running'; assign in source target order to _RUNNING.
// Source: vvaharness/util/stage_telemetry.py:85-90
interface StageRecord {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:86-90
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then For label, declare without assigning a value; source annotation str. Then For outcome, declare without assigning a value; source annotation str. Then For duration_sec, declare without assigning a value; source annotation float | None.
}
// Source: vvaharness/util/stage_telemetry.py:93-103
interface TokenSnapshot {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:94-99
  In source order: Retain source documentation literal source_literal_94_4; it is not a model call. Then For prompt, declare without assigning a value; source annotation int. Then For completion, declare without assigning a value; source annotation int. Then For total, declare without assigning a value; source annotation int. Then For calls, declare without assigning a value; source annotation int.
  // Source: vvaharness/util/stage_telemetry.py:100-103
  In source order: For calls_with_usage, declare without assigning a value; source annotation int. Then For completion_absent, declare without assigning a value; source annotation int. Then For by_phase, declare without assigning a value; source annotation dict[str, TokenBucket].
}
// Source: vvaharness/util/stage_telemetry.py:106-120
interface UnattributedTokens {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:107-119
  In source order: Retain source documentation literal source_literal_107_4; it is not a model call. Then For prompt, declare without assigning a value; source annotation int. Then For completion, declare without assigning a value; source annotation int. Then For cache_read, declare without assigning a value; source annotation int. Then For cache_write, declare without assigning a value; source annotation int.
  // Source: vvaharness/util/stage_telemetry.py:120-120
  In source order: For calls, declare without assigning a value; source annotation int.
}
// Source: vvaharness/util/stage_telemetry.py:123-134
interface StageEntry {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:124-129
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call. Then For label, declare without assigning a value; source annotation str. Then For outcome, declare without assigning a value; source annotation str. Then For duration_sec, declare without assigning a value; source annotation float | None. Then For tokens, declare without assigning a value; source annotation TokenBucket.
  // Source: vvaharness/util/stage_telemetry.py:130-134
  In source order: For model, declare without assigning a value; source annotation str | None. Then For cost_usd, declare without assigning a value; source annotation float | None. Then For cost_estimated, declare without assigning a value; source annotation bool. Then For cached_from_config_sha, declare without assigning a value; source annotation str | None.
}
// Source: vvaharness/util/stage_telemetry.py:137-153
interface Totals {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:138-143
  In source order: Retain source documentation literal source_literal_138_4; it is not a model call. Then For prompt_tokens, declare without assigning a value; source annotation int. Then For completion_tokens, declare without assigning a value; source annotation int. Then For total_tokens, declare without assigning a value; source annotation int. Then For cache_read_tokens, declare without assigning a value; source annotation int.
  // Source: vvaharness/util/stage_telemetry.py:144-149
  In source order: For cache_write_tokens, declare without assigning a value; source annotation int. Then For calls, declare without assigning a value; source annotation int. Then For calls_with_usage, declare without assigning a value; source annotation int. Then For completion_absent, declare without assigning a value; source annotation int. Then For cache_unparsed_calls, declare without assigning a value; source annotation int.
  // Source: vvaharness/util/stage_telemetry.py:150-153
  In source order: For cost_usd, declare without assigning a value; source annotation float | None. Then For unattributed, declare without assigning a value; source annotation UnattributedTokens. Then For cached_carryover, declare without assigning a value; source annotation TokenBucket.
}
// Source: vvaharness/util/stage_telemetry.py:156-161
interface PricingProvenance {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:157-161
  In source order: Retain source documentation literal source_literal_157_4; it is not a model call. Then For file, declare without assigning a value; source annotation str. Then For sha256, declare without assigning a value; source annotation str. Then For source, declare without assigning a value; source annotation str.
}
// Source: vvaharness/util/stage_telemetry.py:164-168
interface PricingStatus {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:165-168
  In source order: Retain source documentation literal source_literal_165_4; it is not a model call. Then For status, declare without assigning a value; source annotation str. Then For reason, declare without assigning a value; source annotation str.
}
// Source: vvaharness/util/stage_telemetry.py:171-177
interface StageSection {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:172-177
  In source order: Retain source documentation literal source_literal_172_4; it is not a model call. Then For stages, declare without assigning a value; source annotation dict[str, StageEntry]. Then For totals, declare without assigning a value; source annotation Totals. Then For pricing, declare without assigning a value; source annotation PricingProvenance | None. Then For pricing_status, declare without assigning a value; source annotation PricingStatus.
}
// Source: vvaharness/util/stage_telemetry.py:180-182
// Source signature: _copy(record: StageRecord) -> StageRecord
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _copy(record) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:181-182
  End this invocation with StageRecord(label=record['label'], outcome=record['outcome'], duration_sec=record['duration_sec']).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:185-227
interface _StageRecorder {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:186-186
  In source order: Retain source documentation literal source_literal_186_4; it is not a model call.
  // Source: vvaharness/util/stage_telemetry.py:189-191
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:190-191
    In source order: Evaluate once threading.Lock(); assign in source target order to self._lock. Then For self._stages, assign {}; source annotation dict[str, StageRecord].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:193-197
  // Source signature: start(self, stage_id: str, label: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn start(self, stage_id, label) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:194-194
    In source order: Retain source documentation literal source_literal_194_8; it is not a model call.
    // Source: vvaharness/util/stage_telemetry.py:195-197
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:196-197
      In source order: Evaluate once StageRecord(label=label, outcome=_RUNNING, duration_sec=None); assign in source target order to self._stages[stage_id].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:199-209
  // Source signature: done(self, stage_id: str, *, outcome: str='completed', duration_sec: float | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn done(self, stage_id, outcome, duration_sec) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:201-201
    In source order: Retain source documentation literal source_literal_201_8; it is not a model call.
    // Source: vvaharness/util/stage_telemetry.py:202-209
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:203-203
      In source order: Evaluate once self._stages.get(stage_id); assign in source target order to record.
      // Source: vvaharness/util/stage_telemetry.py:204-207
      if (the source predicate record is None is truthy) {
        // Source: vvaharness/util/stage_telemetry.py:205-207
        In source order: Evaluate once StageRecord(label='', outcome=outcome, duration_sec=None); assign in source target order to record. Then Evaluate once record; assign in source target order to self._stages[stage_id].
      }
      // Source: vvaharness/util/stage_telemetry.py:208-209
      In source order: Evaluate once outcome; assign in source target order to record['outcome']. Then Evaluate once duration_sec; assign in source target order to record['duration_sec'].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:211-215
  // Source signature: mark(self, stage_id: str, outcome: str, label: str='') -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn mark(self, stage_id, outcome, label) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:212-212
    In source order: Retain source documentation literal source_literal_212_8; it is not a model call.
    // Source: vvaharness/util/stage_telemetry.py:213-215
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:214-215
      In source order: Evaluate once StageRecord(label=label, outcome=outcome, duration_sec=None); assign in source target order to self._stages[stage_id].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:217-220
  // Source signature: reset(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn reset(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:218-218
    In source order: Retain source documentation literal source_literal_218_8; it is not a model call.
    // Source: vvaharness/util/stage_telemetry.py:219-220
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:220-220
      In source order: Evaluate once {}; assign in source target order to self._stages.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:222-227
  // Source signature: snapshot(self) -> dict[str, StageRecord]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn snapshot(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:223-223
    In source order: Retain source documentation literal source_literal_223_8; it is not a model call.
    // Source: vvaharness/util/stage_telemetry.py:224-227
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:225-226
      In source order: Evaluate once [s for s in STAGE_IDS if s in self._stages]; assign in source target order to known. Then Evaluate once [s for s in self._stages if s not in STAGE_IDS]; assign in source target order to extra.
      // Source: vvaharness/util/stage_telemetry.py:227-227
      End this invocation with {s: _copy(self._stages[s]) for s in known + extra}.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/stage_telemetry.py:230-230
In source order: Evaluate once _StageRecorder(); assign in source target order to STAGES.
// Source: vvaharness/util/stage_telemetry.py:233-250
interface _CachedProvenanceRecorder {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/stage_telemetry.py:234-234
  In source order: Retain source documentation literal source_literal_234_4; it is not a model call.
  // Source: vvaharness/util/stage_telemetry.py:236-238
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:237-238
    In source order: Evaluate once threading.Lock(); assign in source target order to self._lock. Then For self._entries, assign {}; source annotation dict[str, Mapping[str, object]].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:240-242
  // Source signature: record(self, stage_id: str, provenance: Mapping[str, object]) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn record(self, stage_id, provenance) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:241-242
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:242-242
      In source order: Evaluate once provenance; assign in source target order to self._entries[stage_id].
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:244-246
  // Source signature: reset(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn reset(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:245-246
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:246-246
      In source order: Evaluate once {}; assign in source target order to self._entries.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/stage_telemetry.py:248-250
  // Source signature: snapshot(self) -> dict[str, Mapping[str, object]]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn snapshot(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/stage_telemetry.py:249-250
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/stage_telemetry.py:250-250
      End this invocation with dict(self._entries).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/stage_telemetry.py:253-253
In source order: Evaluate once _CachedProvenanceRecorder(); assign in source target order to CACHED_PROVENANCE.
// Source: vvaharness/util/stage_telemetry.py:256-263
// Source signature: _sum_buckets(buckets: Sequence[TokenBucket]) -> TokenBucket
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sum_buckets(buckets) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:257-263
  End this invocation with TokenBucket(prompt=sum((b.get('prompt', 0) for b in buckets)), completion=sum((b.get('completion', 0) for b in buckets)), cache_read=sum((b.get('cache_read', 0) for b in buckets)), cache_write=sum((b.get('cache_write', 0) for b in buckets)), calls=sum((b.get('calls', 0) for b in buckets))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:266-268
// Source signature: _has_tokens(bucket: TokenBucket) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _has_tokens(bucket) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:267-268
  End this invocation with bucket.get('prompt', 0) + bucket.get('completion', 0) + bucket.get('cache_read', 0) > 0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:271-289
// Source signature: _group_phases(token_snap: TokenSnapshot) -> tuple[dict[str, list[tuple[str | None, TokenBucket]]], UnattributedTokens]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _group_phases(token_snap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:274-276
  In source order: For by_stage, assign {}; source annotation dict[str, list[tuple[str | None, TokenBucket]]]. Then Evaluate once UnattributedTokens(prompt=0, completion=0, cache_read=0, cache_write=0, calls=0); assign in source target order to unattributed.
  // Source: vvaharness/util/stage_telemetry.py:277-288
  for each (phase, bucket) in token_snap.get('by_phase', {}).items() {
    // Source: vvaharness/util/stage_telemetry.py:278-278
    In source order: Evaluate once PHASE_MAP.get(phase); assign in source target order to mapped.
    // Source: vvaharness/util/stage_telemetry.py:279-286
    if (the source predicate mapped is None is truthy) {
      // Source: vvaharness/util/stage_telemetry.py:281-285
      In source order: Apply source augmented assignment unattributed['prompt'] += bucket.get('prompt', 0) with source evaluation/in-place semantics. Then Apply source augmented assignment unattributed['completion'] += bucket.get('completion', 0) with source evaluation/in-place semantics. Then Apply source augmented assignment unattributed['cache_read'] += bucket.get('cache_read', 0) with source evaluation/in-place semantics. Then Apply source augmented assignment unattributed['cache_write'] += bucket.get('cache_write', 0) with source evaluation/in-place semantics. Then Apply source augmented assignment unattributed['calls'] += bucket.get('calls', 0) with source evaluation/in-place semantics.
      // Source: vvaharness/util/stage_telemetry.py:286-286
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/util/stage_telemetry.py:287-288
    In source order: Evaluate once mapped; assign in source target order to (stage_id, role). Then Evaluate by_stage.setdefault(stage_id, []).append((role, bucket)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/stage_telemetry.py:289-289
  End this invocation with (by_stage, unattributed).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:292-295
// Source signature: stage_token_bucket(step_id: str, token_snap: TokenSnapshot) -> TokenBucket
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn stage_token_bucket(step_id, token_snap) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:293-294
  In source order: Retain source documentation literal source_literal_293_4; it is not a model call. Then Evaluate once _group_phases(token_snap); assign in source target order to (by_stage, _).
  // Source: vvaharness/util/stage_telemetry.py:295-295
  End this invocation with _sum_buckets([bucket for _, bucket in by_stage.get(step_id, [])]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:298-306
// Source signature: _resolve_model(role: str | None, role_models: Mapping[str, str]) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_model(role, role_models) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:300-300
  In source order: Retain source documentation literal source_literal_300_4; it is not a model call.
  // Source: vvaharness/util/stage_telemetry.py:301-302
  if (the source predicate role is None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:302-302
    End this invocation with None.
  }
  // Source: vvaharness/util/stage_telemetry.py:303-305
  for each r in (role, *_ROLE_FALLBACKS.get(role, ())) {
    // Source: vvaharness/util/stage_telemetry.py:304-305
    if (the source predicate role_models.get(r) is truthy) {
      // Source: vvaharness/util/stage_telemetry.py:305-305
      End this invocation with role_models[r].
    }
  }
  // Source: vvaharness/util/stage_telemetry.py:306-306
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:309-314
// Source signature: _rate_for(role: str | None, role_models: Mapping[str, str], pricing: PricingTable) -> ModelPricing | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rate_for(role, role_models, pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:311-311
  In source order: Evaluate once _resolve_model(role, role_models); assign in source target order to model_id.
  // Source: vvaharness/util/stage_telemetry.py:312-313
  if (the source predicate model_id is None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:313-313
    End this invocation with None.
  }
  // Source: vvaharness/util/stage_telemetry.py:314-314
  End this invocation with pricing.models.get(model_id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:317-331
// Source signature: _stage_cost(phases: Sequence[tuple[str | None, TokenBucket]], role_models: Mapping[str, str], pricing: PricingTable | None) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stage_cost(phases, role_models, pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:320-320
  In source order: Retain source documentation literal source_literal_320_4; it is not a model call.
  // Source: vvaharness/util/stage_telemetry.py:321-322
  if (the source predicate pricing is None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:322-322
    End this invocation with None.
  }
  // Source: vvaharness/util/stage_telemetry.py:323-323
  In source order: Evaluate once 0.0; assign in source target order to total.
  // Source: vvaharness/util/stage_telemetry.py:324-330
  for each (role, bucket) in phases {
    // Source: vvaharness/util/stage_telemetry.py:325-325
    In source order: Evaluate once _rate_for(role, role_models, pricing); assign in source target order to rate.
    // Source: vvaharness/util/stage_telemetry.py:326-330
    if (the source predicate rate is not None is truthy) {
      // Source: vvaharness/util/stage_telemetry.py:328-328
      In source order: Apply source augmented assignment total += bucket_cost_usd(bucket, rate, pricing.cache_defaults) with source evaluation/in-place semantics.
    }
    else {
      // Source: vvaharness/util/stage_telemetry.py:329-330
      if (the source predicate _has_tokens(bucket) is truthy) {
        // Source: vvaharness/util/stage_telemetry.py:330-330
        End this invocation with None.
      }
    }
  }
  // Source: vvaharness/util/stage_telemetry.py:331-331
  End this invocation with total.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:334-342
// Source signature: _provenance_cost(model_id: str | None, bucket: TokenBucket, pricing: PricingTable | None) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _provenance_cost(model_id, bucket, pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:336-336
  In source order: Retain source documentation literal source_literal_336_4; it is not a model call.
  // Source: vvaharness/util/stage_telemetry.py:337-338
  if (the source predicate pricing is None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:338-338
    End this invocation with None.
  }
  // Source: vvaharness/util/stage_telemetry.py:339-339
  In source order: Evaluate once pricing.models.get(model_id) if model_id else None; assign in source target order to rate.
  // Source: vvaharness/util/stage_telemetry.py:340-341
  if (the source predicate rate is not None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:341-341
    End this invocation with bucket_cost_usd(bucket, rate, pricing.cache_defaults).
  }
  // Source: vvaharness/util/stage_telemetry.py:342-342
  End this invocation with None if _has_tokens(bucket) else 0.0.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:345-380
// Source signature: _stage_entry(stage_id: str, record: StageRecord | None, phases: Sequence[tuple[str | None, TokenBucket]], role_models: Mapping[str, str], pricing: PricingTable | None, provenance: StageProvenance | None=None) -> StageEntry
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _stage_entry(stage_id, record, phases, role_models, pricing, provenance) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:350-350
  In source order: Evaluate once STAGE_ROLES.get(stage_id); assign in source target order to role.
  // Source: vvaharness/util/stage_telemetry.py:351-368
  if (the source predicate provenance is not None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:353-359
    In source order: Evaluate once provenance.get('model'); assign in source target order to model. Then Evaluate once cast(TokenBucket, provenance.get('tokens') or {}); assign in source target order to raw_tokens. Then Evaluate once _sum_buckets([bucket for _, bucket in phases]); assign in source target order to live_tokens. Then Evaluate once _sum_buckets([raw_tokens, live_tokens]); assign in source target order to tokens. Then Evaluate once _provenance_cost(model, raw_tokens, pricing); assign in source target order to cached_cost.
    // Source: vvaharness/util/stage_telemetry.py:360-363
    In source order: Evaluate once _stage_cost(phases, role_models, pricing); assign in source target order to live_cost. Then Evaluate once None if cached_cost is None or live_cost is None else cached_cost + live_cost; assign in source target order to cost. Then Evaluate once provenance.get('config_sha256'); assign in source target order to cached_from_config_sha.
  }
  else {
    // Source: vvaharness/util/stage_telemetry.py:365-368
    In source order: Evaluate once _resolve_model(role, role_models); assign in source target order to model. Then Evaluate once _sum_buckets([bucket for _, bucket in phases]); assign in source target order to tokens. Then Evaluate once _stage_cost(phases, role_models, pricing); assign in source target order to cost. Then Evaluate once None; assign in source target order to cached_from_config_sha.
  }
  // Source: vvaharness/util/stage_telemetry.py:369-380
  End this invocation with StageEntry(label=record['label'] if record else '', outcome=record['outcome'] if record else _NOT_RUN, duration_sec=record['duration_sec'] if record else None, tokens=tokens, model=model, cost_usd=cost, cost_estimated=stage_id in ESTIMATED_COST_STAGES or any((r in ESTIMATED_COST_ROLES and _has_tokens(b) for r, b in phases)), cached_from_config_sha=cached_from_config_sha).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:383-388
// Source signature: _total_cost(stages: Mapping[str, StageEntry]) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _total_cost(stages) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:384-385
  In source order: Evaluate once [entry['cost_usd'] for entry in stages.values()]; assign in source target order to costs. Then Evaluate once [c for c in costs if c is not None]; assign in source target order to priced.
  // Source: vvaharness/util/stage_telemetry.py:386-387
  if (the source predicate len(priced) != len(costs) is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:387-387
    End this invocation with None.
  }
  // Source: vvaharness/util/stage_telemetry.py:388-388
  End this invocation with sum(priced).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:391-422
// Source signature: _totals(token_snap: TokenSnapshot, stages: Mapping[str, StageEntry], unattributed: UnattributedTokens, cached_provenance: Mapping[str, StageProvenance]) -> Totals
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _totals(token_snap, stages, unattributed, cached_provenance) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:394-404
  In source order: Evaluate once token_snap.get('by_phase', {}); assign in source target order to by_phase. Then Evaluate once _sum_buckets(list(by_phase.values())); assign in source target order to combined. Then Evaluate once sum((b.get('cache_unparsed', 0) for b in by_phase.values() if isinstance(b.get('cache_unparsed'), int))); assign in source target order to cache_unparsed_calls. Then Evaluate once _sum_buckets([cast(TokenBucket, prov.get('tokens') or {}) for prov in cached_provenance.values()]); assign in source target order to cached_carryover.
  // Source: vvaharness/util/stage_telemetry.py:405-422
  End this invocation with Totals(prompt_tokens=token_snap.get('prompt', 0) + cached_carryover['prompt'], completion_tokens=token_snap.get('completion', 0) + cached_carryover['completion'], total_tokens=token_snap.get('total', 0) + cached_carryover['prompt'] + cached_carryover['completion'], cache_read_tokens=combined.get('cache_read', 0) + cached_carryover['cache_read'], cache_write_tokens=combined.get('cache_write', 0) + cached_carryover['cache_write'], calls=token_snap.get('calls', 0) + cached_carryover['calls'], calls_with_usage=token_snap.get('calls_with_usage', 0), completion_absent=token_snap.get('completion_absent', 0), cache_unparsed_calls=cache_unparsed_calls, cost_usd=_total_cost(stages), unattributed=unattributed, cached_carryover=cached_carryover).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:425-429
// Source signature: _provenance(pricing: PricingTable | None) -> PricingProvenance | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _provenance(pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:426-427
  if (the source predicate pricing is None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:427-427
    End this invocation with None.
  }
  // Source: vvaharness/util/stage_telemetry.py:428-429
  End this invocation with PricingProvenance(file=pricing.path, sha256=pricing.sha256, source=pricing.source).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:432-443
// Source signature: _pricing_status(stages: Mapping[str, StageEntry], pricing: PricingTable | None) -> PricingStatus
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _pricing_status(stages, pricing) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:434-435
  if (the source predicate pricing is None is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:435-435
    End this invocation with {'status': 'unavailable', 'reason': 'no pricing table configured'}.
  }
  // Source: vvaharness/util/stage_telemetry.py:436-437
  In source order: Evaluate once sorted({entry['model'] for entry in stages.values() if entry['cost_usd'] is None and entry['model']}); assign in source target order to unpriced.
  // Source: vvaharness/util/stage_telemetry.py:438-442
  if (the source predicate unpriced is truthy) {
    // Source: vvaharness/util/stage_telemetry.py:439-442
    End this invocation with {'status': 'incomplete', 'reason': 'pricing missing for model(s): ' + ', '.join(unpriced)}.
  }
  // Source: vvaharness/util/stage_telemetry.py:443-443
  End this invocation with {'status': 'available', 'reason': 'pricing table applied'}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:446-451
// Source signature: _ordered_stage_ids(stage_snap: Mapping[str, StageRecord], by_stage: Mapping[str, object]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ordered_stage_ids(stage_snap, by_stage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:448-450
  In source order: Evaluate once set(stage_snap) | set(by_stage); assign in source target order to present. Then Evaluate once [s for s in STAGE_IDS if s in present]; assign in source target order to known. Then Evaluate once [s for s in stage_snap if s not in STAGE_IDS]; assign in source target order to extra.
  // Source: vvaharness/util/stage_telemetry.py:451-451
  End this invocation with known + extra.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/stage_telemetry.py:454-474
// Source signature: compose_stage_section(stage_snap: Mapping[str, StageRecord], token_snap: TokenSnapshot, role_models: Mapping[str, str], pricing: PricingTable | None, cached_provenance: Mapping[str, StageProvenance] | None=None) -> StageSection
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn compose_stage_section(stage_snap, token_snap, role_models, pricing, cached_provenance) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/stage_telemetry.py:460-469
  In source order: Retain source documentation literal source_literal_460_4; it is not a model call. Then Evaluate once _group_phases(token_snap); assign in source target order to (by_stage, unattributed). Then Evaluate once cached_provenance or {}; assign in source target order to cached_provenance. Then Evaluate once {stage_id: _stage_entry(stage_id, stage_snap.get(stage_id), by_stage.get(stage_id, []), role_models, pricing, cached_provenance.get(stage_id)) for stage_id in _ordered_stage_ids(stage_snap, by_stage)}; assign in source target order to stages.
  // Source: vvaharness/util/stage_telemetry.py:470-474
  End this invocation with StageSection(stages=stages, totals=_totals(token_snap, stages, unattributed, cached_provenance), pricing=_provenance(pricing), pricing_status=_pricing_status(stages, pricing)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util.pricing import ModelPricing, PricingTable, TokenBucket, bucket_cost_usd` at source line 24: `source_detail/vvaharness/util/pricing.py.sudo.md`.
- `from vvaharness.orchestrator.checkpoints import StageProvenance` at source line 32: `source_detail/vvaharness/orchestrator/checkpoints.py.sudo.md`.
