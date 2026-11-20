# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/rust.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/rust.scm`. SHA-256 `74e4de651db75792515cf8ee5198c466e7287f070596ee6d169a189947b732b3`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/rust.scm:1-37
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for rust
; Copyright 2026 Visa, Inc.
; Licensed under the Apache License, Version 2.0 (the "License");
; you may not use this file except in compliance with the License.
; You may obtain a copy of the License at
; http://www.apache.org/licenses/LICENSE-2.0
; Unless required by applicable law or agreed to in writing, software
; distributed under the License is distributed on an "AS IS" BASIS,
; WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
; See the License for the specific language governing permissions and
; limitations under the License.
(function_item name: (identifier) @name) @definition.function
(struct_item name: (type_identifier) @name) @definition.struct
(enum_item name: (type_identifier) @name) @definition.enum
(trait_item name: (type_identifier) @name) @definition.trait
(impl_item type: (type_identifier) @name !trait) @definition.impl
(mod_item name: (identifier) @name) @definition.module
(type_item name: (type_identifier) @name) @definition.type
(const_item name: (identifier) @name) @definition.const
(static_item name: (identifier) @name) @definition.static
(macro_definition name: (identifier) @name) @definition.macro
(use_declaration argument: (_) @import.source) @import
(call_expression function: (identifier) @call.name) @call
(call_expression function: (field_expression field: (field_identifier) @call.name)) @call
(call_expression function: (scoped_identifier name: (identifier) @call.name)) @call
(call_expression function: (generic_function function: (identifier) @call.name)) @call
(struct_expression name: (type_identifier) @call.name) @call
(field_declaration_list (field_declaration name: (field_identifier) @name) @definition.property)
(impl_item trait: (type_identifier) @heritage.trait type: (type_identifier) @heritage.class) @heritage
(impl_item trait: (generic_type type: (type_identifier) @heritage.trait) type: (type_identifier) @heritage.class) @heritage
(impl_item trait: (type_identifier) @heritage.trait type: (generic_type type: (type_identifier) @heritage.class)) @heritage
(impl_item trait: (generic_type type: (type_identifier) @heritage.trait) type: (generic_type type: (type_identifier) @heritage.class)) @heritage
(assignment_expression left: (field_expression value: (_) @assignment.receiver field: (field_identifier) @assignment.property) right: (_)) @assignment
(call_expression function: (scoped_identifier name: (identifier) @_fn (#match? @_fn "^(spawn|spawn_blocking)$")) arguments: (arguments (call_expression function: (identifier) @spawn.target))) @spawn
(call_expression function: (scoped_identifier name: (identifier) @_fn (#match? @_fn "^(spawn|spawn_blocking)$")) arguments: (arguments (call_expression function: (field_expression field: (field_identifier) @spawn.target)))) @spawn
(call_expression function: (scoped_identifier name: (identifier) @_fn (#match? @_fn "^(spawn|spawn_blocking)$")) arguments: (arguments (call_expression function: (scoped_identifier name: (identifier) @spawn.target)))) @spawn
(call_expression arguments: (arguments (identifier) @delegate.target)) @delegate

``````

