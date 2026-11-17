; Production extraction query set for php
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
(namespace_definition name: (namespace_name) @name) @definition.namespace
(class_declaration name: (name) @name) @definition.class
(interface_declaration name: (name) @name) @definition.interface
(trait_declaration name: (name) @name) @definition.trait
(enum_declaration name: (name) @name) @definition.enum
(function_definition name: (name) @name) @definition.function
(method_declaration name: (name) @name) @definition.method
(namespace_use_declaration (namespace_use_clause (qualified_name) @import.source)) @import
(function_call_expression function: (name) @call.name) @call
(member_call_expression name: (name) @call.name) @call
(nullsafe_member_call_expression name: (name) @call.name) @call
(scoped_call_expression name: (name) @call.name) @call
(object_creation_expression (name) @call.name) @call
(class_declaration name: (name) @heritage.class (base_clause [(name) (qualified_name)] @heritage.extends)) @heritage
(class_declaration name: (name) @heritage.class (class_interface_clause [(name) (qualified_name)] @heritage.implements)) @heritage.impl
(class_declaration name: (name) @heritage.class body: (declaration_list (use_declaration [(name) (qualified_name)] @heritage.trait))) @heritage
(property_declaration (property_element (variable_name (name) @name))) @definition.property
(assignment_expression left: (member_access_expression object: (_) @assignment.receiver name: (name) @assignment.property) right: (_)) @assignment
(function_call_expression function: (name) @_fn (#eq? @_fn "pcntl_fork")) @spawn
