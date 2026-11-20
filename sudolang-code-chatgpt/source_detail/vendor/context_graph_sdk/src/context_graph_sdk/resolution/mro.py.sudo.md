# vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py.evidence.json`. SHA-256: `1144983182705fcace30e172537dc9fa600eeb8ca69d59aa9270ba5e2c19eee0`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:15-22
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import Symbol; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:23-28
In source order: Resolve source import from context_graph_sdk.models import LocalRelationshipType; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.heritage import CLASS_LIKE_LABELS; preserve alias and import-time effects. Then Evaluate once 10000; assign in source target order to _MAX_LINEARIZE_STEPS. Then Evaluate once 1000; assign in source target order to _MAX_HIERARCHY_DEPTH.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:31-66
// Source signature: c3_linearize(hierarchy: dict[str, list[str]]) -> dict[str, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn c3_linearize(hierarchy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:32-36
  In source order: Retain source documentation literal source_literal_32_4; it is not a model call. Then For result, assign {}; source annotation dict[str, list[str]]. Then Evaluate once sorted(set(hierarchy).union({parent for parents in hierarchy.values() for parent in parents})); assign in source target order to all_classes.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:37-65
  for each root in all_classes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:38-39
    if (the source predicate root in result is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:39-39
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:40-41
    In source order: For stack, assign [(root, False)]; source annotation list[tuple[str, bool]]. Then For in_progress, assign set(); source annotation set[str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:42-65
    while (the source predicate stack is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:43-44
      if (the source predicate len(stack) > _MAX_HIERARCHY_DEPTH is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:44-44
        Raise ModelValidationError('hierarchy linearization exceeded the depth bound').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:45-45
      In source order: Evaluate once stack.pop(); assign in source target order to (cls, expanded).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:46-47
      if (the source predicate cls in result is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:47-47
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:48-48
      In source order: Evaluate once hierarchy.get(cls, []); assign in source target order to parents.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:49-54
      if (the source predicate expanded is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:50-53
        In source order: Evaluate once [list(result[parent]) for parent in parents]; assign in source target order to sequences. Then Evaluate sequences.append(list(parents)); retain side effects and discard the expression result. Then Evaluate once [cls, *_c3_merge(sequences)]; assign in source target order to result[cls]. Then Evaluate in_progress.discard(cls); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:54-54
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:55-56
      if (the source predicate cls in in_progress is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:56-56
        Raise ModelValidationError(source_template_56_43).
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:57-58
      In source order: Evaluate in_progress.add(cls); retain side effects and discard the expression result. Then Evaluate stack.append((cls, True)); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:59-65
      for each parent in reversed(parents) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:60-63
        if (the source predicate parent in in_progress is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:61-63
          Raise ModelValidationError(source_template_62_24).
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:64-65
        if (the source predicate parent not in result is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:65-65
          In source order: Evaluate stack.append((parent, False)); retain side effects and discard the expression result.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:66-66
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:69-87
// Source signature: _c3_merge(sequences: list[list[str]]) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _c3_merge(sequences) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:70-70
  In source order: For merged, assign []; source annotation list[str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:71-86
  for each _ in range(_MAX_LINEARIZE_STEPS) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:72-72
    In source order: Evaluate once [sequence for sequence in sequences if sequence]; assign in source target order to sequences.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:73-74
    if (the source predicate not sequences is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:74-74
      End this invocation with merged.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:75-75
    In source order: Evaluate once ''; assign in source target order to found.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:76-80
    for each sequence in sequences {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:77-77
      In source order: Evaluate once sequence[0]; assign in source target order to candidate.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:78-80
      if (the source predicate not any((candidate in other[1:] for other in sequences)) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:79-79
        In source order: Evaluate once candidate; assign in source target order to found.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:80-80
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:81-82
    if (the source predicate not found is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:82-82
      Raise ModelValidationError('inconsistent hierarchy: cannot resolve merge order').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:83-83
    In source order: Evaluate merged.append(found); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:84-86
    for each sequence in sequences {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:85-86
      if (the source predicate sequence and sequence[0] == found is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:86-86
        In source order: Delete source targets in order: sequence[0].
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:87-87
  Raise ModelValidationError('hierarchy linearization exceeded the step bound').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:91-95
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:90-90
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:91-95
interface MROAmbiguity {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:92-95
  In source order: For method_name, declare without assigning a value; source annotation str. Then For defined_in, declare without assigning a value; source annotation tuple[str, ...]. Then For resolved_to, declare without assigning a value; source annotation str. Then For reason, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:99-102
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:98-98
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:99-102
interface MROEntry {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:100-102
  In source order: For class_name, declare without assigning a value; source annotation str. Then For language, declare without assigning a value; source annotation str. Then For ambiguities, assign (); source annotation tuple[MROAmbiguity, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:106-109
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:105-105
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:106-109
interface MROComputation {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:107-109
  In source order: For entries, assign field(default_factory=list[MROEntry]); source annotation list[MROEntry]. Then For override_edges, assign 0; source annotation int. Then For ambiguity_count, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:113-116
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:112-112
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:113-116
interface _AncestorMethod {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:114-116
  In source order: For symbol, declare without assigning a value; source annotation Symbol. Then For parent, declare without assigning a value; source annotation Symbol. Then For is_class, declare without assigning a value; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:119-144
// Source signature: _linearize_all(hierarchy: dict[str, list[str]]) -> tuple[dict[str, list[str]], dict[str, str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _linearize_all(hierarchy) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:122-126
  In source order: Retain source documentation literal source_literal_122_4; it is not a model call. Then For orders, assign {}; source annotation dict[str, list[str]]. Then For failures, assign {}; source annotation dict[str, str].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:127-143
  for each cls in sorted(hierarchy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:128-130
    In source order: For subset_seen, assign set(); source annotation set[str]. Then Evaluate once [cls]; assign in source target order to pending. Then For subset, assign {}; source annotation dict[str, list[str]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:131-138
    while (the source predicate pending is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:132-132
      In source order: Evaluate once pending.pop(); assign in source target order to current.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:133-134
      if (the source predicate current in subset_seen is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:134-134
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:135-138
      In source order: Evaluate subset_seen.add(current); retain side effects and discard the expression result. Then Evaluate once hierarchy.get(current, []); assign in source target order to parents. Then Evaluate once list(parents); assign in source target order to subset[current]. Then Evaluate pending.extend(parents); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:139-143
    Perform the following protected operations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:140-140
      In source order: Evaluate orders.update(c3_linearize(subset)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:141-143
    On the first matching source exception ModelValidationError as error, in handler order {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:142-143
      In source order: Evaluate once str(error); assign in source target order to failures[cls]. Then Evaluate once [cls, *hierarchy.get(cls, [])]; assign in source target order to orders[cls].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:144-144
  End this invocation with (orders, failures).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:147-246
// Source signature: compute_mro(context: ResolutionContext, result: ResolutionResult) -> MROComputation
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn compute_mro(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:148-155
  In source order: Retain source documentation literal source_literal_148_4; it is not a model call. Then Evaluate once MROComputation(); assign in source target order to computation. Then For parents_by_child, assign {}; source annotation dict[str, list[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:156-165
  for each edge in result.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:157-165
    if (the source predicate edge.relationship in (LocalRelationshipType.INHERITS, LocalRelationshipType.IMPLEMENTS) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:161-162
      if (the source predicate edge.target_local_id not in context.symbols_by_id is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:162-162
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:163-163
      In source order: Evaluate once parents_by_child.setdefault(edge.source_local_id, []); assign in source target order to bucket.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:164-165
      if (the source predicate edge.target_local_id not in bucket is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:165-165
        In source order: Evaluate bucket.append(edge.target_local_id); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:167-169
  In source order: Evaluate once _linearize_all(parents_by_child); assign in source target order to (orders, failures). Then For methods_by_owner, assign {}; source annotation dict[str, list[Symbol]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:170-174
  for each symbol in context.symbols {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:171-174
    if (the source predicate symbol.label == 'Method' and symbol.owner_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:172-174
      In source order: Evaluate methods_by_owner.setdefault(source_template_172_40, []).append(symbol); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:176-177
  // Source signature: own_methods(owner: Symbol) -> list[Symbol]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn own_methods(owner) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:177-177
    End this invocation with methods_by_owner.get(source_template_177_36, []).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:179-245
  for each symbol in context.symbols {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:180-181
    if (the source predicate symbol.label not in CLASS_LIKE_LABELS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:181-181
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:182-183
    if (the source predicate symbol.id not in parents_by_child is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:183-183
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:184-188
    In source order: Evaluate once [context.symbols_by_id[ancestor_id] for ancestor_id in orders.get(symbol.id, [])[1:] if ancestor_id in context.symbols_by_id]; assign in source target order to ancestors.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:189-190
    if (the source predicate not ancestors is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:190-190
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:192-192
    In source order: Evaluate once {method.name for method in own_methods(symbol)}; assign in source target order to own_names.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:196-204
    for each child_method in own_methods(symbol) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:197-204
      for each ancestor in ancestors {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:198-204
        for each ancestor_method in own_methods(ancestor) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:199-204
          if (the source predicate ancestor_method.name == child_method.name and result.add_edge(child_method.id, LocalRelationshipType.OVERRIDES, ancestor_method.id) is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:204-204
            In source order: Apply source augmented assignment computation.override_edges += 1 with source evaluation/in-place semantics.
          }
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:206-206
    In source order: For sources_by_name, assign {}; source annotation dict[str, list[_AncestorMethod]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:207-212
    for each ancestor in ancestors {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:208-208
      In source order: Evaluate once ancestor.label in ('Class', 'Struct'); assign in source target order to is_class.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:209-212
      for each method in own_methods(ancestor) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:210-212
        In source order: Evaluate sources_by_name.setdefault(method.name, []).append(_AncestorMethod(method, ancestor, is_class)); retain side effects and discard the expression result.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:214-214
    In source order: For ambiguities, assign []; source annotation list[MROAmbiguity].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:215-218
    if (the source predicate symbol.id in failures is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:216-218
      In source order: Evaluate ambiguities.append(MROAmbiguity('', (), '', source_template_217_41)); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:219-243
    for each method_name in sorted(sources_by_name) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:220-221
      if (the source predicate method_name in own_names is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:221-221
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:222-223
      In source order: For unique, assign []; source annotation list[_AncestorMethod]. Then For seen, assign set(); source annotation set[str].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:224-227
      for each source in sources_by_name[method_name] {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:225-227
        if (the source predicate source.symbol.id not in seen is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:226-227
          In source order: Evaluate seen.add(source.symbol.id); retain side effects and discard the expression result. Then Evaluate unique.append(source); retain side effects and discard the expression result.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:228-229
      if (the source predicate len(unique) < 2 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:229-229
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:230-238
      In source order: Evaluate once _resolve_ambiguity(symbol.language, unique, ancestors); assign in source target order to (resolved_to, reason). Then Evaluate ambiguities.append(MROAmbiguity(method_name, tuple((source.symbol.id for source in unique)), resolved_to, reason)); retain side effects and discard the expression result.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:239-243
      if (the source predicate resolved_to is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:240-241
        if (the source predicate result.add_edge(symbol.id, LocalRelationshipType.OVERRIDES, resolved_to) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:241-241
          In source order: Apply source augmented assignment computation.override_edges += 1 with source evaluation/in-place semantics.
        }
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:243-243
        In source order: Apply source augmented assignment computation.ambiguity_count += 1 with source evaluation/in-place semantics.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:245-245
    In source order: Evaluate computation.entries.append(MROEntry(symbol.name, symbol.language, tuple(ambiguities))); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:246-246
  End this invocation with computation.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:249-260
// Source signature: _resolve_ambiguity(language: str, sources: list[_AncestorMethod], parent_order: list[Symbol]) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_ambiguity(language, sources, parent_order) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:252-253
  if (the source predicate language == 'cpp' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:253-253
    End this invocation with _resolve_leftmost(sources, parent_order, 'C++ leftmost').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:254-255
  if (the source predicate language == 'python' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:255-255
    End this invocation with _resolve_leftmost(sources, parent_order, 'Python C3').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:256-257
  if (the source predicate language in ('csharp', 'java') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:257-257
    End this invocation with _resolve_class_beats_interface(sources).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:258-259
  if (the source predicate language == 'rust' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:259-259
    End this invocation with ('', 'ambiguous: Rust requires qualified syntax (<Type as Trait>::method)').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:260-260
  End this invocation with _resolve_leftmost(sources, parent_order, 'leftmost base').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:263-278
// Source signature: _resolve_leftmost(sources: list[_AncestorMethod], parent_order: list[Symbol], prefix: str) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_leftmost(sources, parent_order, prefix) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:268-270
  In source order: Evaluate once {parent.id: index for index, parent in enumerate(parent_order)}; assign in source target order to order_index. Then For best, assign None; source annotation _AncestorMethod | None. Then Evaluate once len(parent_order) + 1; assign in source target order to best_index.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:271-275
  for each source in sources {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:272-272
    In source order: Evaluate once order_index.get(source.parent.id); assign in source target order to index.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:273-275
    if (the source predicate index is not None and index < best_index is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:274-275
      In source order: Evaluate once index; assign in source target order to best_index. Then Evaluate once source; assign in source target order to best.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:276-277
  if (the source predicate best is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:277-277
    End this invocation with (best.symbol.id, source_template_277_31).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:278-278
  End this invocation with (sources[0].symbol.id, source_template_278_33).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:281-290
// Source signature: _resolve_class_beats_interface(sources: list[_AncestorMethod]) -> tuple[str, str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_class_beats_interface(sources) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:282-283
  In source order: Evaluate once [source for source in sources if source.is_class]; assign in source target order to class_sources. Then Evaluate once [source for source in sources if not source.is_class]; assign in source target order to interface_sources.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:284-285
  if (the source predicate len(class_sources) == 1 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:285-285
    End this invocation with (class_sources[0].symbol.id, 'class method wins over interface default').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:286-287
  if (the source predicate len(class_sources) > 1 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:287-287
    End this invocation with ('', 'ambiguous: multiple class methods').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:288-289
  if (the source predicate len(interface_sources) == 1 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:289-289
    End this invocation with (interface_sources[0].symbol.id, 'single interface method').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/mro.py:290-290
  End this invocation with ('', 'ambiguous: multiple interface defaults').
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.extractors.records import Symbol` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.models import LocalRelationshipType` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
- `from context_graph_sdk.resolution.heritage import CLASS_LIKE_LABELS` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/heritage.py.sudo.md`.
