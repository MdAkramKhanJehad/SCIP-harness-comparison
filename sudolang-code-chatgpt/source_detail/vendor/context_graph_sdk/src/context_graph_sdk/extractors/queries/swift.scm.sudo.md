# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/swift.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/swift.scm`. SHA-256 `b9673bce704ee151a42a069e992af7df49d8cf2633bb06d58434c50574fbf6ff`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/swift.scm:1-29
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for swift
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
(class_declaration "class" name: (type_identifier) @name) @definition.class
(class_declaration "struct" name: (type_identifier) @name) @definition.struct
(class_declaration "enum" name: (type_identifier) @name) @definition.enum
(class_declaration "extension" name: (user_type (type_identifier) @name)) @definition.class
(class_declaration "actor" name: (type_identifier) @name) @definition.class
(protocol_declaration name: (type_identifier) @name) @definition.interface
(typealias_declaration name: (type_identifier) @name) @definition.type
(function_declaration name: (simple_identifier) @name) @definition.function
(protocol_function_declaration name: (simple_identifier) @name) @definition.method
(init_declaration) @definition.constructor
(property_declaration (pattern (simple_identifier) @name)) @definition.property
(import_declaration (identifier (simple_identifier) @import.source)) @import
(call_expression (simple_identifier) @call.name) @call
(call_expression (navigation_expression (navigation_suffix (simple_identifier) @call.name))) @call
(class_declaration name: (type_identifier) @heritage.class (inheritance_specifier inherits_from: (user_type (type_identifier) @heritage.extends))) @heritage
(protocol_declaration name: (type_identifier) @heritage.class (inheritance_specifier inherits_from: (user_type (type_identifier) @heritage.extends))) @heritage
(class_declaration "extension" name: (user_type (type_identifier) @heritage.class) (inheritance_specifier inherits_from: (user_type (type_identifier) @heritage.extends))) @heritage
(call_expression (simple_identifier) @_fn (#eq? @_fn "Task")) @spawn

``````

