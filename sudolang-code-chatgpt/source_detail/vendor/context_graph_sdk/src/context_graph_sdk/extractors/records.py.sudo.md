# vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.evidence.json`. SHA-256: `537c2195f7b15509c662324806ce3eb1936c46e844a9767c052c487c5c8582a9`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import from collections import Counter; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field, replace; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:23-29
In source order: Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.symbols import SYMBOL_CATEGORY_LABELS; preserve alias and import-time effects. Then Evaluate once frozenset({'TypeAlias', 'CodeElement'}); assign in source target order to GENERIC_LABELS. Then Evaluate once frozenset({'Function', 'Method', 'Constructor'}); assign in source target order to CALLABLE_LABELS. Then Evaluate once frozenset({'Class', 'Interface', 'Module', 'Namespace', 'Trait', 'Impl'}); assign in source target order to OWNERLESS_LABELS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:32-41
// Source signature: symbol_id(label: str, file_path: str, name: str, owner: str, *disambiguators: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn symbol_id(label, file_path, name, owner, disambiguators) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:33-34
  In source order: Retain source documentation literal source_literal_33_4; it is not a model call. Then Evaluate once source_template_34_10; assign in source target order to key.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:35-36
  if (the source predicate owner is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:36-36
    In source order: Apply source augmented assignment key += owner + '.' with source evaluation/in-place semantics.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:37-37
  In source order: Apply source augmented assignment key += name with source evaluation/in-place semantics.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:38-40
  for each disambiguator in disambiguators {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:39-40
    if (the source predicate disambiguator is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:40-40
      In source order: Apply source augmented assignment key += ':' + disambiguator with source evaluation/in-place semantics.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:41-41
  End this invocation with hashlib.sha256(key.encode()).hexdigest()[:24].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:45-65
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:44-44
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:45-65
interface Symbol {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:46-50
  In source order: For id, declare without assigning a value; source annotation str. Then For name, declare without assigning a value; source annotation str. Then For label, declare without assigning a value; source annotation str. Then For file_path, declare without assigning a value; source annotation str. Then For start_line, declare without assigning a value; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:51-55
  In source order: For end_line, declare without assigning a value; source annotation int. Then For is_exported, declare without assigning a value; source annotation bool. Then For language, declare without assigning a value; source annotation str. Then For kind, assign ''; source annotation str. Then For content, assign ''; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:56-60
  In source order: For owner_name, assign ''; source annotation str. Then For doc_comment, assign ''; source annotation str. Then For annotations, assign ''; source annotation str. Then For signature, assign ''; source annotation str. Then For parameter_count, assign 0; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:61-61
  In source order: For return_type, assign ''; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:63-65
  // Source signature: __post_init__(self) -> None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn __post_init__(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:64-65
    if (the source predicate self.label not in SYMBOL_CATEGORY_LABELS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:65-65
      Raise ModelValidationError(source_template_65_39).
    }
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:69-71
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:68-68
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:69-71
interface ImportBinding {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:70-71
  In source order: For original, declare without assigning a value; source annotation str. Then For alias, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:75-78
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:74-74
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:75-78
interface Import {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:76-78
  In source order: For file_path, declare without assigning a value; source annotation str. Then For source, declare without assigning a value; source annotation str. Then For bindings, assign (); source annotation tuple[ImportBinding, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:82-86
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:81-81
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:82-86
interface Call {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:83-86
  In source order: For file_path, declare without assigning a value; source annotation str. Then For callee_name, declare without assigning a value; source annotation str. Then For receiver_name, assign ''; source annotation str. Then For line, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:90-94
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:89-89
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:90-94
interface Assignment {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:91-94
  In source order: For file_path, declare without assigning a value; source annotation str. Then For receiver_name, declare without assigning a value; source annotation str. Then For property_name, declare without assigning a value; source annotation str. Then For line, declare without assigning a value; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:98-102
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:97-97
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:98-102
interface Spawn {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:99-102
  In source order: For file_path, declare without assigning a value; source annotation str. Then For target_name, declare without assigning a value; source annotation str. Then For receiver_name, assign ''; source annotation str. Then For line, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:106-110
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:105-105
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:106-110
interface Delegate {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:107-110
  In source order: For file_path, declare without assigning a value; source annotation str. Then For target_name, declare without assigning a value; source annotation str. Then For receiver_name, assign ''; source annotation str. Then For line, assign 0; source annotation int.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:114-120
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:113-113
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:114-120
interface Heritage {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:115-120
  In source order: Retain source documentation literal source_literal_115_4; it is not a model call. Then For file_path, declare without assigning a value; source annotation str. Then For class_name, declare without assigning a value; source annotation str. Then For parent_name, declare without assigning a value; source annotation str. Then For kind, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:124-130
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:123-123
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:124-130
interface TypeBinding {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:125-129
  In source order: For file_path, declare without assigning a value; source annotation str. Then For variable_name, declare without assigning a value; source annotation str. Then For type_name, declare without assigning a value; source annotation str. Then For line, declare without assigning a value; source annotation int. Then For kind, declare without assigning a value; source annotation str.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:130-130
  In source order: For owner_name, assign ''; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:134-136
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:133-133
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:134-136
interface FileDiagnostic {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:135-136
  In source order: For file_path, declare without assigning a value; source annotation str. Then For reason, declare without assigning a value; source annotation str.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:140-148
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:139-139
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:140-148
interface FileExtraction {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:141-145
  In source order: For symbols, assign (); source annotation tuple[Symbol, ...]. Then For imports, assign (); source annotation tuple[Import, ...]. Then For calls, assign (); source annotation tuple[Call, ...]. Then For assignments, assign (); source annotation tuple[Assignment, ...]. Then For spawns, assign (); source annotation tuple[Spawn, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:146-148
  In source order: For delegates, assign (); source annotation tuple[Delegate, ...]. Then For heritage, assign (); source annotation tuple[Heritage, ...]. Then For type_bindings, assign (); source annotation tuple[TypeBinding, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:152-158
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:151-151
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:152-158
interface ExtractionResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:153-154
  In source order: For files, assign (); source annotation tuple[tuple[str, FileExtraction], ...]. Then For diagnostics, assign (); source annotation tuple[FileDiagnostic, ...].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:157-158
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:156-156
  Before creating this callable, evaluate and retain decorators top-to-bottom: property.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:157-158
  // Source signature: symbols(self) -> tuple[Symbol, ...]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn symbols(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:158-158
    End this invocation with tuple((sym for _, extraction in self.files for sym in extraction.symbols)).
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:162-184
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:161-161
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:162-184
interface MutableFileResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:163-168
  In source order: Retain source documentation literal source_literal_163_4; it is not a model call. Then For symbols, assign field(default_factory=list[Symbol]); source annotation list[Symbol]. Then For imports, assign field(default_factory=list[Import]); source annotation list[Import]. Then For calls, assign field(default_factory=list[Call]); source annotation list[Call]. Then For assignments, assign field(default_factory=list[Assignment]); source annotation list[Assignment].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:169-172
  In source order: For spawns, assign field(default_factory=list[Spawn]); source annotation list[Spawn]. Then For delegates, assign field(default_factory=list[Delegate]); source annotation list[Delegate]. Then For heritage, assign field(default_factory=list[Heritage]); source annotation list[Heritage]. Then For type_bindings, assign field(default_factory=list[TypeBinding]); source annotation list[TypeBinding].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:174-184
  // Source signature: freeze(self) -> FileExtraction
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn freeze(self) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:175-184
    End this invocation with FileExtraction(tuple(self.symbols), tuple(self.imports), tuple(self.calls), tuple(self.assignments), tuple(self.spawns), tuple(self.delegates), tuple(self.heritage), tuple(self.type_bindings)).
    If execution reaches this end, finish with the source implicit None result.
  }
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:187-210
// Source signature: deduplicate_symbols(symbols: list[Symbol]) -> list[Symbol]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn deduplicate_symbols(symbols) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:188-189
  In source order: Retain source documentation literal source_literal_188_4; it is not a model call. Then For best, assign {}; source annotation dict[tuple[str, int], int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:190-202
  for each (index, symbol) in enumerate(symbols) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:191-192
    In source order: Evaluate once (symbol.name, symbol.start_line); assign in source target order to key. Then Evaluate once best.get(key); assign in source target order to existing.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:193-195
    if (the source predicate existing is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:194-194
      In source order: Evaluate once index; assign in source target order to best[key].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:195-195
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:196-196
    In source order: Evaluate once symbols[existing]; assign in source target order to current.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:197-198
    if (the source predicate current.label in GENERIC_LABELS and symbol.label not in GENERIC_LABELS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:198-198
      In source order: Evaluate once index; assign in source target order to best[key].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:199-200
    if (the source predicate current.label == 'Function' and symbol.label == 'Method' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:200-200
      In source order: Evaluate once index; assign in source target order to best[key].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:201-202
    if (the source predicate current.label == 'Property' and symbol.label == 'Const' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:202-202
      In source order: Evaluate once index; assign in source target order to best[key].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:203-204
  In source order: For deduped, assign []; source annotation list[Symbol]. Then For seen, assign set(); source annotation set[tuple[str, int]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:205-209
  for each symbol in symbols {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:206-206
    In source order: Evaluate once (symbol.name, symbol.start_line); assign in source target order to key.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:207-209
    if (the source predicate key not in seen is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:208-209
      In source order: Evaluate seen.add(key); retain side effects and discard the expression result. Then Evaluate deduped.append(symbols[best[key]]); retain side effects and discard the expression result.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:210-210
  End this invocation with deduped.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:213-218
// Source signature: _group_disambiguator(symbol: Symbol) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _group_disambiguator(symbol) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:214-215
  if (the source predicate symbol.signature is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:215-215
    End this invocation with symbol.signature.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:216-217
  if (the source predicate symbol.kind or symbol.content is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:217-217
    End this invocation with symbol.kind + '\x00' + symbol.content.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:218-218
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:221-261
// Source signature: disambiguate_duplicate_ids(symbols: list[Symbol]) -> list[Symbol]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn disambiguate_duplicate_ids(symbols) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:222-229
  In source order: Retain source documentation literal source_literal_222_4; it is not a model call. Then For groups, assign {}; source annotation dict[tuple[str, str, str, str], list[int]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:230-232
  for each (index, symbol) in enumerate(symbols) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:231-232
    In source order: Evaluate once (symbol.label, symbol.file_path, symbol.owner_name, symbol.name); assign in source target order to key. Then Evaluate groups.setdefault(key, []).append(index); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:233-260
  for each indexes in groups.values() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:234-235
    if (the source predicate len(indexes) < 2 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:235-235
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:236-236
    In source order: For proposed, assign {}; source annotation dict[int, str].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:237-244
    for each index in indexes {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:238-244
      In source order: Evaluate once symbols[index]; assign in source target order to symbol. Then Evaluate once _group_disambiguator(symbol) or source_template_240_16; assign in source target order to disambiguator. Then Evaluate once symbol_id(symbol.label, symbol.file_path, symbol.name, symbol.owner_name, disambiguator); assign in source target order to proposed[index].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:245-247
    In source order: Evaluate once {identifier for identifier, count in Counter(proposed.values()).items() if count > 1}; assign in source target order to collisions.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:248-260
    for each index in indexes {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:249-250
      In source order: Evaluate once symbols[index]; assign in source target order to symbol. Then Evaluate once proposed[index]; assign in source target order to identifier.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:251-259
      if (the source predicate identifier in collisions is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:252-259
        In source order: Evaluate once symbol_id(symbol.label, symbol.file_path, symbol.name, symbol.owner_name, _group_disambiguator(symbol), source_template_258_20); assign in source target order to identifier.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:260-260
      In source order: Evaluate once replace(symbol, id=identifier); assign in source target order to symbols[index].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:261-261
  End this invocation with symbols.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:264-271
// Source signature: is_valid_symbol_name(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_valid_symbol_name(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:265-266
  if (the source predicate not name or len(name) > 200 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:266-266
    End this invocation with False.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:267-270
  for each char in name {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:268-269
    if (the source predicate char.isalnum() or char in '_$-.:@' or ord(char) > 127 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:269-269
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:270-270
    End this invocation with False.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py:271-271
  End this invocation with True.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import ModelValidationError` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.symbols import SYMBOL_CATEGORY_LABELS` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/symbols.py.sudo.md`.
