# Examples, P9-skills-util

## 1. Degenerate-response gate with a consecutive cap (retry/threshold)

Source `vvaharness/util/response_quality.py:153-186` (excerpt):
```python
    with _lock:
        count = _consecutive.get(stage, 0) + 1
        _consecutive[stage] = count
    summary = "; ".join(reasons)
    if count < _DEGENERATE_MAX_CONSECUTIVE:
        log.warning(Event.RESPONSE_DEGENERATE_ACCEPTED, ...)
        _errlog.log(stage or "quality", stage or "response_quality",
            f"VVAH-E003 warning ({count}/{_DEGENERATE_MAX_CONSECUTIVE}): {summary}",
            ..., raw_head=redact(stripped)[:_RAW_HEAD_CHARS], recovered=True)
        return
    with _lock:
        _consecutive[stage] = 1
    char_axis_failed = len(stripped) < min_chars
    raise DegenerateResponseError(summary, stage=stage, response_len=len(stripped),
        threshold=min_chars if char_axis_failed else 0, consecutive=count)
```
SudoLang `vvah/vvaharness/util/response_quality.sudo`:
```
  count = _consecutive[stage] + 1; _consecutive[stage] = count
  if (count < _DEGENERATE_MAX_CONSECUTIVE) {
    warn RESPONSE_DEGENERATE_ACCEPTED (VVAH-E003, "count/3")
    errlog.log(stage or "quality", stage or "response_quality", "VVAH-E003 warning (count/3): reasons",
      error_code=DegenerateResponseError.error_code, raw_head=first 300 characters of redact(stripped), recovered=true)
    return
  }
  _consecutive[stage] = 1
  throw DegenerateResponseError(reasons, stage, response_len, threshold = if (character axis failed) min_chars else 0, consecutive=count)
```

## 2. Hard gate given to the model (model instruction)

Source `vvaharness/skills/access-control/SKILL.md:29-34`:
```
HARD GATE — for every finding you MUST show:
  (a) the entry point (controller/handler/route) and the identity it
      authenticates as, and
  (b) the object/resource it acts on and WHERE ownership/tenant/role is
      verified for THAT object.
If (b) exists and is correct, DROP the finding.
```
SudoLang `vvah/vvaharness/skills/access-control/SKILL.sudo.md`:
```
    constraint HardGate {
      "HARD GATE — for every finding you MUST show:
        (a) the entry point (controller/handler/route) and the identity it authenticates as, and
        (b) the object/resource it acts on and WHERE ownership/tenant/role is verified for THAT object."
      "If (b) exists and is correct, DROP the finding."
```

## 3. Shell probe cap and conditional reference tables (filter/limit)

Source `vvaharness/skills/ssrf/probe.sh:122-123, 145`:
```sh
SINKS=$FOUND
CAP=8
...
if [ -n "$SINKS" ]; then
```
SudoLang `vvah/vvaharness/skills/ssrf/probe.sudo`:
```
  SINKS = FOUND   // set when any scan() above printed a hit
  CAP = 8         // the posture section below shows at most 8 lines
  ...
  if (SINKS) {
    print fixed reference tables:
```
