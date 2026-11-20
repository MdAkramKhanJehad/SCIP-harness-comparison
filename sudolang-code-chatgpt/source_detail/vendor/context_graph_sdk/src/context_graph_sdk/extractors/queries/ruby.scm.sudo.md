# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/ruby.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/ruby.scm`. SHA-256 `c789b43a08d8272a513dc468ae186635c808bd1203f4b47836bae3e3d0794039`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/ruby.scm:1-21
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
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

``````

