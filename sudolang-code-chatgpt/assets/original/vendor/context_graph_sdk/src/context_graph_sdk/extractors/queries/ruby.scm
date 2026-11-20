; Production extraction query set for ruby
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
(class name: (constant) @name) @definition.class
(module name: (constant) @name) @definition.module
(method name: (identifier) @name) @definition.method
(singleton_method name: (identifier) @name) @definition.function
(call method: (identifier) @call.name) @call
(class name: (constant) @heritage.class superclass: (superclass (constant) @heritage.extends)) @heritage
(call method: (identifier) @_fn (#match? @_fn "^(include|extend|prepend)$") arguments: (argument_list (constant) @heritage.extends)) @heritage
(call method: (identifier) @_fn (#match? @_fn "^(attr_accessor|attr_reader|attr_writer)$") arguments: (argument_list (simple_symbol) @name)) @definition.property
(call receiver: (constant) @_recv (#eq? @_recv "Thread") method: (identifier) @_fn (#eq? @_fn "new")) @spawn
(call arguments: (argument_list (identifier) @delegate.target)) @delegate
