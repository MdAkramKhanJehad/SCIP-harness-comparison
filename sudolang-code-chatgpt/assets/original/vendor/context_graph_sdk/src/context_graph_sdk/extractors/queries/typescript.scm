; Production extraction query set for typescript
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
(class_declaration name: (type_identifier) @name) @definition.class
(interface_declaration name: (type_identifier) @name) @definition.interface
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
(public_field_definition name: (property_identifier) @name) @definition.property
(class_declaration name: (type_identifier) @heritage.class (class_heritage (extends_clause value: (identifier) @heritage.extends))) @heritage
(class_declaration name: (type_identifier) @heritage.class (class_heritage (implements_clause (type_identifier) @heritage.implements))) @heritage.impl
(assignment_expression left: (member_expression object: (_) @assignment.receiver property: (property_identifier) @assignment.property) right: (_)) @assignment
(augmented_assignment_expression left: (member_expression object: (_) @assignment.receiver property: (property_identifier) @assignment.property) right: (_)) @assignment
(call_expression function: (identifier) @_fn (#match? @_fn "^(setTimeout|setInterval|queueMicrotask|setImmediate)$") arguments: (arguments (identifier) @spawn.target)) @spawn
(call_expression function: (identifier) @_fn (#match? @_fn "^(setTimeout|setInterval|queueMicrotask|setImmediate)$") arguments: (arguments (member_expression property: (property_identifier) @spawn.target))) @spawn
(new_expression constructor: (identifier) @_ctor (#eq? @_ctor "Worker")) @spawn
(call_expression function: (member_expression property: (property_identifier) @_fn (#eq? @_fn "addEventListener")) arguments: (arguments (_) (identifier) @spawn.target)) @spawn
(call_expression function: (member_expression property: (property_identifier) @_fn (#match? @_fn "^(then|catch|finally)$")) arguments: (arguments (identifier) @delegate.target)) @delegate
(call_expression arguments: (arguments (identifier) @delegate.target)) @delegate
