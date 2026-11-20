# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/solidity.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/solidity.scm`. SHA-256 `318e90b19b49fade226f4e1d43899c7a55d2f4a826c436358b5bdf8cf6beb310`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/solidity.scm:1-34
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for solidity
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
(contract_declaration name: (identifier) @name) @definition.class
(interface_declaration name: (identifier) @name) @definition.interface
(library_declaration name: (identifier) @name) @definition.class
(function_definition name: (identifier) @name) @definition.function
(constructor_definition "constructor" @name) @definition.constructor
(fallback_receive_definition "receive" @name) @definition.method
(fallback_receive_definition "fallback" @name) @definition.method
(modifier_definition name: (identifier) @name) @definition.method
(event_definition name: (identifier) @name) @definition.event
(error_declaration name: (identifier) @name) @definition.error
(struct_declaration name: (identifier) @name) @definition.struct
(enum_declaration name: (identifier) @name) @definition.enum
(state_variable_declaration "constant" name: (identifier) @name) @definition.constant
(state_variable_declaration name: (identifier) @name) @definition.property
(constant_variable_declaration name: (identifier) @name) @definition.constant
(import_directive source: (string) @import.source) @import
(contract_declaration name: (identifier) @heritage.class (inheritance_specifier ancestor: (_) @heritage.extends)) @heritage
(interface_declaration name: (identifier) @heritage.class (inheritance_specifier ancestor: (_) @heritage.implements)) @heritage.impl
(call_expression . (expression (identifier) @call.name)) @call
(call_expression . (_ (member_expression property: (identifier) @call.name))) @call
(modifier_invocation (identifier) @call.name) @call
(assignment_expression (expression (identifier) @assignment.property) (_)) @assignment
(assignment_expression (expression (member_expression property: (identifier) @assignment.property)) (_)) @assignment

``````

