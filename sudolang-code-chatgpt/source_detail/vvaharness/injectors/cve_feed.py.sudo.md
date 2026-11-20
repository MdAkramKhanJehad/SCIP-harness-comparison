# vvaharness/injectors/cve_feed.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/injectors/cve_feed.py.evidence.json`. SHA-256: `6151a13f35ff72f6e6b71bd81d704dbf352443c1d846468fa7b7393a0937eb06`.

```sudo
// Source: vvaharness/injectors/cve_feed.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/injectors/cve_feed.py:23-29
In source order: Resolve source import from pydantic import ValidationError; preserve alias and import-time effects. Then Resolve source import from vvaharness.models import CVE; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import errlog as _errlog; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/injectors/cve_feed.py:32-80
// Source signature: load_cves(path: str | Path) -> list[CVE]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_cves(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/injectors/cve_feed.py:33-33
  In source order: Evaluate once Path(path); assign in source target order to p.
  // Source: vvaharness/injectors/cve_feed.py:34-35
  if (the source predicate not p.exists() is truthy) {
    // Source: vvaharness/injectors/cve_feed.py:35-35
    End this invocation with [].
  }
  // Source: vvaharness/injectors/cve_feed.py:40-63
  Perform the following protected operations {
    // Source: vvaharness/injectors/cve_feed.py:41-41
    In source order: Evaluate once json.loads(p.read_text(encoding='utf-8')); assign in source target order to data.
    // Source: vvaharness/injectors/cve_feed.py:46-53
    if (the source predicate isinstance(data, dict) is truthy) {
      // Source: vvaharness/injectors/cve_feed.py:47-47
      In source order: Evaluate once data.get('cves'); assign in source target order to items.
      // Source: vvaharness/injectors/cve_feed.py:48-51
      if (the source predicate items is None is truthy) {
        // Source: vvaharness/injectors/cve_feed.py:49-51
        Raise ValueError('CVE feed is a JSON object without a \'cves\' key — expected a list or {"cves": [...]}').
      }
    }
    else {
      // Source: vvaharness/injectors/cve_feed.py:53-53
      In source order: Evaluate once data; assign in source target order to items.
    }
    // Source: vvaharness/injectors/cve_feed.py:57-59
    if (the source predicate not isinstance(items, list) is truthy) {
      // Source: vvaharness/injectors/cve_feed.py:58-59
      Raise TypeError(source_template_59_16).
    }
  }
  // Source: vvaharness/injectors/cve_feed.py:60-63
  On the first matching source exception (OSError, ValueError, TypeError) as e, in handler order {
    // Source: vvaharness/injectors/cve_feed.py:61-62
    In source order: Evaluate log.warning(Event.CVE_FEED_UNREADABLE, path=p, error=type(e).__name__, detail=str(e)); retain side effects and discard the expression result. Then Evaluate _errlog.log('inject.cves', str(p), e); retain side effects and discard the expression result.
    // Source: vvaharness/injectors/cve_feed.py:63-63
    End this invocation with [].
  }
  // Source: vvaharness/injectors/cve_feed.py:68-69
  In source order: For out, assign []; source annotation list[CVE]. Then Evaluate once 0; assign in source target order to skipped.
  // Source: vvaharness/injectors/cve_feed.py:70-77
  for each (idx, item) in enumerate(items) {
    // Source: vvaharness/injectors/cve_feed.py:71-77
    Perform the following protected operations {
      // Source: vvaharness/injectors/cve_feed.py:72-72
      In source order: Evaluate out.append(CVE.model_validate(item)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/injectors/cve_feed.py:73-77
    On the first matching source exception (ValidationError, TypeError, ValueError) as e, in handler order {
      // Source: vvaharness/injectors/cve_feed.py:74-77
      In source order: Apply source augmented assignment skipped += 1 with source evaluation/in-place semantics. Then Evaluate once item.get('id') if isinstance(item, dict) else None; assign in source target order to cid. Then Evaluate once source_template_76_19 + (source_template_76_35 if cid else ''); assign in source target order to unit. Then Evaluate _errlog.log('inject.cves.item', unit, e); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/injectors/cve_feed.py:78-79
  if (the source predicate skipped is truthy) {
    // Source: vvaharness/injectors/cve_feed.py:79-79
    In source order: Evaluate log.warning(Event.CVE_FEED_RECORDS_SKIPPED, path=p, skipped=skipped, loaded=len(out)); retain side effects and discard the expression result.
  }
  // Source: vvaharness/injectors/cve_feed.py:80-80
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 18: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.models import CVE` at source line 25: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import errlog as _errlog` at source line 26: `source_detail/vvaharness/util/errlog.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 27: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/injectors/cve_feed.py.sudo.md). Exact strings in the evidence asset support this conversion.
