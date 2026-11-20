# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/c.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/c.scm`. SHA-256 `8c4f84456168ef9180502c969ea7d5a2fad5ff5c65667b927a8b1e81fba2b1ba`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/c.scm:1-31
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for c
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
(function_definition declarator: (function_declarator declarator: (identifier) @name)) @definition.function
(declaration declarator: (function_declarator declarator: (identifier) @name)) @definition.function
(function_definition declarator: (pointer_declarator declarator: (function_declarator declarator: (identifier) @name))) @definition.function
(declaration declarator: (pointer_declarator declarator: (function_declarator declarator: (identifier) @name))) @definition.function
(function_definition declarator: (pointer_declarator declarator: (pointer_declarator declarator: (function_declarator declarator: (identifier) @name)))) @definition.function
(struct_specifier name: (type_identifier) @name body: (field_declaration_list)) @definition.struct
(struct_specifier name: (type_identifier) @name) @definition.struct
(enum_specifier name: (type_identifier) @name body: (enumerator_list)) @definition.enum
(enum_specifier name: (type_identifier) @name) @definition.enum
(type_definition declarator: (type_identifier) @name) @definition.typedef
(union_specifier name: (type_identifier) @name body: (field_declaration_list)) @definition.union
(union_specifier name: (type_identifier) @name) @definition.union
(preproc_include path: (_) @import.source) @import
(call_expression function: (identifier) @call.name) @call
(call_expression function: (field_expression field: (field_identifier) @call.name)) @call
(preproc_function_def name: (identifier) @name) @definition.macro
(preproc_def name: (identifier) @name) @definition.macro
(assignment_expression left: (field_expression argument: (_) @assignment.receiver field: (field_identifier) @assignment.property) right: (_)) @assignment
(call_expression function: (identifier) @_fn (#eq? @_fn "pthread_create") arguments: (argument_list (_) (_) (identifier) @spawn.target)) @spawn
(call_expression arguments: (argument_list (identifier) @delegate.target)) @delegate

``````

