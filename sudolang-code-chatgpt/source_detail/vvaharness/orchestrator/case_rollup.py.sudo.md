# vvaharness/orchestrator/case_rollup.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/orchestrator/case_rollup.py.evidence.json`. SHA-256: `95c3c38755c2287b21d3b8850f0ed1f8a4d04716e4168c68e250a8fc0fbcebc5`.

```sudo
// Source: vvaharness/orchestrator/case_rollup.py:15-23
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from collections.abc import Iterable; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/case_rollup.py:24-29
In source order: Resolve source import from typing import Final; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.case import FindingCase; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.derive import state_of, verdict_state; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.verdict import Verdict; preserve alias and import-time effects. Then Resolve source import from vvaharness.models.vocab import CaseState; preserve alias and import-time effects.
// Source: vvaharness/orchestrator/case_rollup.py:30-50
In source order: Resolve source import from vvaharness.orchestrator.artifacts import CASE_DIR_NAME, CASE_FILE_NAME, UnsafeArtifactDir, artifact_dir; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['EXIT_NOT_REMEDIATED', 'rc_for_verdicts', 'record', 'reset', 'rollup_for', 'totals']; assign in source target order to __all__. Then For EXIT_NOT_REMEDIATED, assign 3; source annotation Final.
// Source: vvaharness/orchestrator/case_rollup.py:53-56
In source order: For _MAX_CASE_BYTES, assign 4 * 1024 * 1024; source annotation Final. Then For _TOTALS, assign {}; source annotation Final[dict].
// Source: vvaharness/orchestrator/case_rollup.py:59-65
// Source signature: rc_for_verdicts(verdicts: Iterable[Verdict | None]) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn rc_for_verdicts(verdicts) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_rollup.py:60-62
  In source order: Retain source documentation literal source_literal_60_4; it is not a model call. Then Evaluate once [verdict_state(v) for v in verdicts if v is not None]; assign in source target order to states.
  // Source: vvaharness/orchestrator/case_rollup.py:63-64
  if (the source predicate CaseState.VALIDATED in states or CaseState.FAILED not in states is truthy) {
    // Source: vvaharness/orchestrator/case_rollup.py:64-64
    End this invocation with 0.
  }
  // Source: vvaharness/orchestrator/case_rollup.py:65-65
  End this invocation with EXIT_NOT_REMEDIATED.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_rollup.py:68-73
// Source signature: _inside(path: Path, root: Path) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _inside(path, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_rollup.py:69-69
  In source order: Retain source documentation literal source_literal_69_4; it is not a model call.
  // Source: vvaharness/orchestrator/case_rollup.py:70-73
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/case_rollup.py:71-71
    End this invocation with path.resolve().is_relative_to(root.resolve()).
  }
  // Source: vvaharness/orchestrator/case_rollup.py:72-73
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/orchestrator/case_rollup.py:73-73
    End this invocation with False.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_rollup.py:76-82
// Source signature: _shaped(cases: int, states: dict[str, int], decisions: dict[str, int]) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shaped(cases, states, decisions) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_rollup.py:77-77
  In source order: Retain source documentation literal source_literal_77_4; it is not a model call.
  // Source: vvaharness/orchestrator/case_rollup.py:78-82
  End this invocation with {'cases': cases, 'states': dict(sorted(states.items())), 'decisions': dict(sorted(decisions.items()))}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_rollup.py:85-127
// Source signature: rollup_for(repo: Path | str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn rollup_for(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_rollup.py:86-90
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then Evaluate once 0; assign in source target order to cases. Then For states, assign {}; source annotation dict[str, int]. Then For decisions, assign {}; source annotation dict[str, int].
  // Source: vvaharness/orchestrator/case_rollup.py:91-96
  Perform the following protected operations {
    // Source: vvaharness/orchestrator/case_rollup.py:92-92
    In source order: Evaluate once artifact_dir(repo, CASE_DIR_NAME); assign in source target order to case_root.
  }
  // Source: vvaharness/orchestrator/case_rollup.py:93-96
  On the first matching source exception UnsafeArtifactDir as exc, in handler order {
    // Source: vvaharness/orchestrator/case_rollup.py:95-95
    In source order: Evaluate log.warning(Event.CASE_ROOT_UNSAFE, repo=str(repo), detail=str(exc)); retain side effects and discard the expression result.
    // Source: vvaharness/orchestrator/case_rollup.py:96-96
    End this invocation with {}.
  }
  // Source: vvaharness/orchestrator/case_rollup.py:97-98
  if (the source predicate not case_root.is_dir() is truthy) {
    // Source: vvaharness/orchestrator/case_rollup.py:98-98
    End this invocation with {}.
  }
  // Source: vvaharness/orchestrator/case_rollup.py:100-124
  for each path in case_root.glob(source_template_100_31) {
    // Source: vvaharness/orchestrator/case_rollup.py:101-120
    Perform the following protected operations {
      // Source: vvaharness/orchestrator/case_rollup.py:103-104
      if (the source predicate not path.is_file() is truthy) {
        // Source: vvaharness/orchestrator/case_rollup.py:104-104
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/case_rollup.py:105-107
      if (the source predicate not _inside(path, case_root) is truthy) {
        // Source: vvaharness/orchestrator/case_rollup.py:106-106
        In source order: Evaluate log.warning(Event.CASE_PATH_OUTSIDE_ROOT, path=path, case_root=case_root); retain side effects and discard the expression result.
        // Source: vvaharness/orchestrator/case_rollup.py:107-107
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/orchestrator/case_rollup.py:108-108
      In source order: Evaluate once path.stat().st_size; assign in source target order to size.
      // Source: vvaharness/orchestrator/case_rollup.py:109-111
      if (the source predicate size > _MAX_CASE_BYTES is truthy) {
        // Source: vvaharness/orchestrator/case_rollup.py:110-110
        In source order: Evaluate once source_template_110_22; assign in source target order to msg.
        // Source: vvaharness/orchestrator/case_rollup.py:111-111
        Raise ValueError(msg).
      }
      // Source: vvaharness/orchestrator/case_rollup.py:112-116
      In source order: Evaluate once FindingCase.read(path); assign in source target order to case. Then Evaluate once state_of(case.attempts).value; assign in source target order to state. Then Evaluate once case.attempts[-1].verdict if case.attempts else None; assign in source target order to verdict. Then Evaluate once verdict.decision.value if verdict is not None else None; assign in source target order to decision.
    }
    // Source: vvaharness/orchestrator/case_rollup.py:117-120
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/orchestrator/case_rollup.py:119-119
      In source order: Evaluate log.warning(Event.CASE_RECORD_UNREADABLE, path=path, detail=str(exc)); retain side effects and discard the expression result.
      // Source: vvaharness/orchestrator/case_rollup.py:120-120
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/orchestrator/case_rollup.py:121-122
    In source order: Apply source augmented assignment cases += 1 with source evaluation/in-place semantics. Then Evaluate once states.get(state, 0) + 1; assign in source target order to states[state].
    // Source: vvaharness/orchestrator/case_rollup.py:123-124
    if (the source predicate decision is not None is truthy) {
      // Source: vvaharness/orchestrator/case_rollup.py:124-124
      In source order: Evaluate once decisions.get(decision, 0) + 1; assign in source target order to decisions[decision].
    }
  }
  // Source: vvaharness/orchestrator/case_rollup.py:125-126
  if (the source predicate not cases is truthy) {
    // Source: vvaharness/orchestrator/case_rollup.py:126-126
    End this invocation with {}.
  }
  // Source: vvaharness/orchestrator/case_rollup.py:127-127
  End this invocation with _shaped(cases, states, decisions).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_rollup.py:130-139
// Source signature: record(repo: Path | str) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn record(repo) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_rollup.py:131-132
  In source order: Retain source documentation literal source_literal_131_4; it is not a model call. Then Evaluate once rollup_for(repo); assign in source target order to rollup.
  // Source: vvaharness/orchestrator/case_rollup.py:133-138
  if (the source predicate rollup is truthy) {
    // Source: vvaharness/orchestrator/case_rollup.py:134-134
    In source order: Evaluate once _TOTALS.get('cases', 0) + rollup['cases']; assign in source target order to _TOTALS['cases'].
    // Source: vvaharness/orchestrator/case_rollup.py:135-138
    for each key in ('states', 'decisions') {
      // Source: vvaharness/orchestrator/case_rollup.py:136-136
      In source order: Evaluate once _TOTALS.setdefault(key, {}); assign in source target order to bucket.
      // Source: vvaharness/orchestrator/case_rollup.py:137-138
      for each (name, n) in rollup[key].items() {
        // Source: vvaharness/orchestrator/case_rollup.py:138-138
        In source order: Evaluate once bucket.get(name, 0) + n; assign in source target order to bucket[name].
      }
    }
  }
  // Source: vvaharness/orchestrator/case_rollup.py:139-139
  End this invocation with rollup.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_rollup.py:142-146
// Source signature: totals() -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn totals() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_rollup.py:143-143
  In source order: Retain source documentation literal source_literal_143_4; it is not a model call.
  // Source: vvaharness/orchestrator/case_rollup.py:144-145
  if (the source predicate not _TOTALS is truthy) {
    // Source: vvaharness/orchestrator/case_rollup.py:145-145
    End this invocation with {}.
  }
  // Source: vvaharness/orchestrator/case_rollup.py:146-146
  End this invocation with _shaped(_TOTALS['cases'], _TOTALS['states'], _TOTALS['decisions']).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/orchestrator/case_rollup.py:149-151
// Source signature: reset() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reset() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/orchestrator/case_rollup.py:150-151
  In source order: Retain source documentation literal source_literal_150_4; it is not a model call. Then Evaluate _TOTALS.clear(); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 20: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 20: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.models.case import FindingCase` at source line 26: `source_detail/vvaharness/models/case.py.sudo.md`.
- `from vvaharness.models.derive import state_of, verdict_state` at source line 27: `source_detail/vvaharness/models/derive.py.sudo.md`.
- `from vvaharness.models.verdict import Verdict` at source line 28: `source_detail/vvaharness/models/verdict.py.sudo.md`.
- `from vvaharness.models.vocab import CaseState` at source line 29: `source_detail/vvaharness/models/vocab.py.sudo.md`.
- `from vvaharness.orchestrator.artifacts import CASE_DIR_NAME, CASE_FILE_NAME, UnsafeArtifactDir, artifact_dir` at source line 30: `source_detail/vvaharness/orchestrator/artifacts.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 36: `source_detail/vvaharness/util/events.py.sudo.md`.
