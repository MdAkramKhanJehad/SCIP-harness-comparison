; Production extraction query set for java
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
(enum_declaration name: (identifier) @name) @definition.enum
(annotation_type_declaration name: (identifier) @name) @definition.annotation
(method_declaration name: (identifier) @name) @definition.method
(constructor_declaration name: (identifier) @name) @definition.constructor
(field_declaration declarator: (variable_declarator name: (identifier) @name)) @definition.property
(import_declaration (_) @import.source) @import
(method_invocation name: (identifier) @call.name) @call
(method_invocation object: (_) name: (identifier) @call.name) @call
(object_creation_expression type: (type_identifier) @call.name) @call
(class_declaration name: (identifier) @heritage.class (superclass (type_identifier) @heritage.extends)) @heritage
(class_declaration name: (identifier) @heritage.class (super_interfaces (type_list (type_identifier) @heritage.implements))) @heritage.impl
(assignment_expression left: (field_access object: (_) @assignment.receiver field: (identifier) @assignment.property) right: (_)) @assignment
(method_invocation name: (identifier) @_fn (#match? @_fn "^(submit|execute|start)$") arguments: (argument_list (identifier) @spawn.target)) @spawn
(method_invocation name: (identifier) @_fn (#match? @_fn "^(submit|execute|start)$") arguments: (argument_list (method_reference) @spawn.target)) @spawn
(method_reference (identifier) @call.name) @call
(method_reference . (type_identifier) @call.receiver "::" (identifier) @call.name) @call
(method_invocation arguments: (argument_list (identifier) @delegate.target)) @delegate
