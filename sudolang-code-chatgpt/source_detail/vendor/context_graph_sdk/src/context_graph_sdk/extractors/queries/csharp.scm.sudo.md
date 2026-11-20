# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/csharp.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/csharp.scm`. SHA-256 `7bcf69e1ee16774225b6dd577b70b0ffbd87253e2dbc0f14712ea208c600fec4`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/csharp.scm:1-39
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for csharp
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
(interface_declaration name: (identifier) @name) @definition.interface
(struct_declaration name: (identifier) @name) @definition.struct
(enum_declaration name: (identifier) @name) @definition.enum
(record_declaration name: (identifier) @name) @definition.record
(delegate_declaration name: (identifier) @name) @definition.delegate
(namespace_declaration name: (identifier) @name) @definition.namespace
(namespace_declaration name: (qualified_name) @name) @definition.namespace
(file_scoped_namespace_declaration name: (identifier) @name) @definition.namespace
(file_scoped_namespace_declaration name: (qualified_name) @name) @definition.namespace
(method_declaration name: (identifier) @name) @definition.method
(local_function_statement name: (identifier) @name) @definition.function
(constructor_declaration name: (identifier) @name) @definition.constructor
(using_directive (qualified_name) @import.source) @import
(using_directive (identifier) @import.source) @import
(invocation_expression function: (identifier) @call.name) @call
(invocation_expression function: (member_access_expression name: (identifier) @call.name)) @call
(invocation_expression function: (conditional_access_expression (member_binding_expression name: (identifier) @call.name))) @call
(object_creation_expression type: (identifier) @call.name) @call
(implicit_object_creation_expression) @call
(class_declaration name: (identifier) @heritage.class (base_list (identifier) @heritage.extends)) @heritage
(class_declaration name: (identifier) @heritage.class (base_list (generic_name (identifier) @heritage.extends))) @heritage
(interface_declaration name: (identifier) @heritage.class (base_list (identifier) @heritage.extends)) @heritage
(struct_declaration name: (identifier) @heritage.class (base_list (identifier) @heritage.extends)) @heritage
(property_declaration name: (identifier) @name) @definition.property
(assignment_expression left: (member_access_expression expression: (_) @assignment.receiver name: (identifier) @assignment.property) right: (_)) @assignment
(invocation_expression function: (member_access_expression name: (identifier) @_fn (#match? @_fn "^(Run|StartNew|QueueUserWorkItem)$"))) @spawn
(invocation_expression arguments: (argument_list (argument (identifier) @delegate.target))) @delegate

``````

