# s4_deepdive.py — unit scheduler and source packing

Executable. Pool futures run sessions concurrently; coordinator code handles
results. Completion order is not assumed to equal risk order.

```sudo
// Source: vvaharness/pipeline/stages/s4_deepdive.py:43-92
fn run(units, ctx, cfg) {
  tracker = cfg._scan_progress, default None
  repo_root = Path(ctx.repo_root)
  units = stable sort by risk_rank
  parallel = cfg.step4.parallel, default 12
  Validate deepdive_tools(cfg) BEFORE starting any pool.
  investigate = investigate_unit
  guardrail_hits=0; guardrail_gate=max(3, parallel); successes=0; outcomes={}
  for each unit in units {
    if (!unit.files) {
      Log empty_chunk_skipped; outcomes[unit.id]="skipped"; notify tracker if present.
    }
  }
  Remove file-less units from work list, keeping their outcomes.
  Define _guardrail_fail_fast to raise RuntimeError when called.

  // Source: vvaharness/pipeline/stages/s4_deepdive.py:93-152
  if (parallel <= 1) {
    all_findings=[]
    for each unit in units, in order {
      Label and mark scanning; create fresh unit_stats.
      Call investigate(unit, ctx, repo_root, cfg, stats=unit_stats).
      On GuardrailBlocked:
        Update guardrail_hits via guardrail_gate_hit; log; outcome="guardrail"; notify tracker.
        if (guardrail_hits >= guardrail_gate && successes == 0) { _guardrail_fail_fast(error) }
        Otherwise continue to next unit.
      On other Exception:
        if (cli.aborted()) { rethrow }
        if (is_halt_error(error)) {
          Log error; mark current and all later units "halted", notify tracker,
            bump count for that entire suffix; leave this loop.
        }
        Otherwise log error; mark this unit "error"; notify tracker; continue.
      On normal return increment successes, mark "completed", append findings, notify tracker.
    }
    Log outcome counts; print tracker summary when present.
    yield [all_findings, outcomes] and end this call.
    Serial execution does not use plan_batches or split retries.
  }

  // Source: vvaharness/pipeline/stages/s4_deepdive.py:154-190
  results={}; batches=plan_batches(units, _batch_size(cfg))
  split_retry=bool(knob(cfg, "step4.split_retry", true))
  ex = ThreadPoolExecutor(max_workers=parallel)
  futs={}; retry_futs={}
  Define _resubmit(unit): submit singleton through _submit_batch, store future in BOTH maps,
    bump s4_batch_member_resubmitted.
  Define _mark_halted(batches_to_mark): for each unit with no existing outcomes entry,
    mark "halted", store empty results, notify tracker; yield number newly marked.
  for each batch in batches {
    Label/mark scanning for each unit; submit _submit_batch(ex, batch, investigate, ctx, repo_root, cfg).
    Save future -> batch in futs.
  }
  halted=false

  // Source: vvaharness/pipeline/stages/s4_deepdive.py:192-279
  Process the initial as_completed(futs) iterator, in completion order.
  For each completed future's batch:
    Obtain [found, merged_by_unit, verdict_by_unit].
    On GuardrailBlocked: update gate count once for the batch, mark/log every member "guardrail",
      store empty results, notify tracker.
      if (guardrail_hits >= guardrail_gate && successes == 0) {
        cli.abort(); ex.shutdown(wait=false, cancel_futures=true); raise fail-fast RuntimeError.
      }
      Otherwise continue.
    On halt-class Exception:
      pending_batches = entries of futs whose futures are not done
      _mark_halted([current batch] + pending_batches)
      Log current batch, bump s4_units_halted by current batch size plus pending member count.
      cli.abort(); ex.shutdown(wait=false, cancel_futures=true); halted=true; leave initial loop.
    On other Exception:
      retryable = split_retry && len(batch)>1 && !is_deterministic_failure(error) && !cli.aborted()
      for each unit in batch {
        outcomes[unit.id]="error"
        if (retryable) { log recovered=true; _resubmit(unit) }
        else { log error; results[unit.id]=[]; notify tracker error }
      }
      Continue initial completion loop.
    On normal future return:
      successes += 1
      for each unit in batch {
        findings=found.get(unit.id, []); verdict=verdict_by_unit.get(unit.id)
        if (verdict in ["uninvestigated", "failed"]) {
          outcomes[unit.id]=verdict
          if (split_retry && len(batch)>1 && !cli.aborted()) { log recovered=true; _resubmit(unit) }
          else { log s4_batch_member_verdict; results[unit.id]=[]; notify tracker with verdict }
        } else { store findings; outcomes[unit.id]="completed"; notify tracker }
      }

  // Source: vvaharness/pipeline/stages/s4_deepdive.py:281-362
  if (!halted) {
    Process as_completed(retry_futs), in completion order, as a separate wave.
    On GuardrailBlocked: mark/log batch guardrail, same gate/fail-fast behavior.
    On halt-class Exception:
      pending_batches = not-done entries from futs PLUS not-done entries from retry_futs
      _mark_halted([current batch] + pending_batches)
      Log current batch; bump halted by current batch size plus pending member count;
        cli.abort(); shutdown without waiting/cancel pending; halted=true; leave retry loop.
      The maps overlap and existing outcome entries are skipped by _mark_halted;
        no extra de-duplication or overwrite of an earlier "error" is invented.
    On other Exception: mark/log batch error and empty results; notify tracker.
    On normal return: increment successes; store each found.get(unit.id, []), mark completed,
      bump recovered counter and notify tracker. No second split retry.
  }
  KeyboardInterrupt or SystemExit during either completion wave:
    cli.abort(); shutdown(wait=false, cancel_futures=true); rethrow.
  On every exit from the completion-wave protected region: ex.shutdown(wait=true).
  Initial submissions occur before that protected region, as in source.
  Reassemble all_findings by iterating units in stable risk_rank order and extending results.get(id, []).
  Log outcome counts, print tracker summary if present; yield [all_findings, outcomes].
}

// Source: vvaharness/pipeline/stages/s4_deepdive.py:365-390
fn _batch_size(cfg) { _cap_int(cfg.step4, "batch_size", 1) }
fn _submit_batch(ex, batch, investigate, ctx, repo_root, cfg) {
  if (len(batch)==1) {
    Submit callable invoking investigate with fresh stats, yielding
      [{id:findings}, {id:stats.get("merged",0)}, {}].
  } else {
    Submit callable invoking investigate_batch with fresh stats, yielding
      [out, stats.get("merged_by_unit",{}), verdict_by_unit].
  }
  Yield the future, not its result.
}

// Source: vvaharness/pipeline/stages/s4_deepdive.py:393-440
fn _build_shared_context_block(ctx) {
  parts=[]
  if (ctx.app_profile) { append ctx.app_profile.to_prompt_block() }
  if (ctx.threat_model) {
    Append to_compact_prompt_block(max_context_chars=4000, max_assets=10,
      max_boundaries=15, max_threats=25).
  }
  if (ctx.entry_points) {
    Sort entry points by [file,function], keep first 60; include shown/total count,
      auth/unauth tag, kind, file::function; include omitted count when needed.
  }
  Append literal TRUST RULE text (see exact prompt assets) even if other parts are absent.
  Join nonempty parts with blank lines.
}

// Source: vvaharness/pipeline/stages/s4_deepdive.py:445-501
fn _mask_pan(m) {
  Extract digits from matched run; if fewer than 13 yield unchanged.
  Inspect up to 48 characters immediately before run for _CARD_CTX.
  if (!(_luhn(digits) || _CARD_CTX matches preceding window)) { yield unchanged and end this call }
  Preserve first four digits and separators; replace remaining digits with X.
}
fn _redact_source(text, rel, stage="s4") {
  text=sanitize_packed_text(text, rel)
  Apply _PAN_RX, matching 13..19 digits with optional spaces/hyphens and word boundaries,
    replacing with _mask_pan; count only changed matches.
  [masked, counts] = redact_counts(result)
  Warn once per stage:rel when PAN or other-token counts are nonzero; yield masked.
  Use local counts, not shared redact.last_counts, in concurrent sessions.
}

// Source: vvaharness/pipeline/stages/s4_deepdive.py:504-525
fn _load_files_full(files, repo_root, stage="s4") {
  MAX_LINE_CHARS=8000; parts=[]
  for each rel in files {
    p=repo_root/rel
    if (!p.is_file()) { append file-not-found marker; continue to next file }
    Read UTF-8 with replacement; on Exception append read-error marker and continue.
    text=_redact_source(text, rel, stage)
    Prefix each split line with 1-based line number and vertical bar;
      retain only first 8000 characters of each source line.
    Append file header and numbered text.
  }
  Join parts with newlines. This function itself performs no total-file-size cap.
}
```

Exact regexes and shared-context wording remain available in the source and
the evidence extracts. Sanitizer/redactor internals are expanded under source_detail/.
