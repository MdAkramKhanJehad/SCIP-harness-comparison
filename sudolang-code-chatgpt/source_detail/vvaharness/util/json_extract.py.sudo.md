# vvaharness/util/json_extract.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/json_extract.py.evidence.json`. SHA-256: `2a8327658688c8b522515b46a6e4cd0d82c485f9a09c0df25a196ca84086e55f`.

```sudo
// Source: vvaharness/util/json_extract.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects.
// Source: vvaharness/util/json_extract.py:21-30
In source order: Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once re.compile('```(?:json)?\\s*(.*?)\\s*```', re.DOTALL); assign in source target order to _FENCE. Then Evaluate once re.compile('^```\\w*\\s*'); assign in source target order to _FENCE_OPEN. Then Evaluate once 5000000; assign in source target order to _MAX_JSON_INPUT.
// Source: vvaharness/util/json_extract.py:32-32
In source order: Evaluate once set('"\\/nrtu'); assign in source target order to _VALID_ESCAPE.
// Source: vvaharness/util/json_extract.py:35-53
// Source signature: _repair_invalid_escapes(s: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _repair_invalid_escapes(s) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/json_extract.py:36-38
  In source order: Retain source documentation literal source_literal_36_4; it is not a model call. Then For out, assign []; source annotation list[str]. Then Evaluate once (0, len(s)); assign in source target order to (i, n).
  // Source: vvaharness/util/json_extract.py:39-52
  while (the source predicate i < n is truthy) {
    // Source: vvaharness/util/json_extract.py:40-40
    In source order: Evaluate once s[i]; assign in source target order to ch.
    // Source: vvaharness/util/json_extract.py:41-50
    if (the source predicate ch == '\\' is truthy) {
      // Source: vvaharness/util/json_extract.py:42-42
      In source order: Evaluate once s[i + 1] if i + 1 < n else ''; assign in source target order to nxt.
      // Source: vvaharness/util/json_extract.py:43-47
      if (the source predicate nxt in _VALID_ESCAPE is truthy) {
        // Source: vvaharness/util/json_extract.py:44-46
        In source order: Evaluate out.append(ch); retain side effects and discard the expression result. Then Evaluate out.append(nxt); retain side effects and discard the expression result. Then Apply source augmented assignment i += 2 with source evaluation/in-place semantics.
        // Source: vvaharness/util/json_extract.py:47-47
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/util/json_extract.py:48-49
      In source order: Evaluate out.append('\\\\'); retain side effects and discard the expression result. Then Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
      // Source: vvaharness/util/json_extract.py:50-50
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/util/json_extract.py:51-52
    In source order: Evaluate out.append(ch); retain side effects and discard the expression result. Then Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
  }
  // Source: vvaharness/util/json_extract.py:53-53
  End this invocation with ''.join(out).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/json_extract.py:56-80
// Source signature: _balanced_span(s: str, start: int) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _balanced_span(s, start) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/json_extract.py:57-61
  In source order: Evaluate once s[start]; assign in source target order to open_ch. Then Evaluate once '}' if open_ch == '{' else ']'; assign in source target order to close_ch. Then Evaluate once 0; assign in source target order to depth. Then Evaluate once False; assign in source target order to in_str. Then Evaluate once False; assign in source target order to esc.
  // Source: vvaharness/util/json_extract.py:62-79
  for each i in range(start, len(s)) {
    // Source: vvaharness/util/json_extract.py:63-63
    In source order: Evaluate once s[i]; assign in source target order to ch.
    // Source: vvaharness/util/json_extract.py:64-79
    if (the source predicate in_str is truthy) {
      // Source: vvaharness/util/json_extract.py:65-70
      if (the source predicate esc is truthy) {
        // Source: vvaharness/util/json_extract.py:66-66
        In source order: Evaluate once False; assign in source target order to esc.
      }
      else {
        // Source: vvaharness/util/json_extract.py:67-70
        if (the source predicate ch == '\\' is truthy) {
          // Source: vvaharness/util/json_extract.py:68-68
          In source order: Evaluate once True; assign in source target order to esc.
        }
        else {
          // Source: vvaharness/util/json_extract.py:69-70
          if (the source predicate ch == '"' is truthy) {
            // Source: vvaharness/util/json_extract.py:70-70
            In source order: Evaluate once False; assign in source target order to in_str.
          }
        }
      }
    }
    else {
      // Source: vvaharness/util/json_extract.py:72-79
      if (the source predicate ch == '"' is truthy) {
        // Source: vvaharness/util/json_extract.py:73-73
        In source order: Evaluate once True; assign in source target order to in_str.
      }
      else {
        // Source: vvaharness/util/json_extract.py:74-79
        if (the source predicate ch == open_ch is truthy) {
          // Source: vvaharness/util/json_extract.py:75-75
          In source order: Apply source augmented assignment depth += 1 with source evaluation/in-place semantics.
        }
        else {
          // Source: vvaharness/util/json_extract.py:76-79
          if (the source predicate ch == close_ch is truthy) {
            // Source: vvaharness/util/json_extract.py:77-77
            In source order: Apply source augmented assignment depth -= 1 with source evaluation/in-place semantics.
            // Source: vvaharness/util/json_extract.py:78-79
            if (the source predicate depth == 0 is truthy) {
              // Source: vvaharness/util/json_extract.py:79-79
              End this invocation with s[start:i + 1].
            }
          }
        }
      }
    }
  }
  // Source: vvaharness/util/json_extract.py:80-80
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/json_extract.py:83-140
// Source signature: extract_json(text: str) -> dict | list
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_json(text) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/json_extract.py:84-86
  if (the source predicate len(text) > _MAX_JSON_INPUT is truthy) {
    // Source: vvaharness/util/json_extract.py:85-86
    In source order: Evaluate log.warning(Event.JSON_INPUT_TRUNCATED, size=len(text), cap=_MAX_JSON_INPUT); retain side effects and discard the expression result. Then Evaluate once text[:_MAX_JSON_INPUT]; assign in source target order to text.
  }
  // Source: vvaharness/util/json_extract.py:87-91
  In source order: Evaluate once text.strip(); assign in source target order to stripped. Then For candidates, assign []; source annotation list[str]. Then Evaluate once _FENCE.fullmatch(stripped); assign in source target order to whole.
  // Source: vvaharness/util/json_extract.py:92-93
  if (the source predicate whole is truthy) {
    // Source: vvaharness/util/json_extract.py:93-93
    In source order: Evaluate candidates.append(whole.group(1)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/json_extract.py:94-100
  In source order: Apply source augmented assignment candidates += _FENCE.findall(text) with source evaluation/in-place semantics. Then Evaluate candidates.append(text); retain side effects and discard the expression result. Then Evaluate once _FENCE_OPEN.sub('', stripped, count=1); assign in source target order to peek. Then Evaluate once peek[:1] == '{'; assign in source target order to want_dict. Then For held_list, assign None; source annotation list | None.
  // Source: vvaharness/util/json_extract.py:101-101
  In source order: For last_err, assign None; source annotation Exception | None.
  // Source: vvaharness/util/json_extract.py:103-134
  for each cand in candidates {
    // Source: vvaharness/util/json_extract.py:104-104
    In source order: Evaluate once 0; assign in source target order to i.
    // Source: vvaharness/util/json_extract.py:105-134
    while (the source predicate i < len(cand) is truthy) {
      // Source: vvaharness/util/json_extract.py:106-108
      if (the source predicate cand[i] not in '{[' is truthy) {
        // Source: vvaharness/util/json_extract.py:107-107
        In source order: Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/util/json_extract.py:108-108
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/util/json_extract.py:109-109
      In source order: Evaluate once _balanced_span(cand, i); assign in source target order to span.
      // Source: vvaharness/util/json_extract.py:110-113
      if (the source predicate span is None is truthy) {
        // Source: vvaharness/util/json_extract.py:112-112
        In source order: Apply source augmented assignment i += 1 with source evaluation/in-place semantics.
        // Source: vvaharness/util/json_extract.py:113-113
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/util/json_extract.py:114-114
      In source order: Evaluate once None; assign in source target order to val.
      // Source: vvaharness/util/json_extract.py:115-125
      Perform the following protected operations {
        // Source: vvaharness/util/json_extract.py:116-116
        In source order: Evaluate once json.loads(span); assign in source target order to val.
      }
      // Source: vvaharness/util/json_extract.py:117-125
      On the first matching source exception json.JSONDecodeError as e, in handler order {
        // Source: vvaharness/util/json_extract.py:118-120
        In source order: Evaluate once e; assign in source target order to last_err. Then Evaluate once _repair_invalid_escapes(span); assign in source target order to repaired.
        // Source: vvaharness/util/json_extract.py:121-125
        if (the source predicate repaired != span is truthy) {
          // Source: vvaharness/util/json_extract.py:122-125
          Perform the following protected operations {
            // Source: vvaharness/util/json_extract.py:123-123
            In source order: Evaluate once json.loads(repaired); assign in source target order to val.
          }
          // Source: vvaharness/util/json_extract.py:124-125
          On the first matching source exception json.JSONDecodeError, in handler order {
            // Source: vvaharness/util/json_extract.py:125-125
            In source order: Perform no operation at this source statement.
          }
        }
      }
      // Source: vvaharness/util/json_extract.py:126-128
      if (the source predicate val is None is truthy) {
        // Source: vvaharness/util/json_extract.py:127-127
        In source order: Apply source augmented assignment i += len(span) with source evaluation/in-place semantics.
        // Source: vvaharness/util/json_extract.py:128-128
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/util/json_extract.py:129-133
      if (the source predicate want_dict and isinstance(val, list) is truthy) {
        // Source: vvaharness/util/json_extract.py:130-131
        if (the source predicate held_list is None is truthy) {
          // Source: vvaharness/util/json_extract.py:131-131
          In source order: Evaluate once val; assign in source target order to held_list.
        }
        // Source: vvaharness/util/json_extract.py:132-132
        In source order: Apply source augmented assignment i += len(span) with source evaluation/in-place semantics.
        // Source: vvaharness/util/json_extract.py:133-133
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/util/json_extract.py:134-134
      End this invocation with val.
    }
  }
  // Source: vvaharness/util/json_extract.py:136-137
  if (the source predicate held_list is not None is truthy) {
    // Source: vvaharness/util/json_extract.py:137-137
    End this invocation with held_list.
  }
  // Source: vvaharness/util/json_extract.py:138-139
  if (the source predicate last_err is truthy) {
    // Source: vvaharness/util/json_extract.py:139-139
    Raise last_err.
  }
  // Source: vvaharness/util/json_extract.py:140-140
  Raise ValueError('no JSON object found in response').
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 21: `source_detail/vvaharness/util/events.py.sudo.md`.
