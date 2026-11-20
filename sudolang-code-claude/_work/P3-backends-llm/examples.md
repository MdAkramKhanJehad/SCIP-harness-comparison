# Examples: P3-backends-llm

## 1. CLI retry gate and backoff (authentication retries, hard usage cap, transient retries)

Source `vvaharness/backends/llm/cli/retry.py:303-322`:
```python
        if _is_auth_failure(result):
            if auth_attempt < _AUTH_MAX_RETRIES:
                wait = _AUTH_BACKOFF[min(auth_attempt, len(_AUTH_BACKOFF) - 1)]
                ...
                time.sleep(wait)
                auth_attempt += 1
                _rotate_session_id(cmd)
                continue
            raise AuthenticationError(redact(err_text)[:400], status_code=401,
                                      backend="cli")
        if _RL_HARD_CAP.search(err_text):
            console.write(f"    [cli] {label}: hard usage cap reached — not retrying")
            return result
        if attempt >= _RL_MAX_RETRIES or not _is_transient_failure(result):
            return result
        wait = _RL_BACKOFF[min(attempt, len(_RL_BACKOFF) - 1)]
```

SudoLang `vvah/vvaharness/backends/llm/cli/retry.sudo` (`_run_with_retry`):
```
    if (_is_auth_failure(result)) {
      if (auth_attempt < _AUTH_MAX_RETRIES) {
        wait = _AUTH_BACKOFF[min(auth_attempt, 2)]
        sleep(wait)   // preserved: this sleep does not poll the abort flag, unlike the transient backoff below
        auth_attempt += 1
        _rotate_session_id(cmd)
        continue
      }
      throw AuthenticationError(redact(err_text)[:400], status_code=401, backend="cli")
    }
    if (_RL_HARD_CAP matches err_text) { console "hard usage cap reached — not retrying"; return result }
    if (attempt >= _RL_MAX_RETRIES || !_is_transient_failure(result)) return result
    wait = _RL_BACKOFF[min(attempt, 3)]
```

## 2. Structured-submit rejection and re-ask cap (model instruction plus code check)

Source `vvaharness/backends/llm/sdk.py:1495-1538` (condensed, logging lines dropped):
```python
if response_model is not None and b.name == _RESPONSE_MODEL_TOOL_NAME:
    try:
        validated = response_model.model_validate(b.input)
    except Exception as exc:
        submit_rejects += 1
        COUNTERS.bump("llm_structured_submit_rejected")
        if submit_rejects >= STRUCTURED_REASK_MAX:
            ...
            return json.dumps(dict(b.input or {}))
        results.append({... "content": (f"Rejected: {str(exc)[:600]}. Fix the named "
                                        f"fields and call the tool again."),})
        continue
    if submit_guard is not None:
        hold_text = submit_guard()
        if hold_text is not None:
            results.append({... "content": hold_text}); continue
    return validated.model_dump_json()
```

SudoLang `vvah/vvaharness/backends/llm/sdk.sudo`:
```
if (response_model && b.name == "emit_structured_response") {
  try validated = response_model.model_validate(b.input)
  catch exc => {
    submit_rejects += 1; COUNTERS.bump("llm_structured_submit_rejected")
    if (submit_rejects >= STRUCTURED_REASK_MAX) {   // 2
      errlog "emit_structured_response rejected $submit_rejects time(s); raw submit returned" (reason "llm_structured_reask_gave_up", recovered)
      return JSON of b.input
    }
    results.append(tool_result(b.id, "Rejected: <first 600 characters of the error>. Fix the named fields and call the tool again."))
    continue
  }
  if (submit_guard) { hold_text = submit_guard(); if (hold_text != null) { results.append(tool_result(b.id, hold_text)); continue } }
  return validated.model_dump_json()
}
```

## 3. Deep-agents classified retry ladder

Source `vvaharness/backends/llm/deepagents.py:403-431` (console-write lines 422-426 omitted, comments trimmed; `_TRANSIENT_ATTEMPTS = 3` at line 344):
```python
def _call_classified(call, *, model_id, tag, budget=None):
    attempt = 0
    session_t0 = time.monotonic()
    remaining = budget
    while True:
        attempt += 1
        try:
            return call(remaining)
        except Exception as exc:
            mapped = _classify_failure(exc, model_id=model_id, tag=tag)
            if mapped is not None:
                refusal = _refusal_or_raise(mapped, exc)
                break
            if attempt >= _TRANSIENT_ATTEMPTS or not _transient_failure(exc):
                raise
            wait = _transient_wait(exc, session_t0=session_t0, budget=budget, tag=tag)
            time.sleep(wait)
            remaining = None if budget is None else turn_timeout(session_t0, budget, budget)
    raise refusal
```

SudoLang `vvah/vvaharness/backends/llm/deepagents.sudo`:
```
// src: vvaharness/backends/llm/deepagents.py:403-431
fn _call_classified(call, model_id, tag, budget?):executor=code {
  attempt = 0; session_t0 = now; remaining = budget
  loop {
    attempt += 1
    try return call(remaining)
    catch exc => {
      mapped = _classify_failure(exc, model_id, tag)
      if (mapped != null) {
        if (mapped is not ModelRefusal) throw mapped
        refusal = mapped; break
      }
      if (attempt >= _TRANSIENT_ATTEMPTS || !_transient_failure(exc)) throw exc
      wait = _transient_wait(exc, session_t0, budget, tag)
      sleep(wait)
      remaining = if (budget == null) null else turn_timeout(session_t0, budget, budget)
    }
  }
  throw refusal
}
```
