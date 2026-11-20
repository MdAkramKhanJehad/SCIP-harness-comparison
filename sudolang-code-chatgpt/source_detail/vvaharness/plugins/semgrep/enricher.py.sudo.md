# vvaharness/plugins/semgrep/enricher.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/plugins/semgrep/enricher.py.evidence.json`. SHA-256: `2977335357a95fa5757c827fefa7caa086e093dd2d3726d180836640df43300c`.

```sudo
// Source: vvaharness/plugins/semgrep/enricher.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import subprocess; preserve alias and import-time effects. Then Resolve source import import tempfile; preserve alias and import-time effects. Then Resolve source import import time; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/enricher.py:21-32
In source order: Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.identity import ProjectId, make_local_id; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import GraphEdge, GraphMutation, GraphNode, GraphSnapshot, freeze_properties; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.pipeline import PluginContext; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/enricher.py:33-38
In source order: Resolve source import from context_graph_sdk.plugins import PluginMetadata, PluginPhase; preserve alias and import-time effects. Then Resolve source import from vvaharness.plugins.semgrep.findings import read_semgrep_json, relative_path; preserve alias and import-time effects. Then Resolve source import from vvaharness.util import logs; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.events import Event; preserve alias and import-time effects.
// Source: vvaharness/plugins/semgrep/enricher.py:40-45
In source order: Evaluate once logs.get_logger(__name__); assign in source target order to log. Then Evaluate once 'SemgrepScan'; assign in source target order to SCAN_LABEL. Then Evaluate once 'SemgrepFinding'; assign in source target order to FINDING_LABEL. Then Evaluate once 'SemgrepRule'; assign in source target order to RULE_LABEL. Then Evaluate once 'SemgrepLocation'; assign in source target order to LOCATION_LABEL.
// Source: vvaharness/plugins/semgrep/enricher.py:47-52
In source order: Evaluate once 'FLAGGED_BY'; assign in source target order to FLAGGED_BY. Then Evaluate once 'DETECTED_BY'; assign in source target order to DETECTED_BY. Then Evaluate once 'TRACE_TOUCHES'; assign in source target order to TRACE_TOUCHES. Then Evaluate once 500; assign in source target order to MAX_FINDING_NODES. Then Evaluate once 20; assign in source target order to MAX_TRACE_STEPS.
// Source: vvaharness/plugins/semgrep/enricher.py:53-59
In source order: Evaluate once 18000; assign in source target order to MAX_EDGES. Then Evaluate once 15.0; assign in source target order to MIN_BUDGET_SECONDS. Then Evaluate once 6; assign in source target order to MAX_TRACE_NESTING. Then Evaluate once (('taint_source', 'source'), ('intermediate_vars', 'intermediate'), ('taint_sink', 'sink')); assign in source target order to _TRACE_ROLES. Then Evaluate once 1000; assign in source target order to _MAX_MESSAGE_CHARS.
// Source: vvaharness/plugins/semgrep/enricher.py:60-60
In source order: Evaluate once {'ERROR': 0, 'WARNING': 1, 'INFO': 2}; assign in source target order to _SEVERITY_ORDER.
// Source: vvaharness/plugins/semgrep/enricher.py:64-68
// Source: vvaharness/plugins/semgrep/enricher.py:63-63
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/plugins/semgrep/enricher.py:64-68
interface _Located {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/enricher.py:65-68
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call. Then For path, declare without assigning a value; source annotation str. Then For line, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/plugins/semgrep/enricher.py:72-84
// Source: vvaharness/plugins/semgrep/enricher.py:71-71
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/plugins/semgrep/enricher.py:72-84
interface _Symbols {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/enricher.py:73-76
  In source order: Retain source documentation literal source_literal_73_4; it is not a model call. Then For spans, declare without assigning a value; source annotation dict[str, tuple[tuple[int, int, str], ...]]. Then For files, declare without assigning a value; source annotation dict[str, str].
  // Source: vvaharness/plugins/semgrep/enricher.py:78-84
  // Source signature: resolve(self, at: _Located) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn resolve(self, at) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:79-80
    In source order: Retain source documentation literal source_literal_79_8; it is not a model call. Then For best, assign None; source annotation tuple[int, str] | None.
    // Source: vvaharness/plugins/semgrep/enricher.py:81-83
    for each (start, end, node_id) in self.spans.get(at.path, ()) {
      // Source: vvaharness/plugins/semgrep/enricher.py:82-83
      if (the source predicate start <= at.line <= end and (best is None or end - start < best[0]) is truthy) {
        // Source: vvaharness/plugins/semgrep/enricher.py:83-83
        In source order: Evaluate once (end - start, node_id); assign in source target order to best.
      }
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:84-84
    End this invocation with best[1] if best is not None else self.files.get(at.path).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/plugins/semgrep/enricher.py:87-101
// Source signature: _index(graph: GraphSnapshot) -> _Symbols
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _index(graph) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:88-90
  In source order: Retain source documentation literal source_literal_88_4; it is not a model call. Then For spans, assign {}; source annotation dict[str, list[tuple[int, int, str]]]. Then For files, assign {}; source annotation dict[str, str].
  // Source: vvaharness/plugins/semgrep/enricher.py:91-100
  for each node in graph.nodes {
    // Source: vvaharness/plugins/semgrep/enricher.py:92-93
    In source order: Evaluate once node.properties.to_dict(); assign in source target order to props. Then Evaluate once props.get('filePath'); assign in source target order to path.
    // Source: vvaharness/plugins/semgrep/enricher.py:94-95
    if (the source predicate not isinstance(path, str) is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:95-95
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:96-97
    if (the source predicate 'File' in node.labels is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:97-97
      In source order: Evaluate files.setdefault(path, node.id); retain side effects and discard the expression result.
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:98-98
    In source order: Evaluate once (props.get('startLine'), props.get('endLine')); assign in source target order to (start, end).
    // Source: vvaharness/plugins/semgrep/enricher.py:99-100
    if (the source predicate isinstance(start, int) and isinstance(end, int) and (end >= start) is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:100-100
      In source order: Evaluate spans.setdefault(path, []).append((start, end, node.id)); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:101-101
  End this invocation with _Symbols({path: tuple(sorted(rows)) for path, rows in spans.items()}, files).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:104-113
// Source signature: _argv(executable: str, configs: tuple[Path, ...], rulesets: tuple[str, ...], root: str, output: Path) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _argv(executable, configs, rulesets, root, output) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:106-108
  In source order: Retain source documentation literal source_literal_106_4; it is not a model call. Then Evaluate once [executable, '--json', '--quiet', '--metrics=off', '--disable-version-check', '--output', str(output)]; assign in source target order to argv.
  // Source: vvaharness/plugins/semgrep/enricher.py:109-110
  for each config in configs {
    // Source: vvaharness/plugins/semgrep/enricher.py:110-110
    In source order: Apply source augmented assignment argv += ['--config', str(config)] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:111-112
  for each ruleset in rulesets {
    // Source: vvaharness/plugins/semgrep/enricher.py:112-112
    In source order: Apply source augmented assignment argv += ['--config', ruleset] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:113-113
  End this invocation with [*argv, root].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:116-120
// Source signature: _cwe_ids(metadata: dict) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cwe_ids(metadata) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:117-119
  In source order: Retain source documentation literal source_literal_117_4; it is not a model call. Then Evaluate once metadata.get('cwe') or []; assign in source target order to raw. Then Evaluate once [raw] if isinstance(raw, str) else [v for v in raw if isinstance(v, str)]; assign in source target order to values.
  // Source: vvaharness/plugins/semgrep/enricher.py:120-120
  End this invocation with tuple(dict.fromkeys((v.split(':')[0].strip() for v in values if v.strip()))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:123-130
// Source signature: _classes(metadata: dict) -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _classes(metadata) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:124-125
  In source order: Retain source documentation literal source_literal_124_4; it is not a model call. Then For out, assign []; source annotation list[str].
  // Source: vvaharness/plugins/semgrep/enricher.py:126-129
  for each key in ('vulnerability_class', 'owasp', 'category') {
    // Source: vvaharness/plugins/semgrep/enricher.py:127-129
    In source order: Evaluate once metadata.get(key) or []; assign in source target order to raw. Then Evaluate once [raw] if isinstance(raw, str) else [v for v in raw if isinstance(v, str)]; assign in source target order to values. Then Apply source augmented assignment out += [v.strip() for v in values if v.strip()] with source evaluation/in-place semantics.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:130-130
  End this invocation with tuple(dict.fromkeys(out)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:133-144
// Source signature: _trace_steps(extra: dict, root: str) -> tuple[tuple[str, _Located], ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _trace_steps(extra, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:134-135
  In source order: Retain source documentation literal source_literal_134_4; it is not a model call. Then Evaluate once extra.get('dataflow_trace') or {}; assign in source target order to trace.
  // Source: vvaharness/plugins/semgrep/enricher.py:136-137
  if (the source predicate not isinstance(trace, dict) is truthy) {
    // Source: vvaharness/plugins/semgrep/enricher.py:137-137
    End this invocation with ().
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:138-138
  In source order: For steps, assign []; source annotation list[tuple[str, _Located]].
  // Source: vvaharness/plugins/semgrep/enricher.py:139-143
  for each (key, role) in _TRACE_ROLES {
    // Source: vvaharness/plugins/semgrep/enricher.py:140-143
    for each entry in _flatten(trace.get(key)) {
      // Source: vvaharness/plugins/semgrep/enricher.py:141-141
      In source order: Evaluate once _location(entry, root); assign in source target order to located.
      // Source: vvaharness/plugins/semgrep/enricher.py:142-143
      if (the source predicate located is not None is truthy) {
        // Source: vvaharness/plugins/semgrep/enricher.py:143-143
        In source order: Evaluate steps.append((role, located)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:144-144
  End this invocation with tuple(steps[:MAX_TRACE_STEPS]).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:147-153
// Source signature: _flatten(value: object, depth: int=0) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _flatten(value, depth) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:148-148
  In source order: Retain source documentation literal source_literal_148_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/enricher.py:149-150
  if (the source predicate isinstance(value, dict) is truthy) {
    // Source: vvaharness/plugins/semgrep/enricher.py:150-150
    End this invocation with [value].
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:151-152
  if (the source predicate isinstance(value, (list, tuple)) and depth < MAX_TRACE_NESTING is truthy) {
    // Source: vvaharness/plugins/semgrep/enricher.py:152-152
    End this invocation with [found for item in value for found in _flatten(item, depth + 1)].
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:153-153
  End this invocation with [].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:156-162
// Source signature: _location(entry: dict, root: str) -> _Located | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _location(entry, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:157-159
  In source order: Retain source documentation literal source_literal_157_4; it is not a model call. Then Evaluate once entry.get('path'); assign in source target order to path. Then Evaluate once (entry.get('start') or {}).get('line') if isinstance(entry.get('start'), dict) else None; assign in source target order to line.
  // Source: vvaharness/plugins/semgrep/enricher.py:160-161
  if (the source predicate isinstance(path, str) and isinstance(line, int) is truthy) {
    // Source: vvaharness/plugins/semgrep/enricher.py:161-161
    End this invocation with _Located(relative_path(path, root), line).
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:162-162
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:165-173
// Source signature: _ranked(results: list[dict]) -> list[dict]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ranked(results) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:166-166
  In source order: Retain source documentation literal source_literal_166_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/enricher.py:167-172
  // Source signature: key(result: dict) -> tuple[int, str, int, str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn key(result) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:168-169
    In source order: Evaluate once result.get('extra') or {}; assign in source target order to extra. Then Evaluate once str(extra.get('severity', '')).upper(); assign in source target order to severity.
    // Source: vvaharness/plugins/semgrep/enricher.py:170-172
    End this invocation with (_SEVERITY_ORDER.get(severity, 3), str(result.get('path') or ''), int((result.get('start') or {}).get('line') or 0), str(result.get('check_id') or '')).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:173-173
  End this invocation with sorted((r for r in results if isinstance(r, dict)), key=key)[:MAX_FINDING_NODES].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:177-185
// Source: vvaharness/plugins/semgrep/enricher.py:176-176
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/plugins/semgrep/enricher.py:177-185
interface _Coverage {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/enricher.py:178-183
  In source order: Retain source documentation literal source_literal_178_4; it is not a model call. Then For note, declare without assigning a value; source annotation str. Then For complete, assign False; source annotation bool. Then For findings, assign 0; source annotation int. Then For errors, assign 0; source annotation int.
  // Source: vvaharness/plugins/semgrep/enricher.py:184-185
  In source order: For skipped, assign 0; source annotation int. Then For rules, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/plugins/semgrep/enricher.py:188-200
// Source signature: _scan_node(project_id: ProjectId, coverage: _Coverage) -> GraphNode
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _scan_node(project_id, coverage) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:189-189
  In source order: Retain source documentation literal source_literal_189_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/enricher.py:190-200
  End this invocation with GraphNode(project_id=project_id, local_id=make_local_id('semgrep-scan', project_id.value), labels=(SCAN_LABEL,), properties=freeze_properties({'complete': coverage.complete, 'findingCount': coverage.findings, 'errorCount': coverage.errors, 'skippedCount': coverage.skipped, 'ruleCount': coverage.rules, 'note': coverage.note[:_MAX_MESSAGE_CHARS], 'tool': 'semgrep'})).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:203-241
interface _Builder {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/enricher.py:204-204
  In source order: Retain source documentation literal source_literal_204_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/enricher.py:206-209
  // Source signature: __init__(self, project_id: ProjectId) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __init__(self, project_id) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:207-209
    In source order: Evaluate once project_id; assign in source target order to self.project_id. Then For self.nodes, assign {}; source annotation dict[str, GraphNode]. Then For self.edges, assign {}; source annotation dict[str, GraphEdge].
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:211-216
  // Source signature: node(self, local_id: str, labels: tuple[str, ...], properties: dict) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn node(self, local_id, labels, properties) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:212-215
    In source order: Retain source documentation literal source_literal_212_8; it is not a model call. Then Evaluate once GraphNode(project_id=self.project_id, local_id=local_id, labels=labels, properties=freeze_properties(properties)); assign in source target order to node. Then Evaluate self.nodes.setdefault(node.id, node); retain side effects and discard the expression result.
    // Source: vvaharness/plugins/semgrep/enricher.py:216-216
    End this invocation with node.id.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:218-228
  // Source signature: edge(self, source: str, relationship: str, target: str, *, discriminator: str='', properties: dict | None=None) -> bool
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn edge(self, source, relationship, target, discriminator, properties) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:220-220
    In source order: Retain source documentation literal source_literal_220_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/enricher.py:221-222
    if (the source predicate len(self.edges) >= MAX_EDGES is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:222-222
      End this invocation with False.
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:223-227
    In source order: Evaluate once GraphEdge(project_id=self.project_id, source_id=source, relationship_type=relationship, target_id=target, discriminator=discriminator, properties=freeze_properties(properties or {})); assign in source target order to edge. Then Evaluate self.edges.setdefault(edge.id, edge); retain side effects and discard the expression result.
    // Source: vvaharness/plugins/semgrep/enricher.py:228-228
    End this invocation with True.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:230-236
  // Source signature: anchor(self, symbols: _Symbols, at: _Located) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn anchor(self, symbols, at) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:231-232
    In source order: Retain source documentation literal source_literal_231_8; it is not a model call. Then Evaluate once symbols.resolve(at); assign in source target order to resolved.
    // Source: vvaharness/plugins/semgrep/enricher.py:233-234
    if (the source predicate resolved is not None is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:234-234
      End this invocation with resolved.
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:235-236
    End this invocation with self.node(make_local_id('semgrep-location', at.path), (LOCATION_LABEL,), {'name': at.path, 'filePath': at.path}).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:238-241
  // Source signature: mutation(self) -> GraphMutation
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn mutation(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:239-239
    In source order: Retain source documentation literal source_literal_239_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/enricher.py:240-241
    End this invocation with GraphMutation(project_id=self.project_id, nodes=tuple(self.nodes.values()), edges=tuple(self.edges.values())).
    If execution reaches this end, finish with the source implicit None result.
  }
}
// Source: vvaharness/plugins/semgrep/enricher.py:244-249
// Source signature: _rule_id(builder: _Builder, check_id: str, metadata: dict) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rule_id(builder, check_id, metadata) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:245-245
  In source order: Retain source documentation literal source_literal_245_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/enricher.py:246-249
  End this invocation with builder.node(make_local_id('semgrep-rule', check_id), (RULE_LABEL,), {'name': check_id, 'ruleId': check_id, 'cweIds': list(_cwe_ids(metadata)), 'vulnerabilityClasses': list(_classes(metadata))}).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:252-280
// Source signature: _add_finding(builder: _Builder, symbols: _Symbols, result: dict, ordinal: int, root: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _add_finding(builder, symbols, result, ordinal, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:254-256
  In source order: Retain source documentation literal source_literal_254_4; it is not a model call. Then Evaluate once result.get('path'); assign in source target order to raw_path. Then Evaluate once (result.get('start') or {}).get('line'); assign in source target order to line.
  // Source: vvaharness/plugins/semgrep/enricher.py:257-258
  if (the source predicate not isinstance(raw_path, str) or not isinstance(line, int) is truthy) {
    // Source: vvaharness/plugins/semgrep/enricher.py:258-258
    End this invocation with False.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:259-263
  In source order: Evaluate once relative_path(raw_path, root); assign in source target order to path. Then Evaluate once result.get('extra') or {}; assign in source target order to extra. Then Evaluate once extra.get('metadata') or {}; assign in source target order to metadata. Then Evaluate once str(result.get('check_id') or 'semgrep'); assign in source target order to check_id. Then Evaluate once (result.get('end') or {}).get('line'); assign in source target order to end_line.
  // Source: vvaharness/plugins/semgrep/enricher.py:264-273
  In source order: Evaluate once builder.node(make_local_id('semgrep-finding', check_id, path, str(line), str(ordinal)), (FINDING_LABEL,), {'name': check_id, 'ruleId': check_id, 'filePath': path, 'semgrepStartLine': line, 'semgrepEndLine': end_line if isinstance(end_line, int) else line, 'severity': str(extra.get('severity') or '').upper() or 'UNKNOWN', 'message': str(extra.get('message') or check_id)[:_MAX_MESSAGE_CHARS], 'fingerprint': str(extra.get('fingerprint') or '')}); assign in source target order to finding. Then Evaluate builder.edge(builder.anchor(symbols, _Located(path, line)), FLAGGED_BY, finding); retain side effects and discard the expression result. Then Evaluate builder.edge(finding, DETECTED_BY, _rule_id(builder, check_id, metadata)); retain side effects and discard the expression result.
  // Source: vvaharness/plugins/semgrep/enricher.py:274-279
  for each (step, (role, located)) in enumerate(_trace_steps(extra, root)) {
    // Source: vvaharness/plugins/semgrep/enricher.py:275-275
    In source order: Evaluate once symbols.resolve(located); assign in source target order to target.
    // Source: vvaharness/plugins/semgrep/enricher.py:276-279
    if (the source predicate target is not None and target != finding is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:277-279
      In source order: Evaluate builder.edge(finding, TRACE_TOUCHES, target, discriminator=str(step), properties={'step': step, 'role': role, 'filePath': located.path, 'startLine': located.line}); retain side effects and discard the expression result.
    }
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:280-280
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:283-302
// Source signature: _mutation(project_id: ProjectId, graph: GraphSnapshot, document: dict, root: str='') -> GraphMutation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _mutation(project_id, graph, document, root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:285-289
  In source order: Retain source documentation literal source_literal_285_4; it is not a model call. Then Evaluate once document.get('results'); assign in source target order to raw. Then Evaluate once _ranked(raw if isinstance(raw, list) else []); assign in source target order to results. Then Evaluate once _Builder(project_id); assign in source target order to builder. Then Evaluate once _index(graph); assign in source target order to symbols.
  // Source: vvaharness/plugins/semgrep/enricher.py:290-294
  In source order: Evaluate once sum((_add_finding(builder, symbols, r, i, root) for i, r in enumerate(results))); assign in source target order to written. Then Evaluate once document.get('errors'); assign in source target order to errors. Then Evaluate once (document.get('paths') or {}).get('skipped'); assign in source target order to skipped. Then Evaluate once len(errors) if isinstance(errors, list) else 0; assign in source target order to error_count. Then Evaluate once len(raw) - len(results) if isinstance(raw, list) else 0; assign in source target order to dropped.
  // Source: vvaharness/plugins/semgrep/enricher.py:295-301
  In source order: Evaluate once _scan_node(project_id, _Coverage(note=source_template_296_13 if dropped else 'ok', complete=not dropped and (not error_count), findings=written, errors=error_count, skipped=len(skipped) if isinstance(skipped, list) else 0, rules=sum((1 for n in builder.nodes.values() if RULE_LABEL in n.labels)))); assign in source target order to scan. Then Evaluate builder.nodes.setdefault(scan.id, scan); retain side effects and discard the expression result.
  // Source: vvaharness/plugins/semgrep/enricher.py:302-302
  End this invocation with builder.mutation().
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:306-367
// Source: vvaharness/plugins/semgrep/enricher.py:305-305
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/plugins/semgrep/enricher.py:306-367
interface SemgrepEnricher {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/plugins/semgrep/enricher.py:307-312
  In source order: Retain source documentation literal source_literal_307_4; it is not a model call. Then For configs, assign (); source annotation tuple[Path, ...]. Then For rulesets, assign (); source annotation tuple[str, ...]. Then For executable, assign 'semgrep'; source annotation str. Then For timeout_seconds, assign 120.0; source annotation float.
  // Source: vvaharness/plugins/semgrep/enricher.py:313-313
  In source order: For priority, assign 100; source annotation int.
  // Source: vvaharness/plugins/semgrep/enricher.py:316-319
  // Source: vvaharness/plugins/semgrep/enricher.py:315-315
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vvaharness/plugins/semgrep/enricher.py:316-319
  // Source signature: metadata(self) -> PluginMetadata
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn metadata(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:317-317
    In source order: Retain source documentation literal source_literal_317_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/enricher.py:318-319
    End this invocation with PluginMetadata(phase=PluginPhase.POST_DERIVATION, priority=self.priority, name='semgrep', version='1').
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/plugins/semgrep/enricher.py:321-332
  // Source signature: enrich(self, context: PluginContext) -> GraphMutation
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn enrich(self, context) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:322-325
    In source order: Retain source documentation literal source_literal_322_8; it is not a model call. Then Evaluate once context.project.project_id; assign in source target order to project_id. Then Evaluate once min(self.timeout_seconds, context.deadline_monotonic - time.monotonic()); assign in source target order to budget. Then Evaluate once self._refusal(context, budget); assign in source target order to refusal.
    // Source: vvaharness/plugins/semgrep/enricher.py:326-327
    if (the source predicate refusal is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:327-327
      End this invocation with self._degrade(project_id, refusal).
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:328-329
    In source order: Evaluate once str(context.project.source_path); assign in source target order to root. Then Evaluate once self._report(root, budget); assign in source target order to (document, note).
    // Source: vvaharness/plugins/semgrep/enricher.py:330-331
    if (the source predicate document is None is truthy) {
      // Source: vvaharness/plugins/semgrep/enricher.py:331-331
      End this invocation with self._degrade(project_id, note).
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:332-332
    End this invocation with _mutation(project_id, context.graph, document, root).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:334-340
  // Source signature: _degrade(self, project_id: ProjectId, note: str) -> GraphMutation
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _degrade(self, project_id, note) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:335-339
    In source order: Retain source documentation literal source_literal_335_8; it is not a model call. Then Evaluate COUNTERS.bump('semgrep_scan_degraded'); retain side effects and discard the expression result. Then Evaluate log.warning(Event.SEMGREP_SCAN_DEGRADED, reason=note, executable=self.executable, remedy=source_literal_338_27); retain side effects and discard the expression result.
    // Source: vvaharness/plugins/semgrep/enricher.py:340-340
    End this invocation with _degraded(project_id, note).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:342-352
  // Source signature: _refusal(self, context: PluginContext, budget: float) -> str
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _refusal(self, context, budget) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:343-351
    In source order: Retain source documentation literal source_literal_343_8; it is not a model call. Then Evaluate once ((context.cancellation.is_cancelled, 'cancelled before the Semgrep scan started'), (not context.project.source_path, 'the project carries no source path to scan'), (not self.configs and (not self.rulesets), 'no local rule files and no rulesets were configured'), (budget < MIN_BUDGET_SECONDS, source_template_350_13)); assign in source target order to checks.
    // Source: vvaharness/plugins/semgrep/enricher.py:352-352
    End this invocation with next((reason for failed, reason in checks if failed), '').
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/plugins/semgrep/enricher.py:354-367
  // Source signature: _report(self, root: str, budget: float) -> tuple[dict | None, str]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _report(self, root, budget) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/plugins/semgrep/enricher.py:355-355
    In source order: Retain source documentation literal source_literal_355_8; it is not a model call.
    // Source: vvaharness/plugins/semgrep/enricher.py:356-367
    Perform the following protected operations {
      // Source: vvaharness/plugins/semgrep/enricher.py:357-365
      Enter source context managers left-to-right: tempfile.TemporaryDirectory(prefix='vvah-semgrep-') bound to work {
        // Source: vvaharness/plugins/semgrep/enricher.py:358-361
        In source order: Evaluate once Path(work) / 'semgrep.json'; assign in source target order to output. Then Evaluate once _argv(self.executable, self.configs, self.rulesets, root, output); assign in source target order to argv. Then Evaluate once subprocess.run(argv, capture_output=True, text=True, check=False, timeout=budget, cwd=root); assign in source target order to done.
        // Source: vvaharness/plugins/semgrep/enricher.py:362-364
        if (the source predicate not output.is_file() is truthy) {
          // Source: vvaharness/plugins/semgrep/enricher.py:363-363
          In source order: Evaluate once (done.stderr or done.stdout or '').strip()[:_MAX_MESSAGE_CHARS]; assign in source target order to detail.
          // Source: vvaharness/plugins/semgrep/enricher.py:364-364
          End this invocation with (None, source_template_364_33).
        }
        // Source: vvaharness/plugins/semgrep/enricher.py:365-365
        End this invocation with (read_semgrep_json(output), '').
      }
      Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
    }
    // Source: vvaharness/plugins/semgrep/enricher.py:366-367
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/plugins/semgrep/enricher.py:367-367
      End this invocation with (None, source_template_367_25[:_MAX_MESSAGE_CHARS]).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/plugins/semgrep/enricher.py:370-374
// Source signature: _degraded(project_id: ProjectId, note: str) -> GraphMutation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _degraded(project_id, note) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/plugins/semgrep/enricher.py:371-371
  In source order: Retain source documentation literal source_literal_371_4; it is not a model call.
  // Source: vvaharness/plugins/semgrep/enricher.py:372-374
  End this invocation with GraphMutation(project_id=project_id, nodes=(_scan_node(project_id, _Coverage(note=note)),)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/plugins/semgrep/enricher.py:377-389
In source order: Evaluate once ['DETECTED_BY', 'FINDING_LABEL', 'FLAGGED_BY', 'LOCATION_LABEL', 'MAX_EDGES', 'MAX_FINDING_NODES', 'MAX_TRACE_STEPS', 'RULE_LABEL', 'SCAN_LABEL', 'TRACE_TOUCHES', 'SemgrepEnricher']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk.identity import ProjectId, make_local_id` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.
- `from context_graph_sdk.models import GraphEdge, GraphMutation, GraphNode, GraphSnapshot, freeze_properties` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.pipeline import PluginContext` at source line 32: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/pipeline/__init__.py.sudo.md`.
- `from context_graph_sdk.plugins import PluginMetadata, PluginPhase` at source line 33: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/plugins/__init__.py.sudo.md`.
- `from vvaharness.plugins.semgrep.findings import read_semgrep_json, relative_path` at source line 35: `source_detail/vvaharness/plugins/semgrep/findings.py.sudo.md`.
- `from vvaharness.util import logs` at source line 36: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import logs` at source line 36: `source_detail/vvaharness/util/logs.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 37: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from vvaharness.util.events import Event` at source line 38: `source_detail/vvaharness/util/events.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/plugins/semgrep/enricher.py.sudo.md). Exact strings in the evidence asset support this conversion.
