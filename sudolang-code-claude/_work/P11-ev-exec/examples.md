# P11-ev-exec examples

## 1. Request gates (budget, method policy, destructive token)
Source `vvaharness/exploit_verification/executor/_core.py:154-174`:
```python
    if state["n"] >= max_requests:
        return f"ERROR: request budget exhausted ({max_requests} requests) for this finding"
    if method not in allowed_methods:
        if method in DESTRUCTIVE_METHODS:
            why = "set allow_state_changing_methods: true AND safe_mode: false to enable it"
        elif method in MUTATING_METHODS:
            why = "set allow_state_changing_methods: true in the profile to enable it"
        else:
            why = "not a recognised HTTP method"
        return f"ERROR: method {method} is not permitted — {why}"
    path, query, body, extra_headers, oob_nonce = _resolve_oob(
        oob, path, query, body, extra_headers, finding_id, oob_family)
    tok = destructive_token(path, json.dumps(query), json.dumps(body) if body else "",
                            json.dumps(extra_headers) if extra_headers else "")
    if tok:
        return f"ERROR: refused — request contains a destructive token {tok!r}"
```
SudoLang `vvah/vvaharness/exploit_verification/executor/_core.sudo`:
```
  require state.n < max_requests => return "ERROR: request budget exhausted ($max_requests requests) for this finding"
  require method in allowed_methods => { why = match (method) { ... }; return "ERROR: method $method is not permitted — $why" }
  [path, query, body, extra_headers, oob_nonce] = _resolve_oob(oob, path, query, body, extra_headers, finding_id, oob_family)
  tok = destructive_token(path, json(query), if (body) json(body) else "", if (extra_headers) json(extra_headers) else "")
  require !tok => return "ERROR: refused — request contains a destructive token '$tok'"
```

## 2. Mapping chunk retry
Source `vvaharness/exploit_verification/mapping/finding_map.py:240-260` (retry while attempts remain, unless the failure is deterministic; `_ATTEMPTS = 2`).
SudoLang `vvah/vvaharness/exploit_verification/mapping/finding_map.sudo` `_map_chunk`: `for each attempt in 1..max(1, attempts) { try ...; catch exc => { if (attempt < max(1, attempts) && !is_deterministic_failure(exc)) continue; ...; break }; answers = json_objects(text); if (answers) break }`.

## 3. Replay decision ladder
Source `vvaharness/exploit_verification/replay/run.py:215-280`: removed (404/410) -> INCONCLUSIVE; nothing landed -> INCONCLUSIVE; OOB callback -> STILL_VULNERABLE; oracle re-fire -> STILL_VULNERABLE; unchanged response -> STILL_VULNERABLE; baseline drift -> INCONCLUSIVE; variants (if `ev_replay_variants`) -> STILL_VULNERABLE; else remediation judge.
SudoLang `vvah/vvaharness/exploit_verification/replay/run.sudo` `_replay_one`, same order with each reason string.
