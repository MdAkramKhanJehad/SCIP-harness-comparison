# P10-ev-core examples

## 1. Judge downgrade rules enforced in code (gate on model output)

Source `vvaharness/exploit_verification/verify/judge.py:388-399`:
```python
    mechanism = _flag(obj, "mechanism_confirmed", default=False)
    prop_violated = _flag(obj, "property_violated", default=True)
    needs_second = _flag(obj, "requires_second_identity", default=False)

    # Enforced here, not in the caller: an unruled-out benign reading establishes nothing
    if verdict == "exploited" and _said_nothing(why_not):
        verdict = "insufficient_evidence"
        why_not = ""

    # Second rule: exploited must mean the CLAIM, not the mechanism; prose alone could not bind this
    if verdict == "exploited" and not prop_violated:
        verdict = "insufficient_evidence"
```
SudoLang `vvah/vvaharness/exploit_verification/verify/judge.sudo`:
```
  mechanism = _flag(obj, "mechanism_confirmed", default=false)
  prop_violated = _flag(obj, "property_violated", default=true)
  needs_second = _flag(obj, "requires_second_identity", default=false)
  // rule 1, enforced here: an unruled-out benign reading establishes nothing
  require !(verdict == "exploited" && _said_nothing(obj.why_not_benign)) => { verdict = "insufficient_evidence"; why_not = "" }
  // rule 2: exploited must mean the claim, not the mechanism
  require !(verdict == "exploited" && !prop_violated) => verdict = "insufficient_evidence"
```

## 2. Classifier model decision, with the CONFIRMABLE gate

Source `vvaharness/exploit_verification/classify/llm.py:190-210`:
```python
    if action == "skip":
        return Classification(VerifyClass.STATIC, None), "skip"
    if action != "attack":
        return table, "unparsed-action"       # unrecognised -> trust the table
    raw = answer.get("subtype")
    subtype = str(raw).strip().lower() if raw not in (None, "", "null") else None
    if subtype is None:
        return Classification(VerifyClass.ACTIVE, None), "agentic"
    if subtype not in CONFIRMABLE:
        return Classification(VerifyClass.ACTIVE, None), f"refused-subtype:{subtype}"
    cls = (VerifyClass.PASSIVE if subtype in _PASSIVE_CONFIRMABLE
           else VerifyClass.ACTIVE)
    return Classification(cls, subtype), subtype
```
SudoLang `vvah/vvaharness/exploit_verification/classify/llm.sudo`:
```
  if (action == "skip") return (Classification("static", null), "skip")   // routed to the static verifier, not dropped
  if (action != "attack") return (table, "unparsed-action")               // unrecognised: trust the table
  subtype = lowercase trimmed answer.subtype unless it is null, "" or "null"
  if (subtype == null) return (Classification("active", null), "agentic")
  if (subtype not in CONFIRMABLE) return (Classification("active", null), "refused-subtype:$subtype")
  return (Classification(if (subtype in _PASSIVE_CONFIRMABLE) "passive" else "active", subtype), subtype)
```

## 3. Time-based tell thresholds in the oracle

Source `vvaharness/exploit_verification/verify/oracle.py:95-105`:
```python
def _slow(rec, base) -> bool:
    if not _responded(rec):
        return False
    e = _elapsed(rec)
    b = _elapsed(base) if (base is not None and _responded(base)) else 0.0
    if b > 0:
        margin = min(max(_TIME_DELTA, _TIME_DELTA_FACTOR * b), _TIME_DELTA_CAP)
        return (e - b) >= margin
    return e >= _TIME_THRESHOLD
```
SudoLang `vvah/vvaharness/exploit_verification/verify/oracle.sudo` (constants 4.5, 3.0, 0.5, 4.0 at oracle.py:41-44):
```
fn _slow(rec, base):executor=code {
  if (!_responded(rec)) return false
  e = elapsed(rec); b = if (base responded) elapsed(base) else 0
  if (b > 0) return (e - b) >= min(max(_TIME_DELTA, _TIME_DELTA_FACTOR * b), _TIME_DELTA_CAP)
  return e >= _TIME_THRESHOLD
}
```
