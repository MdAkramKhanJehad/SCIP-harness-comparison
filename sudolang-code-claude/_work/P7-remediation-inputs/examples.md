# Examples — P7-remediation-inputs

## 1. Policy gate decision order (gate)

Source `vvaharness/remediation_agent/policy_gate/gate.py:64-96` (excerpt):
```python
        if not self._loaded or d is None:
            return _FAIL_CLOSED
        if d.kill_env and os.environ.get(d.kill_env, "").strip().lower() in _TRUE:
            return Decision(Action.GUIDANCE_ONLY, "kill_switch_env")
        if d.kill_file and d.kill_file.exists():
            return Decision(Action.GUIDANCE_ONLY, "kill_switch_file")
        cwe = _norm_cwe(cwe_id)
        if not cwe:
            return Decision(Action.GUIDANCE_ONLY, "unmapped_cwe")
        if cwe in d.deny:
            return Decision(Action.GUIDANCE_ONLY, d.deny[cwe],
                            matched_rule=f"deny:{cwe}")
        ...
        if cwe in d.allow:
            return Decision(Action.PATCH, "allow_list", matched_rule=f"allow:{cwe}")
        return Decision(d.default, "default_action")
```
Rendering `vvah/vvaharness/remediation_agent/policy_gate/gate.sudo`:
```
    if (!_loaded) return _FAIL_CLOSED   // "policy_unavailable_fail_closed"
    if (_data.kill_env && lower case of trimmed environment[_data.kill_env] in _TRUE) return Decision(GUIDANCE_ONLY, "kill_switch_env")
    if (_data.kill_file && _data.kill_file exists) return Decision(GUIDANCE_ONLY, "kill_switch_file")
    cwe = loader._norm_cwe(cwe_id)
    if (!cwe) return Decision(GUIDANCE_ONLY, "unmapped_cwe")
    if (cwe in _data.deny) return Decision(GUIDANCE_ONLY, _data.deny[cwe], matched_rule="deny:$cwe")
    ...
    if (cwe in _data.allow) return Decision(PATCH, "allow_list", matched_rule="allow:$cwe")
    return Decision(_data.default, "default_action")
```

## 2. Fixer retry bound (retry cap)

Source `vvaharness/remediation_agent/plugin_runner/handoff.py:135-145`:
```python
    def _record_transient(self) -> None:
        if self._attempts < 2:
            self._retry_allowed = True
            ...
        else:
            self._terminal = True
```
Rendering `vvah/vvaharness/remediation_agent/plugin_runner/handoff.sudo`:
```
  // src: handoff.py:135-145 — at most two executed dispatches per session
  fn _record_transient():executor=code {
    if (_attempts < 2) { _retry_allowed = true; warn "fixer reported a transient tool error — one retry is permitted" }
    else { _terminal = true; warn "fixer transient retry exhausted — return Not Fixed" }
  }
```

## 3. Post-gate ACCEPT condition (threshold on model self-report)

Source `vvaharness/remediation_agent/policy/postgate.py:158-166`:
```python
    ceiling = pre.decision.action
    if not bad:
        patch_applied = bool(diff and diff.strip())
        gates_passed = (all_gates_passed and _gates_ok(verdict)
                        and patch_applied
                        and verdict.verdict in ("Fixed", "Partially Fixed"))
        return PostResult(reverted=[], matched_globs=[], downgraded=False,
                          final_verdict=cap_verdict(ceiling, gates_passed))
```
Rendering `vvah/vvaharness/remediation_agent/policy/postgate.sudo`:
```
  ceiling = pre.decision.action
  if (!bad) {
    patch_applied = diff is non-blank
    gates_passed = all_gates_passed && _gates_ok(verdict) && patch_applied && verdict.verdict in ["Fixed", "Partially Fixed"]
    return PostResult(reverted=[], matched_globs=[], downgraded=false, final_verdict=policy_gate.diffscan.cap_verdict(ceiling, gates_passed))
  }
```
