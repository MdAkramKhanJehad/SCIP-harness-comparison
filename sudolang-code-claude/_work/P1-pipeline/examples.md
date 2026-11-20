# P1-pipeline examples

## 1. Repair gate on verdict material (s6/session.py:324-335)
Source:
```
    if abandoned():
        COUNTERS.bump("s6_outcome_repair_skipped_abandoned")
        return {}
    if not _has_verdict_material(raw):
        ...
        COUNTERS.bump("s6_outcome_repair_skipped_no_verdict")
        return {}
    COUNTERS.bump("s6_outcome_repaired_attempt")
```
SudoLang (vvah/vvaharness/pipeline/stages/s6/session.sudo):
```
  if (abandoned()) { COUNTERS.bump("s6_outcome_repair_skipped_abandoned"); return {} }
  require _has_verdict_material(raw) => { ...; COUNTERS.bump("s6_outcome_repair_skipped_no_verdict"); return {} }
  COUNTERS.bump("s6_outcome_repaired_attempt")
```

## 2. Settings-gated system prompt fragments (s6/prompts.py:236-250)
Source: `_GRAPH_DUTY if graph else "", ... _REFRAME_DUTY if reframe else "", ... _TRAIT_STAMP_DUTY if trait_stamps else ""`
SudoLang: `if (graph) _GRAPH_DUTY, ... if (reframe) _REFRAME_DUTY, ... if (trait_stamps) _TRAIT_STAMP_DUTY`. The caller passes `reframe = knob("step6_verify.reframe_enabled", default=false)`.

## 3. Code check on model-proposed merges (s7_dedup.py:99-104)
Source:
```
            if g_idx in canonical_of or g_canon >= g_idx:
                continue
            if cwe_conflict(verified[g_idx], verified[root(g_canon)]):
                blocked += 1
                continue
```
SudoLang (s7_dedup.sudo):
```
      require g_idx not in canonical_of && g_canon < g_idx => skip this row
      require !s7.collapse.cwe_conflict(verified[g_idx], verified[root(g_canon)]) => { blocked += 1; skip this row }
```
