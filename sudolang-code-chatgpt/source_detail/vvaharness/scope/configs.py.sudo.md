# vvaharness/scope/configs.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/scope/configs.py.evidence.json`. SHA-256: `6e332b06f5d3317a5cc86e84e590a767384a332f55865b905e3b72853d25dc53`.

```sudo
// Source: vvaharness/scope/configs.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import configparser; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import json; preserve alias and import-time effects.
// Source: vvaharness/scope/configs.py:21-26
In source order: Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from collections import defaultdict; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from vvaharness.scope.walk import _DEDUP_DEFAULTS, _INSECURE_RX, _SECRET_RX; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import console, logs; preserve alias and import-time effects.
// Source: vvaharness/scope/configs.py:28-28
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log.
// Source: vvaharness/scope/configs.py:30-41
// Source signature: _flatten_keys(obj, prefix: str='') -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _flatten_keys(obj, prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/configs.py:31-35
  if (the source predicate isinstance(obj, dict) is truthy) {
    // Source: vvaharness/scope/configs.py:32-32
    In source order: For out, assign []; source annotation list[str].
    // Source: vvaharness/scope/configs.py:33-34
    for each k in obj {
      // Source: vvaharness/scope/configs.py:34-34
      In source order: Evaluate out.extend(_flatten_keys(obj[k], source_template_34_45 if prefix else str(k))); retain side effects and discard the expression result.
    }
    // Source: vvaharness/scope/configs.py:35-35
    End this invocation with out or [prefix].
  }
  // Source: vvaharness/scope/configs.py:36-40
  if (the source predicate isinstance(obj, list) is truthy) {
    // Source: vvaharness/scope/configs.py:37-37
    In source order: Evaluate once []; assign in source target order to out.
    // Source: vvaharness/scope/configs.py:38-39
    for each it in obj {
      // Source: vvaharness/scope/configs.py:39-39
      In source order: Evaluate out.extend(_flatten_keys(it, source_template_39_41)); retain side effects and discard the expression result.
    }
    // Source: vvaharness/scope/configs.py:40-40
    End this invocation with out or [prefix].
  }
  // Source: vvaharness/scope/configs.py:41-41
  End this invocation with [prefix].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/configs.py:44-45
In source order: Evaluate once re.compile('^\\s*([A-Za-z0-9_.\\-]+)\\s*[:=]'); assign in source target order to _KV_LINE_RX. Then Evaluate once re.compile('^( *)(?:- +)?([\\w.\\-]+)\\s*:'); assign in source target order to _YAML_KEY_RX.
// Source: vvaharness/scope/configs.py:48-82
// Source signature: _shape_hash(text: str, ext: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _shape_hash(text, ext) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/configs.py:49-50
  In source order: Retain source documentation literal source_literal_49_4; it is not a model call. Then For keys, assign []; source annotation list[str].
  // Source: vvaharness/scope/configs.py:51-79
  Perform the following protected operations {
    // Source: vvaharness/scope/configs.py:52-77
    if (the source predicate ext in ('.yml', '.yaml') is truthy) {
      // Source: vvaharness/scope/configs.py:53-53
      In source order: For stack, assign []; source annotation list[tuple[int, str]].
      // Source: vvaharness/scope/configs.py:54-64
      for each ln in text.splitlines() {
        // Source: vvaharness/scope/configs.py:55-56
        if (the source predicate not ln or ln.lstrip().startswith('#') is truthy) {
          // Source: vvaharness/scope/configs.py:56-56
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/scope/configs.py:57-57
        In source order: Evaluate once _YAML_KEY_RX.match(ln); assign in source target order to m.
        // Source: vvaharness/scope/configs.py:58-59
        if (the source predicate not m is truthy) {
          // Source: vvaharness/scope/configs.py:59-59
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vvaharness/scope/configs.py:60-60
        In source order: Evaluate once (len(m.group(1)), m.group(2)); assign in source target order to (indent, name).
        // Source: vvaharness/scope/configs.py:61-62
        while (the source predicate stack and stack[-1][0] >= indent is truthy) {
          // Source: vvaharness/scope/configs.py:62-62
          In source order: Evaluate stack.pop(); retain side effects and discard the expression result.
        }
        // Source: vvaharness/scope/configs.py:63-64
        In source order: Evaluate stack.append((indent, name)); retain side effects and discard the expression result. Then Evaluate keys.append('.'.join((n for _, n in stack))); retain side effects and discard the expression result.
      }
    }
    else {
      // Source: vvaharness/scope/configs.py:65-77
      if (the source predicate ext == '.json' is truthy) {
        // Source: vvaharness/scope/configs.py:66-66
        In source order: Evaluate once _flatten_keys(json.loads(text)); assign in source target order to keys.
      }
      else {
        // Source: vvaharness/scope/configs.py:67-77
        if (the source predicate ext in ('.ini', '.cfg', '.conf') is truthy) {
          // Source: vvaharness/scope/configs.py:68-69
          In source order: Evaluate once configparser.ConfigParser(strict=False, allow_no_value=True); assign in source target order to cp. Then Evaluate cp.read_string(text); retain side effects and discard the expression result.
          // Source: vvaharness/scope/configs.py:70-72
          for each sec in cp.sections() {
            // Source: vvaharness/scope/configs.py:71-72
            for each opt in cp.options(sec) {
              // Source: vvaharness/scope/configs.py:72-72
              In source order: Evaluate keys.append(source_template_72_32); retain side effects and discard the expression result.
            }
          }
        }
        else {
          // Source: vvaharness/scope/configs.py:74-77
          for each ln in text.splitlines() {
            // Source: vvaharness/scope/configs.py:75-75
            In source order: Evaluate once _KV_LINE_RX.match(ln); assign in source target order to m.
            // Source: vvaharness/scope/configs.py:76-77
            if (the source predicate m is truthy) {
              // Source: vvaharness/scope/configs.py:77-77
              In source order: Evaluate keys.append(m.group(1)); retain side effects and discard the expression result.
            }
          }
        }
      }
    }
  }
  // Source: vvaharness/scope/configs.py:78-79
  On the first matching source exception Exception, in handler order {
    // Source: vvaharness/scope/configs.py:79-79
    End this invocation with None.
  }
  // Source: vvaharness/scope/configs.py:80-81
  if (the source predicate not keys is truthy) {
    // Source: vvaharness/scope/configs.py:81-81
    End this invocation with None.
  }
  // Source: vvaharness/scope/configs.py:82-82
  End this invocation with hashlib.sha1(source_literal_82_24.join(sorted(set(keys))).encode()).hexdigest().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/configs.py:85-94
// Source signature: _suspicious_set(text: str, want_secret: bool, want_insecure: bool) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _suspicious_set(text, want_secret, want_insecure) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/configs.py:86-87
  In source order: Retain source documentation literal source_literal_86_4; it is not a model call. Then For out, assign set(); source annotation set[str].
  // Source: vvaharness/scope/configs.py:88-90
  if (the source predicate want_secret is truthy) {
    // Source: vvaharness/scope/configs.py:89-90
    for each m in _SECRET_RX.finditer(text) {
      // Source: vvaharness/scope/configs.py:90-90
      In source order: Evaluate out.add('secret:' + re.sub('\\s+', ' ', m.group(0))[:80]); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/scope/configs.py:91-93
  if (the source predicate want_insecure is truthy) {
    // Source: vvaharness/scope/configs.py:92-93
    for each m in _INSECURE_RX.finditer(text) {
      // Source: vvaharness/scope/configs.py:93-93
      In source order: Evaluate out.add('insecure:' + re.sub('\\s+', ' ', m.group(0))[:80]); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/scope/configs.py:94-94
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/configs.py:97-97
In source order: Evaluate once re.compile('[A-Za-z0-9_.\\-]+(?=[ \\t]*[:=])'); assign in source target order to _REASON_KEY_RX.
// Source: vvaharness/scope/configs.py:100-111
// Source signature: _promotion_reason(entry: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _promotion_reason(entry) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/configs.py:101-104
  In source order: Retain source documentation literal source_literal_101_4; it is not a model call. Then Evaluate once entry.partition(':'); assign in source target order to (label, _, hit). Then Evaluate once _REASON_KEY_RX.match(hit); assign in source target order to m.
  // Source: vvaharness/scope/configs.py:105-106
  if (the source predicate m is truthy) {
    // Source: vvaharness/scope/configs.py:106-106
    End this invocation with source_template_106_15.
  }
  // Source: vvaharness/scope/configs.py:107-108
  if (the source predicate hit.startswith('-----BEGIN') is truthy) {
    // Source: vvaharness/scope/configs.py:108-108
    End this invocation with source_template_108_15.
  }
  // Source: vvaharness/scope/configs.py:109-110
  if (the source predicate hit.startswith(('AKIA', 'eyJ')) is truthy) {
    // Source: vvaharness/scope/configs.py:110-110
    End this invocation with source_template_110_15.
  }
  // Source: vvaharness/scope/configs.py:111-111
  End this invocation with label.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/configs.py:114-121
// Source signature: _rep_score(rel: str, size: int) -> tuple
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rep_score(rel, size) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/configs.py:115-120
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call. Then Evaluate once rel.lower(); assign in source target order to low. Then Evaluate once 0 if '/prod' in low else 1 if any((e in low for e in ('/cert', '/stag', '/stg'))) else 2 if any((e in low for e in ('/perf', '/qa'))) else 3; assign in source target order to env.
  // Source: vvaharness/scope/configs.py:121-121
  End this invocation with (env, -size, rel).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/scope/configs.py:124-271
// Source signature: _dedup_configs(files: list[str], repo_root: Path, cfg) -> tuple[list[str], dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dedup_configs(files, repo_root, cfg) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/scope/configs.py:125-126
  In source order: Evaluate once dict(_DEDUP_DEFAULTS); assign in source target order to dd. Then Evaluate once getattr(getattr(cfg, 'step1', None), 'config_dedup', None); assign in source target order to user.
  // Source: vvaharness/scope/configs.py:127-130
  if (the source predicate user is not None is truthy) {
    // Source: vvaharness/scope/configs.py:128-130
    In source order: Evaluate once user if isinstance(user, dict) else getattr(user, '_data', None) or vars(user); assign in source target order to raw. Then Evaluate dd.update({k: v for k, v in raw.items() if v is not None}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/scope/configs.py:131-132
  if (the source predicate not dd['enabled'] is truthy) {
    // Source: vvaharness/scope/configs.py:132-132
    End this invocation with (files, {'enabled': False}).
  }
  // Source: vvaharness/scope/configs.py:134-139
  In source order: Evaluate once {e.lower() for e in dd['exts']}; assign in source target order to exts. Then Evaluate once int(dd['min_cluster_size']); assign in source target order to min_cluster. Then Evaluate once int(dd['max_file_kb']) * 1024; assign in source target order to max_bytes. Then For candidates, assign []; source annotation list[str]. Then For passthrough, assign []; source annotation list[str].
  // Source: vvaharness/scope/configs.py:140-144
  for each rel in files {
    // Source: vvaharness/scope/configs.py:141-144
    if (the source predicate Path(rel).suffix.lower() in exts is truthy) {
      // Source: vvaharness/scope/configs.py:142-142
      In source order: Evaluate candidates.append(rel); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/scope/configs.py:144-144
      In source order: Evaluate passthrough.append(rel); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/scope/configs.py:146-148
  if (the source predicate len(candidates) < min_cluster is truthy) {
    // Source: vvaharness/scope/configs.py:147-148
    End this invocation with (files, {'enabled': True, 'candidates': len(candidates), 'clusters': 0, 'dropped': 0, 'promoted': 0}).
  }
  // Source: vvaharness/scope/configs.py:150-151
  In source order: Evaluate once dd['promote_on_secret_hit']; assign in source target order to want_sec. Then Evaluate once dd['promote_on_insecure_value']; assign in source target order to want_ins.
  // Source: vvaharness/scope/configs.py:154-163
  // Source signature: _hash(rel: str)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _hash(rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/scope/configs.py:155-155
    In source order: Evaluate once repo_root / rel; assign in source target order to p.
    // Source: vvaharness/scope/configs.py:156-162
    Perform the following protected operations {
      // Source: vvaharness/scope/configs.py:157-157
      In source order: Evaluate once p.stat().st_size; assign in source target order to sz.
      // Source: vvaharness/scope/configs.py:158-159
      if (the source predicate sz > max_bytes is truthy) {
        // Source: vvaharness/scope/configs.py:159-159
        End this invocation with (rel, sz, None).
      }
      // Source: vvaharness/scope/configs.py:160-160
      In source order: Evaluate once p.read_text(encoding='utf-8', errors='replace'); assign in source target order to text.
    }
    // Source: vvaharness/scope/configs.py:161-162
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/scope/configs.py:162-162
      End this invocation with (rel, 0, None).
    }
    // Source: vvaharness/scope/configs.py:163-163
    End this invocation with (rel, sz, _shape_hash(text, p.suffix.lower())).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/scope/configs.py:165-168
  In source order: For clusters, assign defaultdict(list); source annotation dict[str, list[tuple[str, int]]]. Then For unclustered, assign []; source annotation list[str]. Then Resolve source import from concurrent.futures import ThreadPoolExecutor; preserve alias and import-time effects. Then Evaluate once int(dd.get('io_workers', 16)); assign in source target order to workers.
  // Source: vvaharness/scope/configs.py:169-174
  Enter source context managers left-to-right: ThreadPoolExecutor(max_workers=workers) bound to ex {
    // Source: vvaharness/scope/configs.py:170-174
    for each (rel, sz, h) in ex.map(_hash, candidates) {
      // Source: vvaharness/scope/configs.py:171-174
      if (the source predicate h is None is truthy) {
        // Source: vvaharness/scope/configs.py:172-172
        In source order: Evaluate unclustered.append(rel); retain side effects and discard the expression result.
      }
      else {
        // Source: vvaharness/scope/configs.py:174-174
        In source order: Evaluate clusters[h].append((rel, sz)); retain side effects and discard the expression result.
      }
    }
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  // Source: vvaharness/scope/configs.py:176-183
  In source order: For keep, assign list(passthrough) + unclustered; source annotation list[str]. Then For promoted, assign []; source annotation list[tuple[str, str]]. Then For dropped, assign []; source annotation list[str]. Then For cluster_report, assign []; source annotation list[dict]. Then Evaluate once [rel for members in clusters.values() if len(members) >= min_cluster for rel, _ in members]; assign in source target order to need_sus.
  // Source: vvaharness/scope/configs.py:185-193
  // Source signature: _susload(rel: str)
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _susload(rel) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/scope/configs.py:186-186
    In source order: Evaluate once repo_root / rel; assign in source target order to p.
    // Source: vvaharness/scope/configs.py:187-192
    Perform the following protected operations {
      // Source: vvaharness/scope/configs.py:188-189
      if (the source predicate p.stat().st_size > max_bytes is truthy) {
        // Source: vvaharness/scope/configs.py:189-189
        End this invocation with (rel, None).
      }
      // Source: vvaharness/scope/configs.py:190-190
      In source order: Evaluate once p.read_text(encoding='utf-8', errors='replace'); assign in source target order to text.
    }
    // Source: vvaharness/scope/configs.py:191-192
    On the first matching source exception OSError, in handler order {
      // Source: vvaharness/scope/configs.py:192-192
      End this invocation with (rel, None).
    }
    // Source: vvaharness/scope/configs.py:193-193
    End this invocation with (rel, _suspicious_set(text, want_sec, want_ins)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/scope/configs.py:195-195
  In source order: For sus_by_rel, assign {}; source annotation dict[str, set[str]].
  // Source: vvaharness/scope/configs.py:196-200
  if (the source predicate need_sus is truthy) {
    // Source: vvaharness/scope/configs.py:197-200
    Enter source context managers left-to-right: ThreadPoolExecutor(max_workers=workers) bound to ex {
      // Source: vvaharness/scope/configs.py:198-200
      for each (rel, sus) in ex.map(_susload, need_sus) {
        // Source: vvaharness/scope/configs.py:199-200
        if (the source predicate sus is not None is truthy) {
          // Source: vvaharness/scope/configs.py:200-200
          In source order: Evaluate once sus; assign in source target order to sus_by_rel[rel].
        }
      }
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/scope/configs.py:203-243
  for each (h, members) in clusters.items() {
    // Source: vvaharness/scope/configs.py:204-206
    if (the source predicate len(members) < min_cluster is truthy) {
      // Source: vvaharness/scope/configs.py:205-205
      In source order: Evaluate keep.extend((r for r, _ in members)); retain side effects and discard the expression result.
      // Source: vvaharness/scope/configs.py:206-206
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/scope/configs.py:207-208
    In source order: Evaluate members.sort(key=lambda m: _rep_score(m[0], m[1])); retain side effects and discard the expression result. Then For reps, assign {}; source annotation dict[str, str].
    // Source: vvaharness/scope/configs.py:209-213
    if (the source predicate dd['keep_per_top_dir'] is truthy) {
      // Source: vvaharness/scope/configs.py:210-211
      for each (rel, _) in members {
        // Source: vvaharness/scope/configs.py:211-211
        In source order: Evaluate reps.setdefault(rel.split('/', 1)[0], rel); retain side effects and discard the expression result.
      }
    }
    else {
      // Source: vvaharness/scope/configs.py:213-213
      In source order: Evaluate once members[0][0]; assign in source target order to reps['*'].
    }
    // Source: vvaharness/scope/configs.py:214-215
    In source order: Evaluate once set(reps.values()); assign in source target order to rep_set. Then For rep_sus, assign set(); source annotation set[str].
    // Source: vvaharness/scope/configs.py:216-217
    for each r in rep_set {
      // Source: vvaharness/scope/configs.py:217-217
      In source order: Apply source augmented assignment rep_sus |= sus_by_rel.get(r, set()) with source evaluation/in-place semantics.
    }
    // Source: vvaharness/scope/configs.py:218-220
    In source order: Evaluate keep.extend(rep_set); retain side effects and discard the expression result. Then For c_dropped, assign []; source annotation list[str].
    // Source: vvaharness/scope/configs.py:221-235
    for each (rel, _) in members {
      // Source: vvaharness/scope/configs.py:222-223
      if (the source predicate rel in rep_set is truthy) {
        // Source: vvaharness/scope/configs.py:223-223
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/scope/configs.py:224-227
      if (the source predicate rel not in sus_by_rel is truthy) {
        // Source: vvaharness/scope/configs.py:226-226
        In source order: Evaluate keep.append(rel); retain side effects and discard the expression result.
        // Source: vvaharness/scope/configs.py:227-227
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/scope/configs.py:228-229
      In source order: Evaluate once sus_by_rel[rel]; assign in source target order to sus. Then Evaluate once sus - rep_sus; assign in source target order to extra.
      // Source: vvaharness/scope/configs.py:230-235
      if (the source predicate extra is truthy) {
        // Source: vvaharness/scope/configs.py:231-233
        In source order: Evaluate keep.append(rel); retain side effects and discard the expression result. Then Evaluate promoted.append((rel, _promotion_reason(sorted(extra)[0]))); retain side effects and discard the expression result. Then Apply source augmented assignment rep_sus |= sus with source evaluation/in-place semantics.
      }
      else {
        // Source: vvaharness/scope/configs.py:235-235
        In source order: Evaluate c_dropped.append(rel); retain side effects and discard the expression result.
      }
    }
    // Source: vvaharness/scope/configs.py:236-243
    In source order: Evaluate dropped.extend(c_dropped); retain side effects and discard the expression result. Then Evaluate cluster_report.append({'shape': h[:12], 'size': len(members), 'reps': sorted(rep_set), 'dropped': len(c_dropped), 'sample': members[0][0]}); retain side effects and discard the expression result.
  }
  // Source: vvaharness/scope/configs.py:245-257
  In source order: Evaluate cluster_report.sort(key=lambda c: -c['size']); retain side effects and discard the expression result. Then Evaluate once {'enabled': True, 'candidates': len(candidates), 'unparseable_kept': len(unclustered), 'clusters': len([c for c in cluster_report if c['size'] >= min_cluster]), 'kept_reps': sum((len(c['reps']) for c in cluster_report)), 'promoted': len(promoted), 'promoted_files': promoted[:50], 'dropped': len(dropped), 'dropped_files': dropped, 'top_clusters': cluster_report[:10]}; assign in source target order to report.
  // Source: vvaharness/scope/configs.py:259-270
  if (the source predicate dropped is truthy) {
    // Source: vvaharness/scope/configs.py:260-266
    In source order: Evaluate once ', '.join((source_template_260_24 for c in cluster_report[:3])); assign in source target order to top. Then Evaluate console.write(source_template_262_22); retain side effects and discard the expression result. Then Evaluate console.write(source_template_266_22); retain side effects and discard the expression result.
    // Source: vvaharness/scope/configs.py:267-270
    if (the source predicate promoted is truthy) {
      // Source: vvaharness/scope/configs.py:268-270
      In source order: Evaluate console.write(source_template_268_26 + (source_template_270_29 if len(promoted) > 5 else '')); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/scope/configs.py:271-271
  End this invocation with (sorted(keep), report).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.scope.walk import _DEDUP_DEFAULTS, _INSECURE_RX, _SECRET_RX` at source line 25: `source_detail/vvaharness/scope/walk.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 26: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 26: `source_detail/vvaharness/util/console.py.sudo.md`.
- `from vvaharness.util import console, logs` at source line 26: `source_detail/vvaharness/util/logs.py.sudo.md`.
