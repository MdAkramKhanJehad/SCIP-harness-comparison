# vvaharness/report/cvss.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/report/cvss.py.evidence.json`. SHA-256: `9da81e06dd0ab50e226e648914c175f86e91579ab4e347692d7b06ff7b3e82db`.

```sudo
// Source: vvaharness/report/cvss.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Evaluate once re.compile(source_literal_21_4); assign in source target order to _VECTOR_RE. Then Evaluate once {'N': 0.85, 'A': 0.62, 'L': 0.55, 'P': 0.2}; assign in source target order to AV.
// Source: vvaharness/report/cvss.py:26-30
In source order: Evaluate once {'L': 0.77, 'H': 0.44}; assign in source target order to AC. Then Evaluate once {'N': 0.85, 'L': 0.62, 'H': 0.27}; assign in source target order to PR_SCOPE_UNCHANGED. Then Evaluate once {'N': 0.85, 'L': 0.68, 'H': 0.5}; assign in source target order to PR_SCOPE_CHANGED. Then Evaluate once {'N': 0.85, 'R': 0.62}; assign in source target order to UI. Then Evaluate once {'H': 0.56, 'L': 0.22, 'N': 0.0}; assign in source target order to CIA.
// Source: vvaharness/report/cvss.py:31-36
In source order: Evaluate once {'H': 1.5, 'L': 0.5}; assign in source target order to REQ. Then Evaluate once {'U': 0.91, 'P': 0.94, 'F': 0.97, 'H': 1.0}; assign in source target order to EXPLOIT_MATURITY. Then Evaluate once {'O': 0.95, 'T': 0.96, 'W': 0.97, 'U': 1.0}; assign in source target order to REMEDIATION_LEVEL. Then Evaluate once {'U': 0.92, 'R': 0.96, 'C': 1.0}; assign in source target order to REPORT_CONFIDENCE. Then Evaluate once 1.0; assign in source target order to NEUTRAL_WEIGHT.
// Source: vvaharness/report/cvss.py:37-42
In source order: Evaluate once -1.0; assign in source target order to NO_SCORE. Then Evaluate once 10.0; assign in source target order to MAX_SCORE. Then Evaluate once 0.915; assign in source target order to MISS_CAP. Then Evaluate once ((4.0, 'Low'), (7.0, 'Medium'), (9.0, 'High')); assign in source target order to SEVERITY_BANDS. Then Evaluate once 8.22; assign in source target order to EXPLOITABILITY_COEFF.
// Source: vvaharness/report/cvss.py:43-47
In source order: Evaluate once 6.42; assign in source target order to IMPACT_SCOPE_UNCHANGED_COEFF. Then Evaluate once 7.52; assign in source target order to IMPACT_SCOPE_CHANGED_COEFF. Then Evaluate once 0.029; assign in source target order to IMPACT_OFFSET. Then Evaluate once 3.25; assign in source target order to IMPACT_PENALTY_COEFF. Then Evaluate once 0.02; assign in source target order to IMPACT_PENALTY_OFFSET.
// Source: vvaharness/report/cvss.py:48-52
In source order: Evaluate once 15; assign in source target order to BASE_IMPACT_EXPONENT. Then Evaluate once 13; assign in source target order to MODIFIED_IMPACT_EXPONENT. Then Evaluate once 0.9731; assign in source target order to MODIFIED_IMPACT_MISS_CORRECTION. Then Evaluate once 1.08; assign in source target order to SCOPE_CHANGED_COEFF. Then Evaluate once 100000; assign in source target order to ROUNDUP_SCALE.
// Source: vvaharness/report/cvss.py:53-54
In source order: Evaluate once 10000; assign in source target order to ROUNDUP_STEP. Then Evaluate once 10.0; assign in source target order to ROUNDUP_STEPS_PER_UNIT.
// Source: vvaharness/report/cvss.py:57-62
// Source signature: roundup1(x: float) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn roundup1(x) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cvss.py:58-59
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then Evaluate once round(x * ROUNDUP_SCALE); assign in source target order to n.
  // Source: vvaharness/report/cvss.py:60-61
  if (the source predicate n % ROUNDUP_STEP == 0 is truthy) {
    // Source: vvaharness/report/cvss.py:61-61
    End this invocation with n / ROUNDUP_SCALE.
  }
  // Source: vvaharness/report/cvss.py:62-62
  End this invocation with (n // ROUNDUP_STEP + 1) / ROUNDUP_STEPS_PER_UNIT.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cvss.py:65-70
// Source signature: base_impact(iss: float, scope_changed: bool) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn base_impact(iss, scope_changed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cvss.py:66-66
  In source order: Retain source documentation literal source_literal_66_4; it is not a model call.
  // Source: vvaharness/report/cvss.py:67-68
  if (the source predicate not scope_changed is truthy) {
    // Source: vvaharness/report/cvss.py:68-68
    End this invocation with IMPACT_SCOPE_UNCHANGED_COEFF * iss.
  }
  // Source: vvaharness/report/cvss.py:69-70
  End this invocation with IMPACT_SCOPE_CHANGED_COEFF * (iss - IMPACT_OFFSET) - IMPACT_PENALTY_COEFF * (iss - IMPACT_PENALTY_OFFSET) ** BASE_IMPACT_EXPONENT.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cvss.py:73-80
// Source signature: modified_impact(miss: float, scope_changed: bool) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn modified_impact(miss, scope_changed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cvss.py:74-74
  In source order: Retain source documentation literal source_literal_74_4; it is not a model call.
  // Source: vvaharness/report/cvss.py:75-76
  if (the source predicate not scope_changed is truthy) {
    // Source: vvaharness/report/cvss.py:76-76
    End this invocation with IMPACT_SCOPE_UNCHANGED_COEFF * miss.
  }
  // Source: vvaharness/report/cvss.py:77-80
  End this invocation with IMPACT_SCOPE_CHANGED_COEFF * (miss - IMPACT_OFFSET) - IMPACT_PENALTY_COEFF * (miss * MODIFIED_IMPACT_MISS_CORRECTION - IMPACT_PENALTY_OFFSET) ** MODIFIED_IMPACT_EXPONENT.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cvss.py:83-88
// Source signature: combine(impact: float, exploitability: float, scope_changed: bool) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn combine(impact, exploitability, scope_changed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cvss.py:84-85
  In source order: Retain source documentation literal source_literal_84_4; it is not a model call. Then Evaluate once impact + exploitability; assign in source target order to raw.
  // Source: vvaharness/report/cvss.py:86-87
  if (the source predicate scope_changed is truthy) {
    // Source: vvaharness/report/cvss.py:87-87
    In source order: Apply source augmented assignment raw *= SCOPE_CHANGED_COEFF with source evaluation/in-place semantics.
  }
  // Source: vvaharness/report/cvss.py:88-88
  End this invocation with roundup1(min(raw, MAX_SCORE)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cvss.py:91-108
// Source signature: score(vector: str | None) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn score(vector) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cvss.py:92-92
  In source order: Retain source documentation literal source_literal_92_4; it is not a model call.
  // Source: vvaharness/report/cvss.py:93-94
  if (the source predicate not vector is truthy) {
    // Source: vvaharness/report/cvss.py:94-94
    End this invocation with None.
  }
  // Source: vvaharness/report/cvss.py:95-95
  In source order: Evaluate once _VECTOR_RE.search(vector); assign in source target order to m.
  // Source: vvaharness/report/cvss.py:96-97
  if (the source predicate not m is truthy) {
    // Source: vvaharness/report/cvss.py:97-97
    End this invocation with None.
  }
  // Source: vvaharness/report/cvss.py:98-102
  In source order: Evaluate once m.groupdict(); assign in source target order to g. Then Evaluate once g['S'] == 'C'; assign in source target order to scope_changed. Then Evaluate once 1 - (1 - CIA[g['C']]) * (1 - CIA[g['I']]) * (1 - CIA[g['A']]); assign in source target order to iss. Then Evaluate once base_impact(iss, scope_changed); assign in source target order to impact.
  // Source: vvaharness/report/cvss.py:103-104
  if (the source predicate impact <= 0 is truthy) {
    // Source: vvaharness/report/cvss.py:104-104
    End this invocation with 0.0.
  }
  // Source: vvaharness/report/cvss.py:106-107
  In source order: Evaluate once (PR_SCOPE_CHANGED if scope_changed else PR_SCOPE_UNCHANGED)[g['PR']]; assign in source target order to pr. Then Evaluate once EXPLOITABILITY_COEFF * AV[g['AV']] * AC[g['AC']] * pr * UI[g['UI']]; assign in source target order to exploitability.
  // Source: vvaharness/report/cvss.py:108-108
  End this invocation with combine(impact, exploitability, scope_changed).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cvss.py:111-114
// Source signature: score_or_sentinel(vector: str | None) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn score_or_sentinel(vector) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cvss.py:112-113
  In source order: Retain source documentation literal source_literal_112_4; it is not a model call. Then Evaluate once score(vector); assign in source target order to s.
  // Source: vvaharness/report/cvss.py:114-114
  End this invocation with s if s is not None else NO_SCORE.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/report/cvss.py:117-126
// Source signature: rating(s: float | None) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn rating(s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/report/cvss.py:118-118
  In source order: Retain source documentation literal source_literal_118_4; it is not a model call.
  // Source: vvaharness/report/cvss.py:119-120
  if (the source predicate s is None is truthy) {
    // Source: vvaharness/report/cvss.py:120-120
    End this invocation with 'Unknown'.
  }
  // Source: vvaharness/report/cvss.py:121-122
  if (the source predicate s == 0.0 is truthy) {
    // Source: vvaharness/report/cvss.py:122-122
    End this invocation with 'None'.
  }
  // Source: vvaharness/report/cvss.py:123-125
  for each (upper, label) in SEVERITY_BANDS {
    // Source: vvaharness/report/cvss.py:124-125
    if (the source predicate s < upper is truthy) {
      // Source: vvaharness/report/cvss.py:125-125
      End this invocation with label.
    }
  }
  // Source: vvaharness/report/cvss.py:126-126
  End this invocation with 'Critical'.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
