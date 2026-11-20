# orchestrator/checkpoints.py — typed checkpoint facade

Executable code. SQLite connection/schema/filesystem policy implementation is
in `orchestrator/store/` is expanded under source_detail/. This facade describes its own SQL.

```sudo
// Source: vvaharness/orchestrator/checkpoints.py:45-93
fn s4_input_kind(checkpoint) {
  if (checkpoint contains "input_kind") { yield checkpoint.input_kind and end this call }
  findings = checkpoint.get("findings", [])
  outcomes = checkpoint.get("outcomes", {})
  origins = distinct string finding.origin, using "external" when missing or falsey
  if (findings && outcomes == dictionary mapping each origin to "confirmed") { yield "external" }
  else { yield "deepdive" }
}
fn s4_stage_complete(checkpoint) {
  outcomes = checkpoint.get("outcomes", {})
  Yield no outcome belongs to ["error", "halted", "uninvestigated", "failed"].
  Empty/missing outcomes therefore pass this predicate; "guardrail" and "skipped" also pass.
}

// Source: vvaharness/orchestrator/checkpoints.py:96-206
REPO_IDENTITY_STEP = "repo_identity"
EV_COLLECTION_STEP = "ev_collection"
fn _schema_for(step) {
  Fixed schemas:
    s0: SeedPackage; s1: ContextPackage; s2: ThreatModel; s3: TaskManifest;
    s4: {findings, outcomes, optional input_kind in [deepdive, external]};
    s5: {findings, pre_dropped}; s6: {verified, dropped};
    s7: six-tuple [pre_dropped, verified, dropped, canonical, dup_dropped, integer]
      OR five-tuple omitting final integer;
    s8: FinalReport; s9: string; ingest: boolean; repo_identity: string.
  if (step is fixed) { yield its TypeAdapter and end this call }
  if (step ends "_prov" && prefix before suffix is a fixed step) {
    yield TypeAdapter(StageProvenance) and end this call
  }
  if (step == "ev_collection") { lazily cache/yield TypeAdapter(NormalizedCollection) }
  else if (step starts "remediate_") { yield TypeAdapter(dictionary) }
  else if (step starts "validate_") { lazily cache/yield TypeAdapter(ValidationResult) }
  else { raise KeyError through fixed-schema lookup }
}
interface StageProvenance { model; via; config_sha256; tokens }

// Source: vvaharness/orchestrator/checkpoints.py:209-238
fn step_key_for(prefix, engine_id, engine_version, case_id, model="", backend="") {
  if (prefix not in ["remediate_", "validate_"]) { raise ValueError }
  material = newline-joined [engine_id, engine_version, case_id, model, backend], encoded to bytes
  yield prefix + first 24 hexadecimal characters of SHA-256(material)
}
fn prune_stale_steps(run_id, prefix, live_keys) {
  if ([run_id, prefix] already in process-local _PRUNED) { yield [] and end this call }
  Add pair to _PRUNED BEFORE calling store.delete_steps(run_id, prefix, set(live_keys)).
  Log nonempty removed keys; yield removed keys.
}
_CKPT_MAX_BYTES = 100 * 1024 * 1024

// Source: vvaharness/orchestrator/checkpoints.py:241-301
fn save_ckpt(ckpt_dir, run_id, step, obj) {
  Ignore ckpt_dir; blob = _schema_for(step).dump_json(obj).
  if (len(blob) > _CKPT_MAX_BYTES) { warn; end this call without saving }
  Connect store; in ONE transaction:
    Insert parent run if missing with empty repo_root.
    Update run.updated_at using SQLite datetime('now').
    Insert or replace checkpoint row [run_id, step, blob, len(blob)].
  Always close connection; after success print saved step.
}
fn load_ckpt(ckpt_dir, run_id, step) {
  Ignore ckpt_dir; connect, fetch payload/size for [run_id, step], always close.
  if (row absent) { print state-dir hint only for s1; yield None and end this call }
  if (size > _CKPT_MAX_BYTES) { warn; yield None and end this call }
  Validate payload via _schema_for(step).validate_json.
  On ValidationError or ValueError:
    Parse payload with json.loads to distinguish invalid JSON from schema mismatch;
    warn accordingly; yield None.
  Otherwise print resumed step and yield typed object.
  KeyError for an unknown schema is not caught here.
}

// Source: vvaharness/orchestrator/checkpoints.py:304-321
fn save_stage_provenance(ckpt_dir, run_id, step, model, via, config_sha256, tokens) {
  save_ckpt(ckpt_dir, run_id, step + "_prov", {model, via, config_sha256, tokens:copy of tokens})
}
fn load_stage_provenance(ckpt_dir, run_id, step) { load_ckpt(ckpt_dir, run_id, step + "_prov") }
fn run_id_for(repo) { first 32 hexadecimal characters of SHA-256(encoded resolved absolute repo path) }

// Source: vvaharness/orchestrator/checkpoints.py:324-357
fn prune_checkpoints(keep_runs=100, max_age_days=5, dry_run=false) {
  db = store.db_location()
  if (!db.exists()) { yield {root:string db, kept:0, deleted:[]} and end this call }
  Connect; count total runs.
  victims = runs older than max_age_days OR outside most-recent keep_runs by updated_at,
    ordered by updated_at. Tie order is not additionally specified.
  if (!dry_run && victims) {
    Delete victim run rows in one transaction; dependent-row cascade belongs to store schema.
    Fetch all incremental_vacuum results; truncate WAL checkpoint; delete each victim's graphs.
  }
  Always close connection.
  Yield {root:string db, kept:total-len(victims), deleted:victims}, including in dry_run.
}
```

The four-tuple fallback in `scan.py` is retained there. This file's S7 schema
accepts only five or six elements. No reconciliation is invented.

<!-- converted-model-instructions -->
Requested model behavior is expanded in the [prompt workflow map](../../../prompt_workflow.sudo.md).

- [vvaharness/orchestrator/checkpoints.py](../../../prompt_representation/vvaharness/orchestrator/checkpoints.py.sudo.md)
