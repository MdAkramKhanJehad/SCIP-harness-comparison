# vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py.evidence.json`. SHA-256: `026219f8b32bca599dd72639ec895c73d026048236d97fa7b9eb9a67931a3837`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.graph.symbols import is_test_file; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:24-47
In source order: Evaluate once 3; assign in source target order to ORCHESTRATOR_MAX_CALLERS. Then Evaluate once 4; assign in source target order to ORCHESTRATOR_MIN_CALLEES. Then Evaluate once frozenset({'main', 'init', 'bootstrap', 'start', 'run', 'setup', 'configure'}); assign in source target order to _UNIVERSAL_ENTRY. Then Evaluate once tuple((re.compile(pattern, re.IGNORECASE) for pattern in ('^handle', '^on[A-Z]', 'Controller$', 'Handler$', '^process[A-Z]', '^execute', '^perform', '^dispatch', '^trigger', '^fire', '^emit'))); assign in source target order to _ENTRY_PREFIXES. Then Evaluate once (*(re.compile(pattern, re.IGNORECASE) for pattern in ('^get[A-Z]', '^set[A-Z]', '^is[A-Z]', '^has[A-Z]', '^can[A-Z]', '^format', '^parse', '^validate', '^toString', '^fromJSON', '^from[A-Z]', '^encode', '^decode', '^serialize', '^clone', '^merge')), re.compile('^_')); assign in source target order to _UTILITY_PATTERNS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:49-135
In source order: For _LANGUAGE_PATTERNS, assign {'typescript': (re.compile('^use[A-Z]'),), 'javascript': (re.compile('^use[A-Z]'),), 'python': tuple((re.compile(p) for p in ('^get_', '^post_', '^put_', '^delete_', '^patch_'))), 'java': (re.compile('^do(Get|Post|Put|Delete)'), re.compile('^service$')), 'go': tuple((re.compile(p) for p in ('^New[A-Z]', '^Handle', '^Serve'))), 'rust': tuple((re.compile(p) for p in ('^handle_', '^process_', '^serve'))), 'swift': tuple((re.compile(p) for p in ('^viewDidLoad$', '^viewWillAppear$', '^body$', '^applicationDidFinishLaunching'))), 'php': tuple((re.compile(p) for p in ('^handle$', '^index$', '^store$', '^show$', '^update$', '^destroy$'))), 'csharp': tuple((re.compile(p) for p in ('^(Get|Post|Put|Delete|Patch)[A-Z]', '^On[A-Z]', '^Configure'))), 'c': tuple((re.compile(p) for p in ('_init$', '^init_', '_start$', '^start_', '_handler$', '^handle_', '_callback$', '^cmd_', '^server_', '^client_', '^session_', '^window_', '^signal_', '^event_'))), 'cpp': tuple((re.compile(p) for p in ('^(Create|create)[A-Z_]', '^(Run|run)$', '^(Start|start)$', '^On[A-Z]', '^on_'))), 'scala': tuple((re.compile(p) for p in ('^apply$', '^receive$', '^props$', '^routes?$')))}; source annotation dict[str, tuple[re.Pattern[str], ...]]. Then Evaluate once tuple(((re.compile(pattern, re.IGNORECASE), reason) for pattern, reason in (('(^|/)pages/', 'framework:nextjs-page'), ('(^|/)app/.*route\\.(ts|js)x?$', 'framework:nextjs-app-router'), ('(^|/)routes/', 'framework:route-handler'), ('(^|/)controllers/', 'framework:controller'), ('(^|/)handlers/', 'framework:handler'), ('(^|/)api/', 'framework:api-handler'), ('(^|/)middleware/', 'framework:middleware')))); assign in source target order to _FRAMEWORK_PATTERNS. Then For _LABEL_RULES, assign (('Initialization', ('init', 'bootstrap', 'setup')), ('Shutdown', ('shutdown', 'cleanup', 'teardown', 'dispose', 'close')), ('Test flow', ('test', 'bench')), ('Server', ('serve', 'listen', 'accept')), ('Request handler', ('handle', 'handler', 'endpoint', 'middleware')), ('Router', ('route', 'dispatch')), ('Create operation', ('create', 'insert', 'add', 'new')), ('Update operation', ('update', 'modify', 'patch', 'set')), ('Delete operation', ('delete', 'remove', 'destroy', 'drop')), ('Read operation', ('get', 'fetch', 'load', 'read', 'find', 'lookup', 'query')), ('List operation', ('list', 'scan', 'iterate', 'enum')), ('Processing', ('process', 'execute', 'run', 'eval')), ('Parser', ('parse', 'decode', 'unmarshal', 'deserialize')), ('Serializer', ('format', 'encode', 'marshal', 'serialize', 'render')), ('Transformer', ('convert', 'transform', 'map')), ('Copy operation', ('copy', 'clone', 'dup')), ('Merge operation', ('merge', 'combine', 'join')), ('Validation', ('valid', 'check', 'verify')), ('Authentication', ('auth', 'login', 'permit', 'acl')), ('Synchronization', ('sync', 'reconcil', 'replicat')), ('Scheduler', ('schedule', 'plan', 'allocat')), ('Watcher', ('watch', 'monitor', 'poll', 'subscribe')), ('Event emitter', ('emit', 'publish', 'notify', 'broadcast', 'event')), ('Observability', ('log', 'metric', 'trace', 'audit')), ('Registration', ('register', 'bind', 'wire', 'connect')), ('Configuration', ('config', 'option', 'setting')), ('Migration', ('migrat', 'upgrade', 'schema')), ('Lifecycle', ('start', 'stop', 'restart'))); source annotation tuple[tuple[str, tuple[str, ...]], ...].
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:138-145
// Source signature: heuristic_label(name: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn heuristic_label(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:139-139
  In source order: Evaluate once name.lower(); assign in source target order to lower.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:140-141
  if (the source predicate lower == 'main' or lower.endswith('.main') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:141-141
    End this invocation with 'Application entry point'.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:142-144
  for each (label, patterns) in _LABEL_RULES {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:143-144
    if (the source predicate any((pattern in lower for pattern in patterns)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:144-144
      End this invocation with label.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:145-145
  End this invocation with 'Execution flow'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:149-151
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:148-148
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:149-151
interface EntryPointScore {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:150-151
  In source order: For score, declare without assigning a value; source annotation float. Then For reasons, declare without assigning a value; source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:154-159
// Source signature: detect_framework(file_path: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_framework(file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:155-155
  In source order: Evaluate once file_path.replace('\\', '/'); assign in source target order to normalized.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:156-158
  for each (pattern, reason) in _FRAMEWORK_PATTERNS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:157-158
    if (the source predicate pattern.search(normalized) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:158-158
      End this invocation with reason.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:159-159
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:162-174
// Source signature: _name_multiplier(name: str, language: str) -> tuple[float, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _name_multiplier(name, language) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:163-164
  if (the source predicate name.lower() in _UNIVERSAL_ENTRY is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:164-164
    End this invocation with (1.5, 'entry-pattern').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:165-167
  for each pattern in _ENTRY_PREFIXES {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:166-167
    if (the source predicate pattern.search(name) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:167-167
      End this invocation with (1.5, 'entry-pattern').
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:168-170
  for each pattern in _LANGUAGE_PATTERNS.get(language, ()) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:169-170
    if (the source predicate pattern.search(name) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:170-170
      End this invocation with (1.5, 'entry-pattern').
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:171-173
  for each pattern in _UTILITY_PATTERNS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:172-173
    if (the source predicate pattern.search(name) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:173-173
      End this invocation with (0.3, 'utility-pattern').
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:174-174
  End this invocation with (1.0, '').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:177-202
// Source signature: entry_point_score(name: str, language: str, is_exported: bool, caller_count: int, callee_count: int, file_path: str='') -> EntryPointScore
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn entry_point_score(name, language, is_exported, caller_count, callee_count, file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:185-186
  if (the source predicate callee_count == 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:186-186
    End this invocation with EntryPointScore(0.0, ('no-outgoing-calls',)).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:187-189
  In source order: For reasons, assign []; source annotation list[str]. Then Evaluate once callee_count / (caller_count + 1); assign in source target order to base. Then Evaluate once 1.0; assign in source target order to multiplier.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:190-192
  if (the source predicate is_exported is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:191-192
    In source order: Apply source augmented assignment multiplier *= 2.0 with source evaluation/in-place semantics. Then Evaluate reasons.append('exported'); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:193-194
  In source order: Evaluate once _name_multiplier(name, language); assign in source target order to (name_multiplier, name_reason). Then Apply source augmented assignment multiplier *= name_multiplier with source evaluation/in-place semantics.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:195-196
  if (the source predicate name_reason is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:196-196
    In source order: Evaluate reasons.append(name_reason); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:197-201
  if (the source predicate file_path is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:198-198
    In source order: Evaluate once detect_framework(file_path); assign in source target order to framework.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:199-201
    if (the source predicate framework is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:200-201
      In source order: Apply source augmented assignment multiplier *= 1.5 with source evaluation/in-place semantics. Then Evaluate reasons.append(framework); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:202-202
  End this invocation with EntryPointScore(base * multiplier, tuple(reasons)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:205-211
// Source signature: is_command_dir(file_path: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_command_dir(file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:206-207
  if (the source predicate not file_path is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:207-207
    End this invocation with False.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:208-211
  End this invocation with any((part.lower() in ('cmd', 'command', 'commands', 'cli') for part in file_path.replace('\\', '/').split('/'))).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py:214-223
In source order: Evaluate once ['ORCHESTRATOR_MAX_CALLERS', 'ORCHESTRATOR_MIN_CALLEES', 'EntryPointScore', 'detect_framework', 'entry_point_score', 'heuristic_label', 'is_command_dir', 'is_test_file']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk.graph.symbols import is_test_file` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/graph/symbols.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/analysis/entry_points.py.sudo.md). Exact strings in the evidence asset support this conversion.
