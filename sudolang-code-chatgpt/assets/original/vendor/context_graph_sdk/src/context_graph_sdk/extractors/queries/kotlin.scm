; Production extraction query set for kotlin
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
(class_declaration (type_identifier) @name) @definition.class
(object_declaration (type_identifier) @name) @definition.class
(companion_object (type_identifier) @name) @definition.class
(enum_entry (simple_identifier) @name) @definition.const
(type_alias (type_identifier) @name) @definition.type
(function_declaration (simple_identifier) @name) @definition.function
(secondary_constructor) @definition.constructor
(import_header (identifier) @import.source) @import
(call_expression (simple_identifier) @call.name) @call
(call_expression (navigation_expression (simple_identifier) @call.name)) @call
(constructor_invocation (user_type (type_identifier) @call.name)) @call
(class_declaration (type_identifier) @heritage.class (delegation_specifier (user_type (type_identifier) @heritage.extends))) @heritage
(class_declaration (type_identifier) @heritage.class (delegation_specifier (constructor_invocation (user_type (type_identifier) @heritage.extends)))) @heritage
(property_declaration (variable_declaration (simple_identifier) @name)) @definition.property
(call_expression (simple_identifier) @_fn (#match? @_fn "^(launch|async)$")) @spawn
(call_expression (navigation_expression (simple_identifier) @_fn (#match? @_fn "^(launch|async)$"))) @spawn
