# vvaharness/rules/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/rules/__init__.py.evidence.json`. SHA-256: `063c1d526225fc7984be9ee34c51731ceccff22d017f89f4b15cb9c6755779bc`.

```sudo
// Source: vvaharness/rules/__init__.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects.
// Source: vvaharness/rules/__init__.py:22-29
In source order: Resolve source import import yaml; preserve alias and import-time effects. Then Resolve source import from vvaharness.rules.cwe import norm_cwe as _norm_cwe; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects. Then Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once ['RULES_DIR', 'CweKB']; assign in source target order to __all__.
// Source: vvaharness/rules/__init__.py:31-36
In source order: Evaluate once Path(__file__).resolve().parent; assign in source target order to RULES_DIR. Then Evaluate once ('sources', 'sinks', 'sanitizers', 'non_sanitizers', 'fp_checks'); assign in source target order to _LIST_KEYS. Then Evaluate once re.compile('^([a-z][a-z0-9_+-]{0,15}):\\s+(.+)$'); assign in source target order to _LANG_PREFIX_RX.
// Source: vvaharness/rules/__init__.py:39-52
// Source signature: _filter_lang(items: list[str], lang: str | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _filter_lang(items, lang) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/rules/__init__.py:40-42
  In source order: Retain source documentation literal source_literal_40_4; it is not a model call. Then For out, assign []; source annotation list[str]. Then For seen, assign set(); source annotation set[str].
  // Source: vvaharness/rules/__init__.py:43-51
  for each it in items {
    // Source: vvaharness/rules/__init__.py:44-44
    In source order: Evaluate once _LANG_PREFIX_RX.match(it); assign in source target order to m.
    // Source: vvaharness/rules/__init__.py:45-48
    if (the source predicate m is truthy) {
      // Source: vvaharness/rules/__init__.py:46-47
      if (the source predicate lang is not None and m.group(1) != lang is truthy) {
        // Source: vvaharness/rules/__init__.py:47-47
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/rules/__init__.py:48-48
      In source order: Evaluate once m.group(2); assign in source target order to it.
    }
    // Source: vvaharness/rules/__init__.py:49-51
    if (the source predicate it not in seen is truthy) {
      // Source: vvaharness/rules/__init__.py:50-51
      In source order: Evaluate seen.add(it); retain side effects and discard the expression result. Then Evaluate out.append(it); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/rules/__init__.py:52-52
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/rules/__init__.py:55-213
interface CweKB {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/rules/__init__.py:56-56
  In source order: Retain source documentation literal source_literal_56_4; it is not a model call.
  // Source: vvaharness/rules/__init__.py:59-60
  // Source signature: __init__(self, by_cwe: dict[str, dict])
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, by_cwe) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:60-60
    In source order: Evaluate once by_cwe; assign in source target order to self._by_cwe.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/rules/__init__.py:62-63
  // Source signature: __len__(self) -> int
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __len__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:63-63
    End this invocation with len(self._by_cwe).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/rules/__init__.py:65-67
  // Source signature: __contains__(self, cwe) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __contains__(self, cwe) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:66-66
    In source order: Evaluate once _norm_cwe(cwe); assign in source target order to c.
    // Source: vvaharness/rules/__init__.py:67-67
    End this invocation with c is not None and c in self._by_cwe.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/rules/__init__.py:69-69
  In source order: For _cache, assign None; source annotation CweKB | None.
  // Source: vvaharness/rules/__init__.py:72-90
  // Source: vvaharness/rules/__init__.py:71-71
  Before creating this callable, evaluate and retain decorators top-to-bottom: classmethod.
  // Source: vvaharness/rules/__init__.py:72-90
  // Source signature: load(cls, rules_dir: Path | None=None, *, overlays=None, include_all_extras: bool=False) -> CweKB
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn load(cls, rules_dir, overlays, include_all_extras) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:74-77
    In source order: Retain source documentation literal source_literal_74_8; it is not a model call. Then Evaluate once rules_dir is None; assign in source target order to use_default. Then Evaluate once cls._overlay_list(overlays); assign in source target order to overlay_list. Then Evaluate once use_default and (not overlay_list) and (not include_all_extras); assign in source target order to cacheable.
    // Source: vvaharness/rules/__init__.py:78-79
    if (the source predicate cacheable and cls._cache is not None is truthy) {
      // Source: vvaharness/rules/__init__.py:79-79
      End this invocation with cls._cache.
    }
    // Source: vvaharness/rules/__init__.py:80-82
    In source order: Evaluate once Path(rules_dir) if rules_dir else RULES_DIR; assign in source target order to d. Then For merged, assign {}; source annotation dict[str, dict]. Then Evaluate once include_all_extras or rules_dir is not None; assign in source target order to include_extras.
    // Source: vvaharness/rules/__init__.py:83-86
    for each p in cls._kb_files(d, overlays=overlay_list, include_all_extras=include_extras) {
      // Source: vvaharness/rules/__init__.py:85-86
      for each entry in cls._read(p) {
        // Source: vvaharness/rules/__init__.py:86-86
        In source order: Evaluate cls._merge(merged, entry); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/rules/__init__.py:87-87
    In source order: Evaluate once cls(merged); assign in source target order to kb.
    // Source: vvaharness/rules/__init__.py:88-89
    if (the source predicate cacheable is truthy) {
      // Source: vvaharness/rules/__init__.py:89-89
      In source order: Evaluate once kb; assign in source target order to cls._cache.
    }
    // Source: vvaharness/rules/__init__.py:90-90
    End this invocation with kb.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/rules/__init__.py:93-98
  // Source: vvaharness/rules/__init__.py:92-92
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/rules/__init__.py:93-98
  // Source signature: _overlay_list(overlays) -> list[str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _overlay_list(overlays) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:94-95
    if (the source predicate overlays is None is truthy) {
      // Source: vvaharness/rules/__init__.py:95-95
      End this invocation with [].
    }
    // Source: vvaharness/rules/__init__.py:96-97
    if (the source predicate isinstance(overlays, (str, Path)) is truthy) {
      // Source: vvaharness/rules/__init__.py:97-97
      End this invocation with [str(overlays)].
    }
    // Source: vvaharness/rules/__init__.py:98-98
    End this invocation with [str(p) for p in overlays if str(p).strip()].
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/rules/__init__.py:101-122
  // Source: vvaharness/rules/__init__.py:100-100
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/rules/__init__.py:101-122
  // Source signature: _kb_files(d: Path, *, overlays=None, include_all_extras: bool=False) -> list[Path]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _kb_files(d, overlays, include_all_extras) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:103-104
    if (the source predicate not d.is_dir() is truthy) {
      // Source: vvaharness/rules/__init__.py:104-104
      End this invocation with [].
    }
    // Source: vvaharness/rules/__init__.py:105-105
    In source order: For files, assign []; source annotation list[Path].
    // Source: vvaharness/rules/__init__.py:107-110
    for each name in ('cwe_kb.yaml', 'generic.kb.yaml') {
      // Source: vvaharness/rules/__init__.py:108-108
      In source order: Evaluate once d / name; assign in source target order to p.
      // Source: vvaharness/rules/__init__.py:109-110
      if (the source predicate p.is_file() and p not in files is truthy) {
        // Source: vvaharness/rules/__init__.py:110-110
        In source order: Evaluate files.append(p); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/rules/__init__.py:111-114
    if (the source predicate include_all_extras is truthy) {
      // Source: vvaharness/rules/__init__.py:112-114
      for each p in sorted((x for x in d.glob('*.kb.yaml') if x.is_file())) {
        // Source: vvaharness/rules/__init__.py:113-114
        if (the source predicate p not in files is truthy) {
          // Source: vvaharness/rules/__init__.py:114-114
          In source order: Evaluate files.append(p); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/rules/__init__.py:115-121
    for each raw in CweKB._overlay_list(overlays) {
      // Source: vvaharness/rules/__init__.py:116-116
      In source order: Evaluate once Path(raw); assign in source target order to p.
      // Source: vvaharness/rules/__init__.py:117-119
      if (the source predicate not p.is_absolute() is truthy) {
        // Source: vvaharness/rules/__init__.py:118-119
        In source order: Evaluate once d / p; assign in source target order to candidate. Then Evaluate once candidate if candidate.is_file() else p; assign in source target order to p.
      }
      // Source: vvaharness/rules/__init__.py:120-121
      if (the source predicate p.is_file() and p not in files is truthy) {
        // Source: vvaharness/rules/__init__.py:121-121
        In source order: Evaluate files.append(p); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/rules/__init__.py:122-122
    End this invocation with files.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/rules/__init__.py:125-132
  // Source: vvaharness/rules/__init__.py:124-124
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/rules/__init__.py:125-132
  // Source signature: _read(p: Path) -> list[dict]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _read(p) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:126-130
    Perform the following protected operations {
      // Source: vvaharness/rules/__init__.py:127-127
      In source order: Evaluate once yaml.safe_load(p.read_text(encoding='utf-8')) or {}; assign in source target order to doc.
    }
    // Source: vvaharness/rules/__init__.py:128-130
    On the first matching source exception (OSError, yaml.YAMLError) as e, in handler order {
      // Source: vvaharness/rules/__init__.py:129-129
      In source order: Evaluate log.warning(Event.RULEPACK_LOAD_FAILED, pack=p.name, detail=str(e)); retain side effects and discard the expression result.
      // Source: vvaharness/rules/__init__.py:130-130
      End this invocation with [].
    }
    // Source: vvaharness/rules/__init__.py:131-131
    In source order: Evaluate once doc.get('entries') if isinstance(doc, dict) else None; assign in source target order to entries.
    // Source: vvaharness/rules/__init__.py:132-132
    End this invocation with [e for e in entries or [] if isinstance(e, dict)].
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/rules/__init__.py:135-155
  // Source: vvaharness/rules/__init__.py:134-134
  Before creating this callable, evaluate and retain decorators top-to-bottom: staticmethod.
  // Source: vvaharness/rules/__init__.py:135-155
  // Source signature: _merge(acc: dict[str, dict], entry: dict) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _merge(acc, entry) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:136-136
    In source order: Evaluate once _norm_cwe(entry.get('cwe')); assign in source target order to cwe.
    // Source: vvaharness/rules/__init__.py:137-138
    if (the source predicate not cwe is truthy) {
      // Source: vvaharness/rules/__init__.py:138-138
      End this invocation with None.
    }
    // Source: vvaharness/rules/__init__.py:139-140
    In source order: Evaluate once acc.setdefault(cwe, {'cwe': cwe, 'title': '', 'origin': [], **{k: [] for k in _LIST_KEYS}}); assign in source target order to slot.
    // Source: vvaharness/rules/__init__.py:141-142
    if (the source predicate not slot['title'] is truthy) {
      // Source: vvaharness/rules/__init__.py:142-142
      In source order: Evaluate once str(entry.get('title') or ''); assign in source target order to slot['title'].
    }
    // Source: vvaharness/rules/__init__.py:143-143
    In source order: Evaluate once str(entry.get('origin') or ''); assign in source target order to origin.
    // Source: vvaharness/rules/__init__.py:144-145
    if (the source predicate origin and origin not in slot['origin'] is truthy) {
      // Source: vvaharness/rules/__init__.py:145-145
      In source order: Evaluate slot['origin'].append(origin); retain side effects and discard the expression result.
    }
    // Source: vvaharness/rules/__init__.py:146-150
    for each k in _LIST_KEYS {
      // Source: vvaharness/rules/__init__.py:147-150
      for each v in entry.get(k) or () {
        // Source: vvaharness/rules/__init__.py:148-148
        In source order: Evaluate once str(v).strip(); assign in source target order to v.
        // Source: vvaharness/rules/__init__.py:149-150
        if (the source predicate v and v not in slot[k] is truthy) {
          // Source: vvaharness/rules/__init__.py:150-150
          In source order: Evaluate slot[k].append(v); retain side effects and discard the expression result.
        }
      }
    }
    // Source: vvaharness/rules/__init__.py:152-155
    for each a in entry.get('aliases') or () {
      // Source: vvaharness/rules/__init__.py:153-153
      In source order: Evaluate once _norm_cwe(a); assign in source target order to an.
      // Source: vvaharness/rules/__init__.py:154-155
      if (the source predicate an and an not in acc is truthy) {
        // Source: vvaharness/rules/__init__.py:155-155
        In source order: Evaluate once slot; assign in source target order to acc[an].
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/rules/__init__.py:157-180
  // Source signature: for_cwes(self, cwes, lang: str | None=None) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn for_cwes(self, cwes, lang) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:158-158
    In source order: Retain source documentation literal source_literal_158_8; it is not a model call.
    // Source: vvaharness/rules/__init__.py:159-160
    if (the source predicate isinstance(cwes, str) is truthy) {
      // Source: vvaharness/rules/__init__.py:160-160
      In source order: Evaluate once [cwes]; assign in source target order to cwes.
    }
    // Source: vvaharness/rules/__init__.py:161-163
    In source order: Evaluate once {'cwe': [], 'title': [], 'origin': [], **{k: [] for k in _LIST_KEYS}}; assign in source target order to out. Then For seen_slots, assign set(); source annotation set[int].
    // Source: vvaharness/rules/__init__.py:164-179
    for each c in cwes or () {
      // Source: vvaharness/rules/__init__.py:165-166
      In source order: Evaluate once _norm_cwe(c); assign in source target order to cn. Then Evaluate once self._by_cwe.get(cn) if cn else None; assign in source target order to slot.
      // Source: vvaharness/rules/__init__.py:167-168
      if (the source predicate slot is None or id(slot) in seen_slots is truthy) {
        // Source: vvaharness/rules/__init__.py:168-168
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/rules/__init__.py:169-170
      In source order: Evaluate seen_slots.add(id(slot)); retain side effects and discard the expression result. Then Evaluate out['cwe'].append(slot['cwe']); retain side effects and discard the expression result.
      // Source: vvaharness/rules/__init__.py:171-172
      if (the source predicate slot['title'] is truthy) {
        // Source: vvaharness/rules/__init__.py:172-172
        In source order: Evaluate out['title'].append(slot['title']); retain side effects and discard the expression result.
      }
      // Source: vvaharness/rules/__init__.py:173-175
      for each o in slot['origin'] {
        // Source: vvaharness/rules/__init__.py:174-175
        if (the source predicate o not in out['origin'] is truthy) {
          // Source: vvaharness/rules/__init__.py:175-175
          In source order: Evaluate out['origin'].append(o); retain side effects and discard the expression result.
        }
      }
      // Source: vvaharness/rules/__init__.py:176-179
      for each k in _LIST_KEYS {
        // Source: vvaharness/rules/__init__.py:177-179
        for each v in _filter_lang(slot[k], lang) {
          // Source: vvaharness/rules/__init__.py:178-179
          if (the source predicate v not in out[k] is truthy) {
            // Source: vvaharness/rules/__init__.py:179-179
            In source order: Evaluate out[k].append(v); retain side effects and discard the expression result.
          }
        }
      }
    }
    // Source: vvaharness/rules/__init__.py:180-180
    End this invocation with out.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/rules/__init__.py:182-213
  // Source signature: prompt_block(self, cwes, lang: str | None=None, limit: int=20) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn prompt_block(self, cwes, lang, limit) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/rules/__init__.py:184-185
    In source order: Retain source documentation literal source_literal_184_8; it is not a model call. Then Evaluate once self.for_cwes(cwes, lang); assign in source target order to ctx.
    // Source: vvaharness/rules/__init__.py:186-187
    if (the source predicate not any((ctx[k] for k in _LIST_KEYS)) is truthy) {
      // Source: vvaharness/rules/__init__.py:187-187
      End this invocation with ''.
    }
    // Source: vvaharness/rules/__init__.py:188-189
    In source order: Evaluate once ' / '.join(ctx['title']) or ', '.join(ctx['cwe']); assign in source target order to title. Then Evaluate once source_template_189_15; assign in source target order to head.
    // Source: vvaharness/rules/__init__.py:190-191
    if (the source predicate ctx['origin'] is truthy) {
      // Source: vvaharness/rules/__init__.py:191-191
      In source order: Apply source augmented assignment head += source_template_191_20 with source evaluation/in-place semantics.
    }
    // Source: vvaharness/rules/__init__.py:192-204
    In source order: Evaluate once [head]; assign in source target order to lines. Then Evaluate once (('sanitizers', 'SANITIZERS — if ANY of these sits on the path, REFUTE:'), ('non_sanitizers', 'NON-SANITIZERS — these look safe but are NOT; do NOT refute on their basis alone:'), ('fp_checks', 'FP CHECKS — if ANY is true, REFUTE:'), ('sinks', 'KNOWN SINKS — for reference; the candidate sink should match one of these shapes:')); assign in source target order to labels.
    // Source: vvaharness/rules/__init__.py:205-212
    for each (key, label) in labels {
      // Source: vvaharness/rules/__init__.py:206-206
      In source order: Evaluate once ctx[key][:limit]; assign in source target order to items.
      // Source: vvaharness/rules/__init__.py:207-208
      if (the source predicate not items is truthy) {
        // Source: vvaharness/rules/__init__.py:208-208
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/rules/__init__.py:209-210
      In source order: Evaluate lines.append(source_template_209_25); retain side effects and discard the expression result. Then Evaluate lines.extend((source_template_210_25 for it in items)); retain side effects and discard the expression result.
      // Source: vvaharness/rules/__init__.py:211-212
      if (the source predicate len(ctx[key]) > limit is truthy) {
        // Source: vvaharness/rules/__init__.py:212-212
        In source order: Evaluate lines.append(source_template_212_29); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/rules/__init__.py:213-213
    End this invocation with source_literal_213_15.join(lines) + source_literal_213_34.
    If execution reaches this end, finish with the source implicit None result.
  }
}
```

## Local import links

- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 17: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.rules.cwe import norm_cwe as _norm_cwe` at source line 24: `source_detail/vvaharness/rules/cwe.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 25: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/rules/__init__.py.sudo.md). Exact strings in the evidence asset support this conversion.
