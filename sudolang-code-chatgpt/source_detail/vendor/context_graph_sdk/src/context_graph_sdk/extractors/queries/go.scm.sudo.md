# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/go.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/go.scm`. SHA-256 `d87d1119eed0559f44d0e78b94d6b28526b0d83b10210a9f64b4a8672af9c54f`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/go.scm:1-29
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for go
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
(function_declaration name: (identifier) @name) @definition.function
(method_declaration name: (field_identifier) @name) @definition.method
(type_declaration (type_spec name: (type_identifier) @name type: (struct_type))) @definition.struct
(type_declaration (type_spec name: (type_identifier) @name type: (interface_type))) @definition.interface
(type_declaration (type_spec name: (type_identifier) @name)) @definition.type
(import_declaration (import_spec name: (package_identifier) @import.alias path: (interpreted_string_literal) @import.source)) @import
(import_declaration (import_spec_list (import_spec name: (package_identifier) @import.alias path: (interpreted_string_literal) @import.source))) @import
(import_declaration (import_spec !name path: (interpreted_string_literal) @import.source)) @import
(import_declaration (import_spec_list (import_spec !name path: (interpreted_string_literal) @import.source))) @import
(field_declaration_list (field_declaration name: (field_identifier) @name) @definition.property)
(call_expression function: (identifier) @call.name) @call
(call_expression function: (selector_expression operand: (_) @call.receiver field: (field_identifier) @call.name)) @call
(composite_literal type: (type_identifier) @call.name) @call
(type_declaration (type_spec name: (type_identifier) @heritage.class type: (struct_type (field_declaration_list (field_declaration !name type: (type_identifier) @heritage.extends))))) @heritage
(assignment_statement left: (expression_list (selector_expression operand: (_) @assignment.receiver field: (field_identifier) @assignment.property)) right: (_)) @assignment
(go_statement (call_expression function: (identifier) @spawn.name)) @spawn
(go_statement (call_expression function: (selector_expression operand: (_) @spawn.receiver field: (field_identifier) @spawn.name))) @spawn
(call_expression arguments: (argument_list (identifier) @delegate.target)) @delegate

``````

