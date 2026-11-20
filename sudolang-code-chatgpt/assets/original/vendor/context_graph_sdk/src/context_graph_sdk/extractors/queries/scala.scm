; Production extraction query set for scala
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
(class_definition name: (identifier) @name) @definition.class
(object_definition name: (identifier) @name) @definition.class
(trait_definition name: (identifier) @name) @definition.interface
(enum_definition name: (identifier) @name) @definition.enum
(function_definition name: (identifier) @name) @definition.function
(type_definition name: (type_identifier) @name) @definition.type
(val_declaration name: (identifier) @name) @definition.property
(var_declaration name: (identifier) @name) @definition.property
(full_enum_case name: (identifier) @name) @definition.const
(simple_enum_case name: (identifier) @name) @definition.const
(import_declaration path: (_) @import.source) @import
(call_expression function: (identifier) @call.name) @call
(call_expression function: (field_expression field: (identifier) @call.name)) @call
(class_definition name: (identifier) @heritage.class (extends_clause (type_identifier) @heritage.extends)) @heritage
(trait_definition name: (identifier) @heritage.class (extends_clause (type_identifier) @heritage.extends)) @heritage
(object_definition name: (identifier) @heritage.class (extends_clause (type_identifier) @heritage.extends)) @heritage
