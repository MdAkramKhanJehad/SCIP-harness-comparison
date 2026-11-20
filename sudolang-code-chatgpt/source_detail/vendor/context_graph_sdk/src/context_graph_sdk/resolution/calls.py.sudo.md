# vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py.evidence.json`. SHA-256: `2d2d7c59374822b16bca83c97cc0559ef1232f529dfada64518cfd78053451b5`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import CALLABLE_LABELS, Symbol; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:23-28
In source order: Resolve source import from context_graph_sdk.models import LocalRelationshipType; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult, file_local_id; preserve alias and import-time effects. Then Evaluate once 0.8; assign in source target order to CALL_CONFIDENCE. Then Evaluate once 0.9; assign in source target order to SPAWN_CONFIDENCE. Then Evaluate once 0.7; assign in source target order to DELEGATE_CONFIDENCE.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:29-71
In source order: Evaluate once 'tree-sitter call extraction'; assign in source target order to CALL_REASON. Then Evaluate once frozenset({'log', 'warn', 'error', 'info', 'debug', 'setTimeout', 'setInterval', 'clearTimeout', 'clearInterval', 'parseInt', 'parseFloat', 'isNaN', 'isFinite', 'parse', 'stringify', 'resolve', 'reject', 'then', 'catch', 'finally', 'require', 'map', 'filter', 'reduce', 'forEach', 'find', 'findIndex', 'some', 'every', 'includes', 'indexOf', 'slice', 'splice', 'concat', 'join', 'split', 'push', 'pop', 'shift', 'unshift', 'sort', 'reverse', 'keys', 'values', 'entries', 'assign', 'freeze', 'hasOwnProperty', 'toString', 'useState', 'useEffect', 'useCallback', 'useMemo', 'useRef', 'useContext', 'useReducer', 'createElement', 'createContext', 'forwardRef', 'memo', 'print', 'len', 'range', 'str', 'int', 'float', 'list', 'dict', 'set', 'tuple', 'open', 'read', 'write', 'close', 'append', 'extend', 'update', 'super', 'type', 'isinstance', 'issubclass', 'getattr', 'setattr', 'hasattr', 'enumerate', 'zip', 'sorted', 'reversed', 'min', 'max', 'sum', 'abs', 'printf', 'fprintf', 'sprintf', 'snprintf', 'scanf', 'fscanf', 'sscanf', 'malloc', 'calloc', 'realloc', 'free', 'memcpy', 'memmove', 'memset', 'memcmp', 'strlen', 'strcpy', 'strncpy', 'strcat', 'strcmp', 'sizeof', 'assert', 'abort', 'exit', 'fopen', 'fclose', 'fread', 'fwrite', 'make', 'new', 'panic', 'recover', 'copy', 'delete', 'puts', 'p', 'pp', 'raise', 'fail', 'lambda', 'proc', 'each', 'select', 'detect', 'collect', 'inject', 'flat_map', 'any?', 'all?', 'none?', 'count', 'first', 'last', 'sort_by', 'group_by', 'partition', 'compact', 'flatten', 'uniq', 'attr_accessor', 'attr_reader', 'attr_writer', 'public', 'private', 'protected', 'include', 'prepend', 'require_relative', 'likely', 'unlikely', 'printk', 'kfree', 'kmalloc', 'kzalloc'}); assign in source target order to BUILT_IN_NAMES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:75-81
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:74-74
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:75-81
interface CallSite {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:76-80
  In source order: For caller_local_id, declare without assigning a value; source annotation str. Then For callee_name, declare without assigning a value; source annotation str. Then For caller_file_path, declare without assigning a value; source annotation str. Then For original_name, assign ''; source annotation str. Then For receiver_name, assign ''; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:81-81
  In source order: For receiver_type, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:84-139
// Source signature: resolve_call_tiered(context: ResolutionContext, imported_files: dict[str, set[str]], site: CallSite) -> tuple[Symbol | None, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_call_tiered(context, imported_files, site) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:89-90
  In source order: Retain source documentation literal source_literal_89_4; it is not a model call. Then Evaluate once list(context.symbols_by_name.get(site.callee_name, [])); assign in source target order to candidates.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:91-92
  if (the source predicate site.original_name and site.original_name != site.callee_name is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:92-92
    In source order: Evaluate candidates.extend(context.symbols_by_name.get(site.original_name, [])); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:93-94
  if (the source predicate not candidates is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:94-94
    End this invocation with (None, 0).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:96-100
  In source order: Evaluate once imported_files.get(file_local_id(site.caller_file_path), set()); assign in source target order to imports. Then Evaluate once posixpath.dirname(site.caller_file_path); assign in source target order to caller_dir. Then For best, assign None; source annotation Symbol | None. Then Evaluate once -1; assign in source target order to best_score.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:101-138
  for each candidate in candidates {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:102-102
    In source order: Evaluate once 0; assign in source target order to score.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:103-104
    if (the source predicate candidate.label in CALLABLE_LABELS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:104-104
      In source order: Apply source augmented assignment score += 10 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:105-105
    In source order: Evaluate once candidate.owner_name; assign in source target order to owner.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:106-113
    if (the source predicate site.caller_file_path and candidate.file_path == site.caller_file_path is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:107-113
      if (the source predicate not site.receiver_name or not owner or len(site.receiver_name) <= 2 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:108-108
        In source order: Apply source augmented assignment score += 100 with source evaluation/in-place semantics.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:110-111
        In source order: Evaluate once site.receiver_name.lower(); assign in source target order to receiver. Then Evaluate once owner.lower(); assign in source target order to owner_lower.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:112-113
        if (the source predicate receiver == owner_lower or owner_lower.startswith(receiver) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:113-113
          In source order: Apply source augmented assignment score += 100 with source evaluation/in-place semantics.
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:114-131
    if (the source predicate site.caller_file_path is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:115-124
      if (the source predicate candidate.file_path in imports is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:116-116
        In source order: Apply source augmented assignment score += 50 with source evaluation/in-place semantics.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:118-118
        In source order: Evaluate once posixpath.dirname(candidate.file_path); assign in source target order to candidate_dir.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:119-124
        if (the source predicate candidate_dir and any((posixpath.dirname(path) == candidate_dir for path in imports)) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:124-124
          In source order: Apply source augmented assignment score += 45 with source evaluation/in-place semantics.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:125-131
      if (the source predicate candidate.file_path and candidate.file_path != site.caller_file_path and caller_dir and (posixpath.dirname(candidate.file_path) == caller_dir) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:131-131
        In source order: Apply source augmented assignment score += 40 with source evaluation/in-place semantics.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:132-133
    if (the source predicate site.receiver_type and owner and (owner == site.receiver_type) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:133-133
      In source order: Apply source augmented assignment score += 200 with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:134-138
    if (the source predicate score > best_score or (score == best_score and best is not None and (candidate.id < best.id)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:137-138
      In source order: Evaluate once candidate; assign in source target order to best. Then Evaluate once score; assign in source target order to best_score.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:139-139
  End this invocation with (best, best_score).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:142-152
// Source signature: _build_imported_files(result: ResolutionResult, context: ResolutionContext) -> dict[str, set[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _build_imported_files(result, context) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:145-145
  In source order: For imported, assign {}; source annotation dict[str, set[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:146-151
  for each edge in result.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:147-148
    if (the source predicate edge.relationship is not LocalRelationshipType.IMPORTS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:148-148
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:149-149
    In source order: Evaluate once edge.target_local_id; assign in source target order to target.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:150-151
    if (the source predicate target.startswith('file:') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:151-151
      In source order: Evaluate imported.setdefault(edge.source_local_id, set()).add(target.removeprefix('file:')); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:152-152
  End this invocation with imported.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:155-195
// Source signature: _external_receivers(context: ResolutionContext, result: ResolutionResult) -> dict[str, set[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _external_receivers(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:158-159
  In source order: Retain source documentation literal source_literal_158_4; it is not a model call. Then For resolved_targets, assign {}; source annotation dict[str, set[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:160-166
  for each edge in result.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:161-162
    if (the source predicate edge.relationship is not LocalRelationshipType.IMPORTS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:162-162
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:163-166
    if (the source predicate edge.source_local_id.startswith('file:') and edge.target_local_id.startswith('file:') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:164-166
      In source order: Evaluate resolved_targets.setdefault(edge.source_local_id.removeprefix('file:'), set()).add(edge.target_local_id.removeprefix('file:')); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:167-167
  In source order: For externals, assign {}; source annotation dict[str, set[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:168-194
  for each (path, file_result) in context.extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:169-170
    if (the source predicate context.file_language.get(path) != 'go' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:170-170
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:171-194
    for each imported in file_result.imports {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:172-175
      In source order: Evaluate once imported.source; assign in source target order to source. Then Evaluate once False; assign in source target order to is_resolved. Then Evaluate once resolved_targets.get(path, set()); assign in source target order to targets. Then Evaluate once source.split('/'); assign in source target order to parts.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:176-180
      for each index in range(len(parts)) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:177-177
        In source order: Evaluate once '/'.join(parts[index:]); assign in source target order to suffix.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:178-180
        if (the source predicate any((t == suffix or t.startswith(suffix + '/') for t in targets)) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:179-179
          In source order: Evaluate once True; assign in source target order to is_resolved.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:180-180
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:181-182
      if (the source predicate is_resolved is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:182-182
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:183-183
      In source order: Evaluate once posixpath.basename(source); assign in source target order to alias.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:184-185
      if (the source predicate not alias or alias == '.' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:185-185
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:186-189
      if (the source predicate len(alias) >= 2 and alias[0] == 'v' and alias[1].isdigit() is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:187-187
        In source order: Evaluate once posixpath.basename(posixpath.dirname(source)); assign in source target order to parent.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:188-189
        if (the source predicate parent and parent != '.' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:189-189
          In source order: Evaluate once parent; assign in source target order to alias.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:190-193
      for each binding in imported.bindings {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:191-193
        if (the source predicate binding.alias is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:192-192
          In source order: Evaluate once binding.alias; assign in source target order to alias.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:193-193
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:194-194
      In source order: Evaluate externals.setdefault(path, set()).add(alias); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:195-195
  End this invocation with externals.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:198-288
// Source signature: resolve_calls_spawns_delegates(context: ResolutionContext, result: ResolutionResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_calls_spawns_delegates(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:199-200
  In source order: Evaluate once _build_imported_files(result, context); assign in source target order to imported_files. Then Evaluate once _external_receivers(context, result); assign in source target order to externals.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:202-288
  for each (path, file_result) in context.extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:203-203
    In source order: Evaluate once context.import_aliases.get(path, {}); assign in source target order to aliases.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:204-230
    for each call in file_result.calls {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:205-206
      if (the source predicate call.callee_name in BUILT_IN_NAMES is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:206-206
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:207-208
      if (the source predicate call.receiver_name and call.receiver_name in externals.get(path, set()) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:208-208
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:209-211
      In source order: Evaluate once context.receiver_type(path, call.receiver_name) if call.receiver_name else ''; assign in source target order to receiver_type.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:212-213
      if (the source predicate call.receiver_name and call.receiver_name in aliases is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:213-213
        In source order: Evaluate once aliases[call.receiver_name]; assign in source target order to receiver_type.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:214-222
      In source order: Evaluate once CallSite(caller_local_id=context.enclosing_symbol(path, call.line), callee_name=call.callee_name, caller_file_path=path, original_name=aliases.get(call.callee_name, ''), receiver_name=call.receiver_name, receiver_type=receiver_type); assign in source target order to site. Then Evaluate once resolve_call_tiered(context, imported_files, site); assign in source target order to (target, _).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:223-224
      if (the source predicate target is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:224-224
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:225-230
      In source order: Evaluate result.add_edge(site.caller_local_id, LocalRelationshipType.CALLS, target.id, {'confidence': CALL_CONFIDENCE, 'reason': CALL_REASON}); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:234-252
    for each spawn in file_result.spawns {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:235-244
      In source order: Evaluate once CallSite(caller_local_id=context.enclosing_symbol(path, spawn.line), callee_name=spawn.target_name, caller_file_path=path, receiver_name=spawn.receiver_name, receiver_type=context.receiver_type(path, spawn.receiver_name) if spawn.receiver_name else ''); assign in source target order to site. Then Evaluate once resolve_call_tiered(context, imported_files, site); assign in source target order to (target, _).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:245-246
      if (the source predicate target is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:246-246
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:247-252
      In source order: Evaluate result.add_edge(site.caller_local_id, LocalRelationshipType.SPAWNS, target.id, {'confidence': SPAWN_CONFIDENCE}); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:254-288
    for each delegate in file_result.delegates {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:255-256
      if (the source predicate delegate.target_name in BUILT_IN_NAMES is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:256-256
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:257-268
      In source order: Evaluate once CallSite(caller_local_id=context.enclosing_symbol(path, delegate.line), callee_name=delegate.target_name, caller_file_path=path, receiver_name=delegate.receiver_name, receiver_type=context.receiver_type(path, delegate.receiver_name) if delegate.receiver_name else ''); assign in source target order to site. Then Evaluate once resolve_call_tiered(context, imported_files, site); assign in source target order to (target, score).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:269-270
      if (the source predicate target is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:270-270
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:271-272
      if (the source predicate target.label not in ('Function', 'Method') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:272-272
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:275-276
      if (the source predicate score < 100 or target.file_path != site.caller_file_path is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:276-276
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:279-280
      if (the source predicate not delegate.receiver_name and target.label == 'Method' and target.owner_name is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:280-280
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:281-282
      if (the source predicate site.caller_local_id == target.id is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:282-282
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/calls.py:283-288
      In source order: Evaluate result.add_edge(site.caller_local_id, LocalRelationshipType.DELEGATES_TO, target.id, {'confidence': DELEGATE_CONFIDENCE}); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.extractors.records import CALLABLE_LABELS, Symbol` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import LocalRelationshipType` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult, file_local_id` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
