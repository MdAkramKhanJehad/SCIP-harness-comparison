# vvaharness/orchestrator/checkpoints.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/checkpoints.py.evidence.json`. SHA-256: `7f2b6e3112404b943b45af63c235bfd027bf8805d22ca08babecb3dc6a79a709`.

```sudo
// Source: vvaharness/orchestrator/checkpoints.py:16-21
In source order: Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Retain source documentation literal source_literal_19_0; it is not a model call. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/checkpoints.py:22-27
In source order: Resolve source import from collections.abc import Iterable, Mapping; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from pydantic import TypeAdapter, ValidationError; preserve alias and import-time effects. Then Resolve source import from typing import Literal; preserve alias and import-time effects. Then Resolve source import from typing_extensions import NotRequired, TypedDict; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/checkpoints.py:29-40
In source order: Resolve source import from vvaharness.models import ContextPackage, DroppedFinding, FinalReport, Finding, TaskManifest, ThreatModel; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.scan import SeedPackage; preserve alias and import-time effects. Then Resolve source import from vvaharness.orchestrator import store; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/checkpoints.py:42-42
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/orchestrator/checkpoints.py:46-49
interface _S4Ckpt {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/checkpoints.py:47-49
  In source order: For findings, declare without assigning a value; source annotation list[Finding]. Then For outcomes, declare without assigning a value; source annotation dict[str, str]. Then For input_kind, declare without assigning a value; source annotation NotRequired[Literal['deepdive', 'external']].
}
// Source: vvaharness/orchestrator/checkpoints.py:52-60
// Source signature: s4_input_kind(checkpoint: dict) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn s4_input_kind(checkpoint) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:53-54
  if (the source predicate 'input_kind' in checkpoint is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:54-54
    End this invocation with checkpoint['input_kind'].
  }
  // Source: vvaharness/orchestrator/checkpoints.py:55-57
  In source order: Evaluate once checkpoint.get('findings', []); assign in source target order to findings. Then Evaluate once checkpoint.get('outcomes', {}); assign in source target order to outcomes. Then Evaluate once {str(getattr(finding, 'origin', None) or 'external') for finding in findings}; assign in source target order to origins.
  // Source: vvaharness/orchestrator/checkpoints.py:58-59
  if (the source predicate findings and outcomes == dict.fromkeys(origins, 'confirmed') is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:59-59
    End this invocation with 'external'.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:60-60
  End this invocation with 'deepdive'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:64-64
In source order: Evaluate once frozenset({'error', 'halted', 'uninvestigated', 'failed'}); assign in source target order to _S4_UNTRUSTED_OUTCOMES.
// Source: vvaharness/orchestrator/checkpoints.py:67-70
// Source signature: s4_stage_complete(checkpoint: dict) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn s4_stage_complete(checkpoint) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:68-69
  In source order: Retain source documentation literal source_literal_68_4; it is not a model call. Then Evaluate once checkpoint.get('outcomes', {}); assign in source target order to outcomes.
  // Source: vvaharness/orchestrator/checkpoints.py:70-70
  End this invocation with not any((outcome in _S4_UNTRUSTED_OUTCOMES for outcome in outcomes.values())).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:73-75
interface _S5Ckpt {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/checkpoints.py:74-75
  In source order: For findings, declare without assigning a value; source annotation list[Finding]. Then For pre_dropped, declare without assigning a value; source annotation list[DroppedFinding].
}
// Source: vvaharness/orchestrator/checkpoints.py:78-80
interface _S6Ckpt {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/checkpoints.py:79-80
  In source order: For verified, declare without assigning a value; source annotation list[Finding]. Then For dropped, declare without assigning a value; source annotation list[DroppedFinding].
}
// Source: vvaharness/orchestrator/checkpoints.py:84-97
In source order: Evaluate once tuple[list[DroppedFinding], list[Finding], list[DroppedFinding], list[Finding], list[DroppedFinding], int] | tuple[list[DroppedFinding], list[Finding], list[DroppedFinding], list[Finding], list[DroppedFinding]]; assign in source target order to _S7Ckpt. Then Evaluate once 'repo_identity'; assign in source target order to REPO_IDENTITY_STEP.
// Source: vvaharness/orchestrator/checkpoints.py:100-120
interface StageProvenance {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/orchestrator/checkpoints.py:101-120
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call. Then For model, declare without assigning a value; source annotation str | None. Then For via, declare without assigning a value; source annotation str | None. Then For config_sha256, declare without assigning a value; source annotation str | None. Then For tokens, declare without assigning a value; source annotation dict[str, int | float | None].
}
// Source: vvaharness/orchestrator/checkpoints.py:124-126
In source order: Evaluate once '_prov'; assign in source target order to _PROVENANCE_SUFFIX. Then For _PROVENANCE_SCHEMA, assign TypeAdapter(StageProvenance); source annotation TypeAdapter.
// Source: vvaharness/orchestrator/checkpoints.py:129-130
// Source signature: _provenance_step(step: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _provenance_step(step) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:130-130
  End this invocation with source_template_130_11.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:133-158
In source order: For _STEP_SCHEMA, assign {'s0': TypeAdapter(SeedPackage), 's1': TypeAdapter(ContextPackage), 's2': TypeAdapter(ThreatModel), 's3': TypeAdapter(TaskManifest), 's4': TypeAdapter(_S4Ckpt), 's5': TypeAdapter(_S5Ckpt), 's6': TypeAdapter(_S6Ckpt), 's7': TypeAdapter(_S7Ckpt), 's8': TypeAdapter(FinalReport), 's9': TypeAdapter(str), 'ingest': TypeAdapter(bool), REPO_IDENTITY_STEP: TypeAdapter(str)}; source annotation dict[str, TypeAdapter]. Then For _REMEDIATE_STEP_SCHEMA, assign TypeAdapter(dict); source annotation TypeAdapter. Then Evaluate once 'remediate_'; assign in source target order to REMEDIATE_PREFIX. Then Evaluate once 'validate_'; assign in source target order to VALIDATE_PREFIX. Then For _DYNAMIC_PREFIXES, assign (REMEDIATE_PREFIX, VALIDATE_PREFIX); source annotation tuple[str, ...].
// Source: vvaharness/orchestrator/checkpoints.py:161-164
In source order: Evaluate once 24; assign in source target order to _STEP_DIGEST_CHARS. Then For _VALIDATE_STEP_SCHEMA, assign None; source annotation TypeAdapter | None.
// Source: vvaharness/orchestrator/checkpoints.py:167-173
// Source signature: _validate_schema() -> TypeAdapter
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_schema() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:168-169
  In source order: Retain source documentation literal source_literal_168_4; it is not a model call. Then Bind names in module scope: _VALIDATE_STEP_SCHEMA.
  // Source: vvaharness/orchestrator/checkpoints.py:170-172
  if (the source predicate _VALIDATE_STEP_SCHEMA is None is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:171-172
    In source order: Resolve source import from vvaharness.validation.models import ValidationResult; preserve alias and import-time effects. Then Evaluate once TypeAdapter(ValidationResult); assign in source target order to _VALIDATE_STEP_SCHEMA.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:173-173
  End this invocation with _VALIDATE_STEP_SCHEMA.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:177-179
In source order: Evaluate once 'ev_collection'; assign in source target order to EV_COLLECTION_STEP. Then For _EV_COLLECTION_SCHEMA, assign None; source annotation TypeAdapter | None.
// Source: vvaharness/orchestrator/checkpoints.py:182-190
// Source signature: _ev_collection_schema() -> TypeAdapter
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ev_collection_schema() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:183-184
  In source order: Retain source documentation literal source_literal_183_4; it is not a model call. Then Bind names in module scope: _EV_COLLECTION_SCHEMA.
  // Source: vvaharness/orchestrator/checkpoints.py:185-189
  if (the source predicate _EV_COLLECTION_SCHEMA is None is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:186-189
    In source order: Resolve source import from vvaharness.exploit_verification.collection.model import NormalizedCollection; preserve alias and import-time effects. Then Evaluate once TypeAdapter(NormalizedCollection); assign in source target order to _EV_COLLECTION_SCHEMA.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:190-190
  End this invocation with _EV_COLLECTION_SCHEMA.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:193-206
// Source signature: _schema_for(step: str) -> TypeAdapter
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _schema_for(step) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:194-194
  In source order: Retain source documentation literal source_literal_194_4; it is not a model call.
  // Source: vvaharness/orchestrator/checkpoints.py:195-196
  if (the source predicate step in _STEP_SCHEMA is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:196-196
    End this invocation with _STEP_SCHEMA[step].
  }
  // Source: vvaharness/orchestrator/checkpoints.py:197-199
  if (the source predicate step.endswith(_PROVENANCE_SUFFIX) and step[:-len(_PROVENANCE_SUFFIX)] in _STEP_SCHEMA is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:199-199
    End this invocation with _PROVENANCE_SCHEMA.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:200-201
  if (the source predicate step == EV_COLLECTION_STEP is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:201-201
    End this invocation with _ev_collection_schema().
  }
  // Source: vvaharness/orchestrator/checkpoints.py:202-203
  if (the source predicate step.startswith(REMEDIATE_PREFIX) is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:203-203
    End this invocation with _REMEDIATE_STEP_SCHEMA.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:204-205
  if (the source predicate step.startswith(VALIDATE_PREFIX) is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:205-205
    End this invocation with _validate_schema().
  }
  // Source: vvaharness/orchestrator/checkpoints.py:206-206
  End this invocation with _STEP_SCHEMA[step].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:209-217
// Source signature: step_key_for(prefix: str, *, engine_id: str, engine_version: str, case_id: str, model: str='', backend: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn step_key_for(prefix, engine_id, engine_version, case_id, model, backend) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:211-211
  In source order: Retain source documentation literal source_literal_211_4; it is not a model call.
  // Source: vvaharness/orchestrator/checkpoints.py:212-215
  if (the source predicate prefix not in _DYNAMIC_PREFIXES is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:213-214
    In source order: Evaluate once source_template_213_15; assign in source target order to msg.
    // Source: vvaharness/orchestrator/checkpoints.py:215-215
    Raise ValueError(msg).
  }
  // Source: vvaharness/orchestrator/checkpoints.py:216-216
  In source order: Evaluate once source_literal_216_15.join((engine_id, engine_version, case_id, model, backend)).encode(); assign in source target order to material.
  // Source: vvaharness/orchestrator/checkpoints.py:217-217
  End this invocation with prefix + hashlib.sha256(material).hexdigest()[:_STEP_DIGEST_CHARS].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:221-221
In source order: For _PRUNED, assign set(); source annotation set[tuple[str, str]].
// Source: vvaharness/orchestrator/checkpoints.py:224-234
// Source signature: prune_stale_steps(run_id: str, prefix: str, live_keys: Iterable[str]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prune_stale_steps(run_id, prefix, live_keys) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:225-226
  In source order: Retain source documentation literal source_literal_225_4; it is not a model call. Then Evaluate once (run_id, prefix); assign in source target order to once.
  // Source: vvaharness/orchestrator/checkpoints.py:227-228
  if (the source predicate once in _PRUNED is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:228-228
    End this invocation with [].
  }
  // Source: vvaharness/orchestrator/checkpoints.py:229-230
  In source order: Evaluate _PRUNED.add(once); retain side effects and discard the expression result. Then Evaluate once store.delete_steps(run_id, prefix, set(live_keys)); assign in source target order to removed.
  // Source: vvaharness/orchestrator/checkpoints.py:231-233
  if (the source predicate removed is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:232-233
    In source order: Evaluate console.write(source_template_232_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:234-234
  End this invocation with removed.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:238-238
In source order: Evaluate once 100 * 1024 * 1024; assign in source target order to _CKPT_MAX_BYTES.
// Source: vvaharness/orchestrator/checkpoints.py:241-263
// Source signature: save_ckpt(ckpt_dir: Path, run_id: str, step: str, obj) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn save_ckpt(ckpt_dir, run_id, step, obj) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:242-244
  In source order: Retain source documentation literal source_literal_242_4; it is not a model call. Then Delete source targets in order: ckpt_dir. Then Evaluate once _schema_for(step).dump_json(obj); assign in source target order to blob.
  // Source: vvaharness/orchestrator/checkpoints.py:245-247
  if (the source predicate len(blob) > _CKPT_MAX_BYTES is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:246-246
    In source order: Evaluate log.warning(Event.CKPT_TOO_LARGE, step=step, size=len(blob), cap=_CKPT_MAX_BYTES); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/checkpoints.py:247-247
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:248-248
  In source order: Evaluate once store.connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/checkpoints.py:249-262
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/checkpoints.py:250-260
    Enter source context managers left-to-right: con {
      // Source: vvaharness/orchestrator/checkpoints.py:252-260
      In source order: Evaluate con.execute("INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')", (run_id,)); retain side effects and discard the expression result. Then Evaluate con.execute("UPDATE runs SET updated_at = datetime('now') WHERE run_id = ?", (run_id,)); retain side effects and discard the expression result. Then Evaluate con.execute('INSERT OR REPLACE INTO checkpoints(run_id, step, payload, size) VALUES (?, ?, ?, ?)', (run_id, step, blob, len(blob))); retain side effects and discard the expression result.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/checkpoints.py:262-262
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:263-263
  In source order: Evaluate console.write(source_template_263_18); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:266-301
// Source signature: load_ckpt(ckpt_dir: Path, run_id: str, step: str)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_ckpt(ckpt_dir, run_id, step) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:267-269
  In source order: Retain source documentation literal source_literal_267_4; it is not a model call. Then Delete source targets in order: ckpt_dir. Then Evaluate once store.connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/checkpoints.py:270-276
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/checkpoints.py:271-274
    In source order: Evaluate once con.execute('SELECT payload, size FROM checkpoints WHERE run_id=? AND step=?', (run_id, step)).fetchone(); assign in source target order to row.
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/checkpoints.py:276-276
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:277-282
  if (the source predicate row is None is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:278-281
    if (the source predicate step == 's1' is truthy) {
      // Source: vvaharness/orchestrator/checkpoints.py:279-281
      In source order: Evaluate console.write(source_template_279_26); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/checkpoints.py:282-282
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:283-283
  In source order: Evaluate once row; assign in source target order to (payload, size).
  // Source: vvaharness/orchestrator/checkpoints.py:284-286
  if (the source predicate size > _CKPT_MAX_BYTES is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:285-285
    In source order: Evaluate log.warning(Event.CKPT_STORED_TOO_LARGE, step=step, cap=_CKPT_MAX_BYTES); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/checkpoints.py:286-286
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:287-299
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/checkpoints.py:288-288
    In source order: Evaluate once _schema_for(step).validate_json(payload); assign in source target order to obj.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:289-299
  On the first matching source exception (ValidationError, ValueError) as e, in handler order {
    // Source: vvaharness/orchestrator/checkpoints.py:291-298
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/checkpoints.py:292-292
      In source order: Evaluate json.loads(payload); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/checkpoints.py:293-295
    On the first matching source exception (ValueError, TypeError), in handler order {
      // Source: vvaharness/orchestrator/checkpoints.py:295-295
      In source order: Evaluate log.warning(Event.CKPT_UNREADABLE, step=step, detail=str(e)); retain side effects and discard the expression result.
    }
    Only when the protected body falls through normally, without exception, return, break or continue {
      // Source: vvaharness/orchestrator/checkpoints.py:298-298
      In source order: Evaluate log.warning(Event.CKPT_SCHEMA_MISMATCH, step=step, detail=str(e)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/orchestrator/checkpoints.py:299-299
    End this invocation with None.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:300-300
  In source order: Evaluate console.write(source_template_300_18); retain side effects and discard the expression result.
  // Source: vvaharness/orchestrator/checkpoints.py:301-301
  End this invocation with obj.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:304-311
// Source signature: save_stage_provenance(ckpt_dir: Path, run_id: str, step: str, *, model: str | None, via: str | None, config_sha256: str | None, tokens: Mapping[str, object]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn save_stage_provenance(ckpt_dir, run_id, step, model, via, config_sha256, tokens) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:308-311
  In source order: Retain source documentation literal source_literal_308_4; it is not a model call. Then Evaluate save_ckpt(ckpt_dir, run_id, _provenance_step(step), StageProvenance(model=model, via=via, config_sha256=config_sha256, tokens=dict(tokens))); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:314-316
// Source signature: load_stage_provenance(ckpt_dir: Path, run_id: str, step: str) -> StageProvenance | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_stage_provenance(ckpt_dir, run_id, step) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:315-315
  In source order: Retain source documentation literal source_literal_315_4; it is not a model call.
  // Source: vvaharness/orchestrator/checkpoints.py:316-316
  End this invocation with load_ckpt(ckpt_dir, run_id, _provenance_step(step)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:319-321
// Source signature: run_id_for(repo: str | Path) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn run_id_for(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:320-320
  In source order: Retain source documentation literal source_literal_320_4; it is not a model call.
  // Source: vvaharness/orchestrator/checkpoints.py:321-321
  End this invocation with hashlib.sha256(str(Path(repo).resolve()).encode()).hexdigest()[:32].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/checkpoints.py:324-357
// Source signature: prune_checkpoints(*, keep_runs: int=100, max_age_days: int=5, dry_run: bool=False) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn prune_checkpoints(keep_runs, max_age_days, dry_run) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/checkpoints.py:326-328
  In source order: Retain source documentation literal source_literal_326_4; it is not a model call. Then Evaluate once store.db_location(); assign in source target order to db.
  // Source: vvaharness/orchestrator/checkpoints.py:329-330
  if (the source predicate not db.exists() is truthy) {
    // Source: vvaharness/orchestrator/checkpoints.py:330-330
    End this invocation with {'root': str(db), 'kept': 0, 'deleted': []}.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:331-331
  In source order: Evaluate once store.connect(); assign in source target order to con.
  // Source: vvaharness/orchestrator/checkpoints.py:332-354
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/checkpoints.py:333-342
    In source order: Evaluate once con.execute('SELECT COUNT(*) FROM runs').fetchone()[0]; assign in source target order to total. Then Evaluate once [r[0] for r in con.execute(source_literal_335_12, (source_template_341_13, keep_runs))]; assign in source target order to victims.
    // Source: vvaharness/orchestrator/checkpoints.py:343-352
    if (the source predicate not dry_run and victims is truthy) {
      // Source: vvaharness/orchestrator/checkpoints.py:344-346
      Enter source context managers left-to-right: con {
        // Source: vvaharness/orchestrator/checkpoints.py:345-346
        In source order: Evaluate con.executemany('DELETE FROM runs WHERE run_id = ?', [(v,) for v in victims]); retain side effects and discard the expression result.
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
      // Source: vvaharness/orchestrator/checkpoints.py:349-350
      In source order: Evaluate con.execute('PRAGMA incremental_vacuum').fetchall(); retain side effects and discard the expression result. Then Evaluate con.execute('PRAGMA wal_checkpoint(TRUNCATE)'); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/checkpoints.py:351-352
      for each v in victims {
        // Source: vvaharness/orchestrator/checkpoints.py:352-352
        In source order: Evaluate store.delete_run_graphs(v); retain side effects and discard the expression result.
      }
    }
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vvaharness/orchestrator/checkpoints.py:354-354
    In source order: Evaluate con.close(); retain side effects and discard the expression result.
  }
  // Source: vvaharness/orchestrator/checkpoints.py:356-357
  End this invocation with {'root': str(db), 'kept': total - len(victims), 'deleted': victims}.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.models import ContextPackage, DroppedFinding, FinalReport, Finding, TaskManifest, ThreatModel` at source line 29: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.models.scan import SeedPackage` at source line 37: `source_detail/vvaharness/models/scan/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 38: `source_detail/vvaharness/orchestrator/__init__.py.sudo.md`.
- `from vvaharness.orchestrator import store` at source line 38: `source_detail/vvaharness/orchestrator/store/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 39: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 39: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 40: `source_detail/vvaharness/util/events.py.sudo.md`.
- `from vvaharness.validation.models import ValidationResult` at source line 171: `source_detail/vvaharness/validation/models/__init__.py.sudo.md`.
- `from vvaharness.exploit_verification.collection.model import NormalizedCollection` at source line 186: `source_detail/vvaharness/exploit_verification/collection/model.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/orchestrator/checkpoints.py.sudo.md). Exact strings in the evidence asset support this conversion.
