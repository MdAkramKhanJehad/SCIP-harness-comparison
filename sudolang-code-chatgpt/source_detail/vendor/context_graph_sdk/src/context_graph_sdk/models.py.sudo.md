# vendor/context_graph_sdk/src/context_graph_sdk/models.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/models.py.evidence.json`. SHA-256: `8e44d9ccce2df0b526eaa8c7fd79d450b30488117f6209e634a15634d6a10120`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import from collections.abc import Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:22-28
In source order: Resolve source import from enum import StrEnum; preserve alias and import-time effects. Then Resolve source import from typing import TypeAlias, cast; preserve alias and import-time effects. Then Resolve source import from .errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from .identity import ProjectId, SnapshotId, make_edge_id, make_global_id, validate_local_id; preserve alias and import-time effects. Then For PropertyScalar, assign str | int | float | bool | None; source annotation TypeAlias.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:29-29
In source order: For PropertyValue, assign 'PropertyScalar | tuple[PropertyValue, ...] | FrozenMap'; source annotation TypeAlias.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:33-53
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:32-32
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:33-53
interface FrozenMap {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:34-36
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call. Then For entries, assign (); source annotation tuple[tuple[str, PropertyValue], ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:38-44
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:39-39
    In source order: Evaluate once [key for key, _ in self.entries]; assign in source target order to keys.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:40-41
    if (the source predicate any((not key for key in keys)) or len(keys) != len(set(keys)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:41-41
      Raise ModelValidationError('property keys must be non-empty and unique').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:42-43
    if (the source predicate keys != sorted(keys) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:43-43
      Raise ModelValidationError('property keys must be sorted').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:44-44
    In source order: Evaluate _validate_frozen_map(self, budget=_PropertyBudget(), depth=0); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:46-50
  // Source signature: __getitem__(self, key: str) -> PropertyValue
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __getitem__(self, key) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:47-49
    for each (candidate, value) in self.entries {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:48-49
      if (the source predicate candidate == key is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:49-49
        End this invocation with value.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:50-50
    Raise KeyError(key).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:52-53
  // Source signature: to_dict(self) -> dict[str, object]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn to_dict(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:53-53
    End this invocation with {key: thaw_value(value) for key, value in self.entries}.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:56-57
In source order: Evaluate once 8; assign in source target order to MAX_PROPERTY_DEPTH. Then Evaluate once 10000; assign in source target order to MAX_PROPERTY_ITEMS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:61-67
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:60-60
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:61-67
interface _PropertyBudget {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:62-62
  In source order: For items, assign 0; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:64-67
  // Source signature: consume(self, count: int) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn consume(self, count) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:65-65
    In source order: Apply source augmented assignment self.items += count with source evaluation/in-place semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:66-67
    if (the source predicate self.items > MAX_PROPERTY_ITEMS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:67-67
      Raise ModelValidationError('property value tree exceeds aggregate item limit').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:70-75
// Source signature: _validate_frozen_map(value: FrozenMap, *, budget: _PropertyBudget, depth: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_frozen_map(value, budget, depth) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:71-72
  if (the source predicate depth > MAX_PROPERTY_DEPTH is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:72-72
    Raise ModelValidationError('property nesting exceeds maximum depth').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:73-73
  In source order: Evaluate budget.consume(len(value.entries)); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:74-75
  for each (_, child) in value.entries {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:75-75
    In source order: Evaluate _validate_frozen_value(child, budget=budget, depth=depth + 1); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:78-96
// Source signature: _validate_frozen_value(value: object, *, budget: _PropertyBudget, depth: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _validate_frozen_value(value, budget, depth) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:79-80
  if (the source predicate depth > MAX_PROPERTY_DEPTH is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:80-80
    Raise ModelValidationError('property nesting exceeds maximum depth').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:81-82
  if (the source predicate value is None or isinstance(value, str | bool | int) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:82-82
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:83-86
  if (the source predicate isinstance(value, float) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:84-85
    if (the source predicate not math.isfinite(value) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:85-85
      Raise ModelValidationError('float properties must be finite').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:86-86
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:87-89
  if (the source predicate isinstance(value, FrozenMap) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:88-88
    In source order: Evaluate _validate_frozen_map(value, budget=budget, depth=depth); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:89-89
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:90-95
  if (the source predicate isinstance(value, tuple) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:91-92
    In source order: Evaluate once cast(tuple[object, ...], value); assign in source target order to sequence. Then Evaluate budget.consume(len(sequence)); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:93-94
    for each child in sequence {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:94-94
      In source order: Evaluate _validate_frozen_value(child, budget=budget, depth=depth + 1); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:95-95
    End this invocation with None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:96-96
  Raise ModelValidationError(source_template_96_31).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:99-130
// Source signature: freeze_value(value: object, *, _depth: int=0, _budget: _PropertyBudget | None=None) -> PropertyValue
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn freeze_value(value, _depth, _budget) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:105-105
  In source order: Evaluate once _budget or _PropertyBudget(); assign in source target order to budget.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:106-107
  if (the source predicate _depth > MAX_PROPERTY_DEPTH is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:107-107
    Raise ModelValidationError('property nesting exceeds maximum depth').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:108-109
  if (the source predicate value is None or isinstance(value, str | bool | int) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:109-109
    End this invocation with value.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:110-113
  if (the source predicate isinstance(value, float) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:111-112
    if (the source predicate not math.isfinite(value) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:112-112
      Raise ModelValidationError('float properties must be finite').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:113-113
    End this invocation with value.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:114-116
  if (the source predicate isinstance(value, FrozenMap) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:115-115
    In source order: Evaluate _validate_frozen_map(value, budget=budget, depth=_depth); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:116-116
    End this invocation with value.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:117-125
  if (the source predicate isinstance(value, Mapping) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:118-120
    In source order: Evaluate once cast(Mapping[object, object], value); assign in source target order to mapping. Then Evaluate budget.consume(len(mapping)); retain side effects and discard the expression result. Then For items, assign []; source annotation list[tuple[str, PropertyValue]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:121-124
    for each (key, child) in mapping.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:122-123
      if (the source predicate not isinstance(key, str) or not key is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:123-123
        Raise ModelValidationError('property map keys must be non-empty strings').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:124-124
      In source order: Evaluate items.append((key, freeze_value(child, _depth=_depth + 1, _budget=budget))); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:125-125
    End this invocation with FrozenMap(tuple(sorted(items))).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:126-129
  if (the source predicate isinstance(value, Sequence) and (not isinstance(value, str | bytes | bytearray)) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:127-128
    In source order: Evaluate once cast(Sequence[object], value); assign in source target order to sequence. Then Evaluate budget.consume(len(sequence)); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:129-129
    End this invocation with tuple((freeze_value(child, _depth=_depth + 1, _budget=budget) for child in sequence)).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:130-130
  Raise ModelValidationError(source_template_130_31).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:133-135
// Source signature: freeze_properties(values: Mapping[str, object] | None=None) -> FrozenMap
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn freeze_properties(values) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:134-134
  In source order: Evaluate once freeze_value(values or {}); assign in source target order to frozen.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:135-135
  End this invocation with cast(FrozenMap, frozen).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:138-143
// Source signature: thaw_value(value: PropertyValue) -> object
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn thaw_value(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:139-140
  if (the source predicate isinstance(value, FrozenMap) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:140-140
    End this invocation with value.to_dict().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:141-142
  if (the source predicate isinstance(value, tuple) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:142-142
    End this invocation with [thaw_value(item) for item in value].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:143-143
  End this invocation with value.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:146-156
interface NodeLabel {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:147-151
  In source order: Evaluate once 'Project'; assign in source target order to PROJECT. Then Evaluate once 'File'; assign in source target order to FILE. Then Evaluate once 'Folder'; assign in source target order to FOLDER. Then Evaluate once 'Module'; assign in source target order to MODULE. Then Evaluate once 'Dependency'; assign in source target order to DEPENDENCY.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:152-156
  In source order: Evaluate once 'Symbol'; assign in source target order to SYMBOL. Then Evaluate once 'Community'; assign in source target order to COMMUNITY. Then Evaluate once 'Process'; assign in source target order to PROCESS. Then Evaluate once 'ProjectSnapshot'; assign in source target order to PROJECT_SNAPSHOT. Then Evaluate once 'NodeRef'; assign in source target order to NODE_REF.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:159-175
interface LocalRelationshipType {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:160-164
  In source order: Evaluate once 'CONTAINS'; assign in source target order to CONTAINS. Then Evaluate once 'DEFINES'; assign in source target order to DEFINES. Then Evaluate once 'IMPORTS'; assign in source target order to IMPORTS. Then Evaluate once 'CALLS'; assign in source target order to CALLS. Then Evaluate once 'SPAWNS'; assign in source target order to SPAWNS.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:165-169
  In source order: Evaluate once 'DELEGATES_TO'; assign in source target order to DELEGATES_TO. Then Evaluate once 'ACCESSES'; assign in source target order to ACCESSES. Then Evaluate once 'USES'; assign in source target order to USES. Then Evaluate once 'INHERITS'; assign in source target order to INHERITS. Then Evaluate once 'IMPLEMENTS'; assign in source target order to IMPLEMENTS.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:170-174
  In source order: Evaluate once 'DEPENDS_ON'; assign in source target order to DEPENDS_ON. Then Evaluate once 'MEMBER_OF'; assign in source target order to MEMBER_OF. Then Evaluate once 'HAS_METHOD'; assign in source target order to HAS_METHOD. Then Evaluate once 'HAS_PROPERTY'; assign in source target order to HAS_PROPERTY. Then Evaluate once 'OVERRIDES'; assign in source target order to OVERRIDES.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:175-175
  In source order: Evaluate once 'STEP_IN_PROCESS'; assign in source target order to STEP_IN_PROCESS.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:178-180
interface CorrelationEndpointRole {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:179-180
  In source order: Evaluate once 'source'; assign in source target order to SOURCE. Then Evaluate once 'target'; assign in source target order to TARGET.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:183-187
interface CorrelationType {
  Describe the source Python type, preserving its base/metaclass expression order: StrEnum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:184-187
  In source order: Evaluate once 'CROSS_REPO_IMPORTS'; assign in source target order to CROSS_REPO_IMPORTS. Then Evaluate once 'CROSS_REPO_CALLS'; assign in source target order to CROSS_REPO_CALLS. Then Evaluate once 'CROSS_REPO_DEPENDENCY'; assign in source target order to CROSS_REPO_DEPENDENCY. Then Evaluate once 'SHARED_TYPE'; assign in source target order to SHARED_TYPE.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:190-190
In source order: Evaluate once frozenset((member.value for member in CorrelationType)); assign in source target order to CORRELATION_RELATIONSHIP_TYPES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:194-204
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:193-193
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:194-204
interface AnalysisVersion {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:195-196
  In source order: For sdk_version, declare without assigning a value; source annotation str. Then For components, assign (); source annotation tuple[tuple[str, str], ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:198-204
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:199-200
    if (the source predicate not self.sdk_version is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:200-200
      Raise ModelValidationError('sdk_version is required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:201-201
    In source order: Evaluate once [name for name, version in self.components if name and version]; assign in source target order to names.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:202-203
    if (the source predicate len(names) != len(self.components) or len(names) != len(set(names)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:203-203
      Raise ModelValidationError('analysis components require unique names and versions').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:204-204
    In source order: Evaluate object.__setattr__(self, 'components', tuple(sorted(self.components))); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:208-217
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:207-207
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:208-217
interface ProjectMetadata {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:209-213
  In source order: For project_id, declare without assigning a value; source annotation ProjectId. Then For display_name, declare without assigning a value; source annotation str. Then For source_path, assign None; source annotation str | None. Then For source_url, assign None; source annotation str | None. Then For revision, assign None; source annotation str | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:215-217
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:216-217
    if (the source predicate not self.display_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:217-217
      Raise ModelValidationError('display_name is required').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:221-228
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:220-220
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:221-228
interface SnapshotLocator {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:222-224
  In source order: For project_id, declare without assigning a value; source annotation ProjectId. Then For snapshot_id, declare without assigning a value; source annotation SnapshotId. Then For database_path, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:226-228
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:227-228
    if (the source predicate not self.database_path is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:228-228
      Raise ModelValidationError('database_path is required').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:232-237
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:231-231
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:232-237
interface SnapshotInfo {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:233-237
  In source order: Retain source documentation literal source_literal_233_4; it is not a model call. Then For fingerprint, declare without assigning a value; source annotation str. Then For node_count, declare without assigning a value; source annotation int. Then For edge_count, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:241-257
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:240-240
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:241-257
interface GraphNode {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:242-246
  In source order: For project_id, declare without assigning a value; source annotation ProjectId. Then For local_id, declare without assigning a value; source annotation str. Then For labels, declare without assigning a value; source annotation tuple[str, ...]. Then For properties, assign field(default_factory=FrozenMap); source annotation FrozenMap. Then For id, assign ''; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:248-257
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:249-249
    In source order: Evaluate validate_local_id(self.local_id); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:250-251
    if (the source predicate not self.labels or any((not label for label in self.labels)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:251-251
      Raise ModelValidationError('a node requires non-empty labels').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:252-254
    In source order: Evaluate once tuple(sorted(set(self.labels))); assign in source target order to labels. Then Evaluate object.__setattr__(self, 'labels', labels); retain side effects and discard the expression result. Then Evaluate once make_global_id(self.project_id, self.local_id); assign in source target order to expected.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:255-256
    if (the source predicate self.id and self.id != expected is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:256-256
      Raise ModelValidationError('node global id does not match project/local identity').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:257-257
    In source order: Evaluate object.__setattr__(self, 'id', expected); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:261-286
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:260-260
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:261-286
interface GraphEdge {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:262-266
  In source order: For project_id, declare without assigning a value; source annotation ProjectId. Then For source_id, declare without assigning a value; source annotation str. Then For relationship_type, declare without assigning a value; source annotation str. Then For target_id, declare without assigning a value; source annotation str. Then For discriminator, assign ''; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:267-268
  In source order: For properties, assign field(default_factory=FrozenMap); source annotation FrozenMap. Then For id, assign ''; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:270-286
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:271-272
    if (the source predicate not self.relationship_type is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:272-272
      Raise ModelValidationError('relationship_type is required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:273-276
    if (the source predicate self.relationship_type in CORRELATION_RELATIONSHIP_TYPES is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:274-276
      Raise ModelValidationError('cross-project relationship types belong in the correlation store').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:277-283
    In source order: Evaluate once make_edge_id(self.project_id, self.source_id, self.relationship_type, self.target_id, self.discriminator); assign in source target order to expected.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:284-285
    if (the source predicate self.id and self.id != expected is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:285-285
      Raise ModelValidationError('edge id does not match its identity fields').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:286-286
    In source order: Evaluate object.__setattr__(self, 'id', expected); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:290-316
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:289-289
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:290-316
interface GraphSnapshot {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:291-295
  In source order: For project, declare without assigning a value; source annotation ProjectMetadata. Then For snapshot_id, declare without assigning a value; source annotation SnapshotId. Then For analysis_version, declare without assigning a value; source annotation AnalysisVersion. Then For nodes, assign (); source annotation tuple[GraphNode, ...]. Then For edges, assign (); source annotation tuple[GraphEdge, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:297-316
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:298-298
    In source order: Evaluate once {node.id for node in self.nodes}; assign in source target order to node_ids.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:299-300
    if (the source predicate len(node_ids) != len(self.nodes) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:300-300
      Raise ModelValidationError('snapshot contains duplicate node ids').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:301-302
    if (the source predicate any((node.project_id != self.project.project_id for node in self.nodes)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:302-302
      Raise ModelValidationError('snapshot nodes must belong to its project').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:303-303
    In source order: Evaluate once {NodeLabel.PROJECT_SNAPSHOT.value, NodeLabel.NODE_REF.value}; assign in source target order to correlation_labels.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:304-307
    if (the source predicate any((correlation_labels.intersection(node.labels) for node in self.nodes)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:305-307
      Raise ModelValidationError('correlation-store labels cannot appear in a project snapshot').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:308-309
    if (the source predicate len({edge.id for edge in self.edges}) != len(self.edges) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:309-309
      Raise ModelValidationError('snapshot contains duplicate edge ids').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:310-314
    for each edge in self.edges {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:311-312
      if (the source predicate edge.project_id != self.project.project_id is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:312-312
        Raise ModelValidationError('local edges must belong to the snapshot project').
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:313-314
      if (the source predicate edge.source_id not in node_ids or edge.target_id not in node_ids is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:314-314
        Raise ModelValidationError('local edge endpoints must exist in the same snapshot').
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:315-316
    In source order: Evaluate object.__setattr__(self, 'nodes', tuple(sorted(self.nodes, key=lambda node: node.id))); retain side effects and discard the expression result. Then Evaluate object.__setattr__(self, 'edges', tuple(sorted(self.edges, key=lambda edge: edge.id))); retain side effects and discard the expression result.
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:320-343
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:319-319
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:320-343
interface GraphMutation {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:321-325
  In source order: For project_id, declare without assigning a value; source annotation ProjectId. Then For nodes, assign (); source annotation tuple[GraphNode, ...]. Then For edges, assign (); source annotation tuple[GraphEdge, ...]. Then For removed_node_ids, assign (); source annotation tuple[str, ...]. Then For removed_edge_ids, assign (); source annotation tuple[str, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:327-343
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:328-329
    if (the source predicate any((node.project_id != self.project_id for node in self.nodes)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:329-329
      Raise ModelValidationError('mutation nodes must belong to its project').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:330-331
    if (the source predicate any((edge.project_id != self.project_id for edge in self.edges)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:331-331
      Raise ModelValidationError('mutation edges must remain project-local').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:332-339
    for each (values, name) in (([node.id for node in self.nodes], 'node'), ([edge.id for edge in self.edges], 'edge'), (list(self.removed_node_ids), 'removed node'), (list(self.removed_edge_ids), 'removed edge')) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:338-339
      if (the source predicate len(values) != len(set(values)) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:339-339
        Raise ModelValidationError(source_template_339_43).
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:340-341
    if (the source predicate {node.id for node in self.nodes}.intersection(self.removed_node_ids) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:341-341
      Raise ModelValidationError('mutation cannot add and remove the same node').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:342-343
    if (the source predicate {edge.id for edge in self.edges}.intersection(self.removed_edge_ids) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:343-343
      Raise ModelValidationError('mutation cannot add and remove the same edge').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:347-359
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:346-346
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:347-359
interface ProjectSnapshot {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:348-352
  In source order: For project, declare without assigning a value; source annotation ProjectMetadata. Then For snapshot_id, declare without assigning a value; source annotation SnapshotId. Then For locator, declare without assigning a value; source annotation SnapshotLocator. Then For analysis_version, declare without assigning a value; source annotation AnalysisVersion. Then For accepted, declare without assigning a value; source annotation bool.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:354-359
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:355-359
    if (the source predicate self.locator.project_id != self.project.project_id or self.locator.snapshot_id != self.snapshot_id is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:359-359
      Raise ModelValidationError('snapshot locator identity does not match its record').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:363-372
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:362-362
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:363-372
interface NodeRef {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:364-367
  In source order: For project_id, declare without assigning a value; source annotation ProjectId. Then For snapshot_id, declare without assigning a value; source annotation SnapshotId. Then For local_id, declare without assigning a value; source annotation str. Then For node_id, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:369-372
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:370-370
    In source order: Evaluate once make_global_id(self.project_id, validate_local_id(self.local_id)); assign in source target order to expected.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:371-372
    if (the source predicate self.node_id != expected is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:372-372
      Raise ModelValidationError('NodeRef global id does not match project/local identity').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:376-392
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:375-375
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:376-392
interface CorrelationEdge {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:377-381
  In source order: For source, declare without assigning a value; source annotation NodeRef. Then For relationship_type, declare without assigning a value; source annotation CorrelationType. Then For target, declare without assigning a value; source annotation NodeRef. Then For provider_name, declare without assigning a value; source annotation str. Then For provider_version, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:382-384
  In source order: For confidence, declare without assigning a value; source annotation float. Then For reason, declare without assigning a value; source annotation str. Then For evidence, assign field(default_factory=FrozenMap); source annotation FrozenMap.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:386-392
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:387-388
    if (the source predicate self.source.project_id == self.target.project_id is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:388-388
      Raise ModelValidationError('correlations must connect different projects').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:389-390
    if (the source predicate not self.provider_name or not self.provider_version or (not self.reason) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:390-390
      Raise ModelValidationError('correlation provenance and reason are required').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:391-392
    if (the source predicate not math.isfinite(self.confidence) or not 0.0 <= self.confidence <= 1.0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:392-392
      Raise ModelValidationError('correlation confidence must be between zero and one').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:396-404
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:395-395
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:396-404
interface ProviderManifest {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:397-400
  In source order: For project_id, declare without assigning a value; source annotation ProjectId. Then For snapshot_id, declare without assigning a value; source annotation SnapshotId. Then For provider_name, declare without assigning a value; source annotation str. Then For provider_version, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:402-404
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:403-404
    if (the source predicate not self.provider_name or not self.provider_version is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:404-404
      Raise ModelValidationError('provider manifest name and version are required').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:408-423
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:407-407
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:408-423
interface ResolvedCorrelation {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:409-411
  In source order: For correlation, declare without assigning a value; source annotation CorrelationEdge. Then For queried_endpoint, declare without assigning a value; source annotation CorrelationEndpointRole. Then For related_snapshot, declare without assigning a value; source annotation ProjectSnapshot.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:413-423
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:414-418
    In source order: Evaluate once self.correlation.target if self.queried_endpoint == CorrelationEndpointRole.SOURCE else self.correlation.source; assign in source target order to related.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:419-423
    if (the source predicate related.project_id != self.related_snapshot.project.project_id or related.snapshot_id != self.related_snapshot.snapshot_id is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:423-423
      Raise ModelValidationError('resolved snapshot does not match the related endpoint').
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:427-462
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:426-426
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:427-462
interface CatalogPublication {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:428-431
  In source order: For snapshot, declare without assigning a value; source annotation ProjectSnapshot. Then For node_refs, declare without assigning a value; source annotation tuple[NodeRef, ...]. Then For correlations, declare without assigning a value; source annotation tuple[CorrelationEdge, ...]. Then For provider_manifests, assign (); source annotation tuple[ProviderManifest, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:433-462
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:434-435
    if (the source predicate not self.snapshot.accepted is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:435-435
      Raise ModelValidationError('published snapshot must be accepted').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:436-436
    In source order: Evaluate once self.snapshot.project.project_id; assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:437-441
    if (the source predicate any((ref.project_id == candidate and ref.snapshot_id != self.snapshot.snapshot_id for ref in self.node_refs)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:441-441
      Raise ModelValidationError('candidate NodeRefs must use the published snapshot').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:442-448
    if (the source predicate any((edge.source.project_id != candidate and edge.target.project_id != candidate for edge in self.correlations)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:446-448
      Raise ModelValidationError('every refreshed correlation must touch the candidate project').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:449-449
    In source order: Evaluate once [manifest.provider_name for manifest in self.provider_manifests]; assign in source target order to manifest_names.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:450-451
    if (the source predicate len(manifest_names) != len(set(manifest_names)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:451-451
      Raise ModelValidationError('provider manifests must have unique names').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:452-456
    if (the source predicate any((manifest.project_id != candidate or manifest.snapshot_id != self.snapshot.snapshot_id for manifest in self.provider_manifests)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:456-456
      Raise ModelValidationError('provider manifests must belong to the published snapshot').
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:457-457
    In source order: Evaluate once {(ref.project_id, ref.snapshot_id, ref.node_id) for ref in self.node_refs}; assign in source target order to refs.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:458-462
    for each edge in self.correlations {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:459-462
      for each endpoint in (edge.source, edge.target) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:460-460
        In source order: Evaluate once (endpoint.project_id, endpoint.snapshot_id, endpoint.node_id); assign in source target order to key.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:461-462
        if (the source predicate key not in refs is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/models.py:462-462
          Raise ModelValidationError('correlation endpoints require persisted NodeRefs').
        }
      }
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
```

## Local import links

- `from .errors import ModelValidationError` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from .identity import ProjectId, SnapshotId, make_edge_id, make_global_id, validate_local_id` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/identity.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../../prompt_representation/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md). Exact strings in the evidence asset support this conversion.
