# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/javascript.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/javascript.scm`. SHA-256 `65bbfc05f609be70ad055ddb4e81575322089000a4674f3ba000ce97fb0c3709`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/javascript.scm:1-31
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for javascript
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
(class_declaration name: (identifier) @name) @definition.class
(function_declaration name: (identifier) @name) @definition.function
(method_definition name: (property_identifier) @name) @definition.method
(lexical_declaration (variable_declarator name: (identifier) @name value: (arrow_function))) @definition.function
(lexical_declaration (variable_declarator name: (identifier) @name value: (function_expression))) @definition.function
(export_statement declaration: (lexical_declaration (variable_declarator name: (identifier) @name value: (arrow_function)))) @definition.function
(export_statement declaration: (lexical_declaration (variable_declarator name: (identifier) @name value: (function_expression)))) @definition.function
(import_statement source: (string) @import.source) @import
(export_statement source: (string) @import.source) @import
(call_expression function: (identifier) @call.name) @call
(call_expression function: (member_expression property: (property_identifier) @call.name)) @call
(new_expression constructor: (identifier) @call.name) @call
(field_definition property: (property_identifier) @name) @definition.property
(class_declaration name: (identifier) @heritage.class (class_heritage (identifier) @heritage.extends)) @heritage
(assignment_expression left: (member_expression object: (_) @assignment.receiver property: (property_identifier) @assignment.property) right: (_)) @assignment
(augmented_assignment_expression left: (member_expression object: (_) @assignment.receiver property: (property_identifier) @assignment.property) right: (_)) @assignment
(call_expression function: (identifier) @_fn (#match? @_fn "^(setTimeout|setInterval|queueMicrotask|setImmediate)$") arguments: (arguments (identifier) @spawn.target)) @spawn
(call_expression function: (identifier) @_fn (#match? @_fn "^(setTimeout|setInterval|queueMicrotask|setImmediate)$") arguments: (arguments (member_expression property: (property_identifier) @spawn.target))) @spawn
(new_expression constructor: (identifier) @_ctor (#eq? @_ctor "Worker")) @spawn
(call_expression arguments: (arguments (identifier) @delegate.target)) @delegate

``````

