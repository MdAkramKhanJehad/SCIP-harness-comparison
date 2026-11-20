# vvaharness/util/tokens.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/tokens.py.evidence.json`. SHA-256: `bd187172a7225597ab99561e8096d73944744a678413f526652115269bc114d0`.

```sudo
// Source: vvaharness/util/tokens.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects. Then Resolve source import from collections import defaultdict; preserve alias and import-time effects.
// Source: vvaharness/util/tokens.py:22-25
In source order: Resolve source import from contextlib import contextmanager; preserve alias and import-time effects. Then Resolve source import from typing import NamedTuple, TypedDict; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.warn_once import warn_once; preserve alias and import-time effects.
// Source: vvaharness/util/tokens.py:28-37
interface TokenUsage {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/tokens.py:29-35
  In source order: Retain source documentation literal source_literal_29_4; it is not a model call. Then For input_tokens, declare without assigning a value; source annotation int. Then For output_tokens, declare without assigning a value; source annotation int | None. Then For cache_creation_input_tokens, declare without assigning a value; source annotation int. Then For cache_read_input_tokens, declare without assigning a value; source annotation int.
  // Source: vvaharness/util/tokens.py:37-37
  In source order: For reasoning_tokens, declare without assigning a value; source annotation int.
}
// Source: vvaharness/util/tokens.py:40-40
In source order: Evaluate once 'unscoped'; assign in source target order to DEFAULT_PHASE.
// Source: vvaharness/util/tokens.py:43-49
interface Spend {
  Describe the source Python type, preserving its base/metaclass expression order: NamedTuple.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/tokens.py:44-49
  In source order: Retain source documentation literal source_literal_44_4; it is not a model call. Then For usd, assign 0.0; source annotation float. Then For turns, assign 0; source annotation int. Then For usd_reports, assign 0; source annotation int. Then For turn_reports, assign 0; source annotation int.
}
// Source: vvaharness/util/tokens.py:52-58
// Source signature: reported_between(before: Spend, after: Spend) -> tuple[float | None, int | None]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn reported_between(before, after) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/tokens.py:53-57
  In source order: Retain source documentation literal source_literal_53_4; it is not a model call. Then Evaluate once after.usd - before.usd if after.usd_reports > before.usd_reports else None; assign in source target order to usd. Then Evaluate once after.turns - before.turns if after.turn_reports > before.turn_reports else None; assign in source target order to turns.
  // Source: vvaharness/util/tokens.py:58-58
  End this invocation with (usd, turns).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/tokens.py:63-66
In source order: Evaluate once 4.4; assign in source target order to _CPT_PROSE. Then Evaluate once 2.45; assign in source target order to _CPT_DENSE. Then Evaluate once 0.08; assign in source target order to _DENSE_FRAC_LO. Then Evaluate once 0.34; assign in source target order to _DENSE_FRAC_HI.
// Source: vvaharness/util/tokens.py:69-86
// Source signature: estimate_tokens(text: str) -> int
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn estimate_tokens(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/tokens.py:70-71
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once len(text); assign in source target order to n.
  // Source: vvaharness/util/tokens.py:72-73
  if (the source predicate n <= 0 is truthy) {
    // Source: vvaharness/util/tokens.py:73-73
    End this invocation with 0.
  }
  // Source: vvaharness/util/tokens.py:74-74
  In source order: Evaluate once 0; assign in source target order to dense.
  // Source: vvaharness/util/tokens.py:75-77
  for each ch in text {
    // Source: vvaharness/util/tokens.py:76-77
    if (the source predicate not ch.isspace() and (not ch.isalpha()) is truthy) {
      // Source: vvaharness/util/tokens.py:77-77
      In source order: Apply source augmented assignment dense += 1 with source evaluation/in-place semantics.
    }
  }
  // Source: vvaharness/util/tokens.py:78-78
  In source order: Evaluate once dense / n; assign in source target order to frac.
  // Source: vvaharness/util/tokens.py:79-85
  if (the source predicate frac <= _DENSE_FRAC_LO is truthy) {
    // Source: vvaharness/util/tokens.py:80-80
    In source order: Evaluate once _CPT_PROSE; assign in source target order to cpt.
  }
  else {
    // Source: vvaharness/util/tokens.py:81-85
    if (the source predicate frac >= _DENSE_FRAC_HI is truthy) {
      // Source: vvaharness/util/tokens.py:82-82
      In source order: Evaluate once _CPT_DENSE; assign in source target order to cpt.
    }
    else {
      // Source: vvaharness/util/tokens.py:84-85
      In source order: Evaluate once (frac - _DENSE_FRAC_LO) / (_DENSE_FRAC_HI - _DENSE_FRAC_LO); assign in source target order to span. Then Evaluate once _CPT_PROSE + span * (_CPT_DENSE - _CPT_PROSE); assign in source target order to cpt.
    }
  }
  // Source: vvaharness/util/tokens.py:86-86
  End this invocation with int(n / cpt).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/tokens.py:89-93
// Source signature: _bucket() -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _bucket() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/tokens.py:91-93
  End this invocation with {'prompt': 0, 'completion': 0, 'cache_read': 0, 'cache_write': 0, 'calls': 0, 'cache_unparsed': 0, 'usd': None, 'turns': None, 'reasoning': 0}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/tokens.py:98-99
In source order: Evaluate once re.compile('^[A-Za-z0-9_.\\-]{1,64}$'); assign in source target order to _UNPARSED_CACHE_KEY_RX. Then Evaluate once 8; assign in source target order to _UNPARSED_CACHE_KEY_CAP.
// Source: vvaharness/util/tokens.py:102-112
// Source signature: unparsed_cache_keys(usage, parsed) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn unparsed_cache_keys(usage, parsed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/tokens.py:103-103
  In source order: Retain source documentation literal source_literal_103_4; it is not a model call.
  // Source: vvaharness/util/tokens.py:105-106
  if (the source predicate not isinstance(usage, dict) is truthy) {
    // Source: vvaharness/util/tokens.py:106-106
    End this invocation with ().
  }
  // Source: vvaharness/util/tokens.py:107-111
  In source order: Evaluate once {k for k, v in usage.items() if isinstance(k, str) and k not in parsed and (v is not None) and ('cache' in k.lower()) and _UNPARSED_CACHE_KEY_RX.match(k)}; assign in source target order to hits.
  // Source: vvaharness/util/tokens.py:112-112
  End this invocation with tuple(sorted(hits)[:_UNPARSED_CACHE_KEY_CAP]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/tokens.py:115-237
interface _TokenCounter {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/tokens.py:116-133
  // Source signature: __init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:117-121
    In source order: Evaluate once threading.Lock(); assign in source target order to self._lock. Then Evaluate once DEFAULT_PHASE; assign in source target order to self._phase. Then Evaluate once 0; assign in source target order to self.prompt. Then Evaluate once 0; assign in source target order to self.completion. Then Evaluate once 0; assign in source target order to self.calls.
    // Source: vvaharness/util/tokens.py:122-127
    In source order: Evaluate once 0; assign in source target order to self.calls_with_usage. Then Evaluate once 0; assign in source target order to self.completion_absent. Then Evaluate once 0.0; assign in source target order to self.usd. Then Evaluate once 0; assign in source target order to self.turns. Then Evaluate once 0; assign in source target order to self.usd_reports.
    // Source: vvaharness/util/tokens.py:128-133
    In source order: Evaluate once 0; assign in source target order to self.turn_reports. Then For self.by_phase, assign defaultdict(_bucket); source annotation dict[str, dict]. Then For self._cache_unparsed_seen, assign set(); source annotation set[tuple]. Then For self._completion_absent_noted, assign set(); source annotation set[str].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/tokens.py:136-141
  // Source: vvaharness/util/tokens.py:135-135
  Before creating this callable, evaluate and retain decorators top-to-bottom: contextmanager.
  // Source: vvaharness/util/tokens.py:136-141
  // Source signature: phase(self, name: str)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn phase(self, name) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:137-137
    In source order: Evaluate once (self._phase, name); assign in source target order to (prev, self._phase).
    // Source: vvaharness/util/tokens.py:138-141
    Perform the following protected operations {
      // Source: vvaharness/util/tokens.py:139-139
      In source order: Yield None; suspend this generator until resumed.
    }
    On every exit from this protected/handler/normal-completion region {
      // Source: vvaharness/util/tokens.py:141-141
      In source order: Evaluate once prev; assign in source target order to self._phase.
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/util/tokens.py:143-145
  // Source signature: current_phase(self) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn current_phase(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:144-145
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/tokens.py:145-145
      End this invocation with self._phase.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/tokens.py:147-194
  // Source signature: add(self, usage: TokenUsage | None, *, usd: float | None=None, turns: int | None=None) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn add(self, usage, usd, turns) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:149-149
    In source order: Retain source documentation literal source_literal_149_8; it is not a model call.
    // Source: vvaharness/util/tokens.py:150-194
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/tokens.py:151-151
      In source order: Evaluate once 1; assign in source target order to n_requests.
      // Source: vvaharness/util/tokens.py:152-156
      if (the source predicate isinstance(usage, dict) is truthy) {
        // Source: vvaharness/util/tokens.py:153-153
        In source order: Evaluate once usage.get('calls'); assign in source target order to raw_calls.
        // Source: vvaharness/util/tokens.py:154-156
        if (the source predicate isinstance(raw_calls, int) and (not isinstance(raw_calls, bool)) and (raw_calls > 0) is truthy) {
          // Source: vvaharness/util/tokens.py:156-156
          In source order: Evaluate once raw_calls; assign in source target order to n_requests.
        }
      }
      // Source: vvaharness/util/tokens.py:157-159
      In source order: Apply source augmented assignment self.calls += n_requests with source evaluation/in-place semantics. Then Evaluate once self.by_phase[self._phase]; assign in source target order to b. Then Apply source augmented assignment b['calls'] += n_requests with source evaluation/in-place semantics.
      // Source: vvaharness/util/tokens.py:160-163
      if (the source predicate usd is not None is truthy) {
        // Source: vvaharness/util/tokens.py:161-163
        In source order: Apply source augmented assignment self.usd_reports += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment self.usd += usd with source evaluation/in-place semantics. Then Evaluate once (b['usd'] or 0.0) + usd; assign in source target order to b['usd'].
      }
      // Source: vvaharness/util/tokens.py:164-167
      if (the source predicate turns is not None is truthy) {
        // Source: vvaharness/util/tokens.py:165-167
        In source order: Apply source augmented assignment self.turn_reports += 1 with source evaluation/in-place semantics. Then Apply source augmented assignment self.turns += turns with source evaluation/in-place semantics. Then Evaluate once (b['turns'] or 0) + turns; assign in source target order to b['turns'].
      }
      // Source: vvaharness/util/tokens.py:168-169
      if (the source predicate not isinstance(usage, dict) is truthy) {
        // Source: vvaharness/util/tokens.py:169-169
        End this invocation with None.
      }
      // Source: vvaharness/util/tokens.py:170-174
      In source order: Apply source augmented assignment self.calls_with_usage += n_requests with source evaluation/in-place semantics. Then Evaluate once int(usage.get('input_tokens', 0) or 0); assign in source target order to fresh. Then Evaluate once int(usage.get('cache_creation_input_tokens', 0) or 0); assign in source target order to cw. Then Evaluate once int(usage.get('cache_read_input_tokens', 0) or 0); assign in source target order to cr. Then Evaluate once usage.get('output_tokens', 0); assign in source target order to out_raw.
      // Source: vvaharness/util/tokens.py:175-184
      if (the source predicate out_raw is None is truthy) {
        // Source: vvaharness/util/tokens.py:177-184
        In source order: Apply source augmented assignment self.completion_absent += 1 with source evaluation/in-place semantics. Then Evaluate warn_once(self._completion_absent_noted, 'null-completion-count', source_literal_181_20); retain side effects and discard the expression result.
      }
      // Source: vvaharness/util/tokens.py:185-190
      In source order: Evaluate once int(out_raw or 0); assign in source target order to out. Then Apply source augmented assignment self.prompt += fresh + cw with source evaluation/in-place semantics. Then Apply source augmented assignment self.completion += out with source evaluation/in-place semantics. Then Apply source augmented assignment b['prompt'] += fresh + cw with source evaluation/in-place semantics. Then Apply source augmented assignment b['completion'] += out with source evaluation/in-place semantics.
      // Source: vvaharness/util/tokens.py:191-194
      In source order: Apply source augmented assignment b['cache_read'] += cr with source evaluation/in-place semantics. Then Apply source augmented assignment b['cache_write'] += cw with source evaluation/in-place semantics. Then Apply source augmented assignment b['reasoning'] += int(usage.get('reasoning_tokens', 0) or 0) with source evaluation/in-place semantics.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/tokens.py:196-200
  // Source signature: spend(self) -> Spend
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn spend(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:197-197
    In source order: Retain source documentation literal source_literal_197_8; it is not a model call.
    // Source: vvaharness/util/tokens.py:198-200
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/tokens.py:199-200
      End this invocation with Spend(usd=self.usd, turns=self.turns, usd_reports=self.usd_reports, turn_reports=self.turn_reports).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/tokens.py:202-213
  // Source signature: note_cache_unparsed(self, keys: tuple[str, ...], *, via: str='') -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn note_cache_unparsed(self, keys, via) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:204-204
    In source order: Retain source documentation literal source_literal_204_8; it is not a model call.
    // Source: vvaharness/util/tokens.py:205-206
    if (the source predicate not keys is truthy) {
      // Source: vvaharness/util/tokens.py:206-206
      End this invocation with False.
    }
    // Source: vvaharness/util/tokens.py:207-213
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/tokens.py:208-209
      In source order: Apply source augmented assignment self.by_phase[self._phase]['cache_unparsed'] += 1 with source evaluation/in-place semantics. Then Evaluate once (via, keys); assign in source target order to marker.
      // Source: vvaharness/util/tokens.py:210-211
      if (the source predicate marker in self._cache_unparsed_seen is truthy) {
        // Source: vvaharness/util/tokens.py:211-211
        End this invocation with False.
      }
      // Source: vvaharness/util/tokens.py:212-212
      In source order: Evaluate self._cache_unparsed_seen.add(marker); retain side effects and discard the expression result.
      // Source: vvaharness/util/tokens.py:213-213
      End this invocation with True.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/tokens.py:215-223
  // Source signature: reset(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn reset(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:216-223
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/tokens.py:217-221
      In source order: Evaluate once 0; assign in source target order to self.prompt, self.completion, self.calls, self.calls_with_usage. Then Evaluate once 0; assign in source target order to self.completion_absent. Then Evaluate once 0.0; assign in source target order to self.usd. Then Evaluate once 0; assign in source target order to self.turns, self.usd_reports, self.turn_reports. Then Evaluate once defaultdict(_bucket); assign in source target order to self.by_phase.
      // Source: vvaharness/util/tokens.py:222-223
      In source order: Evaluate once set(); assign in source target order to self._cache_unparsed_seen. Then Evaluate once set(); assign in source target order to self._completion_absent_noted.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/util/tokens.py:225-237
  // Source signature: snapshot(self) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn snapshot(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/util/tokens.py:226-237
    Enter source context managers left-to-right: self._lock {
      // Source: vvaharness/util/tokens.py:227-237
      End this invocation with {'prompt': self.prompt, 'completion': self.completion, 'total': self.prompt + self.completion, 'calls': self.calls, 'calls_with_usage': self.calls_with_usage, 'completion_absent': self.completion_absent, 'usd': self.usd if self.usd_reports else None, 'turns': self.turns if self.turn_reports else None, 'by_phase': {k: dict(v) for k, v in self.by_phase.items()}}.
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/util/tokens.py:240-240
In source order: Evaluate once _TokenCounter(); assign in source target order to TOKENS.
```

## Local import links

- `from vvaharness.util.warn_once import warn_once` at source line 25: `source_detail/vvaharness/util/warn_once.py.sudo.md`.
