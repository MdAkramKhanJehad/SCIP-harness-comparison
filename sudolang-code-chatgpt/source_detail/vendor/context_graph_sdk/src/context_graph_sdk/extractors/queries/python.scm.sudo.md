# vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/python.scm

Role: Tree-sitter matching query, data for vendored extractor.

Exact source asset: `assets/original/vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/python.scm`. SHA-256 `c13e9d997307059cb9ecd7f2af6dd03fde2811bd4fa3d5faa2b88da54b124adc`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/queries/python.scm:1-32
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
; Production extraction query set for python
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
(function_definition name: (identifier) @name) @definition.function
(class_definition body: (block (function_definition name: (identifier) @name) @definition.method))
(class_definition body: (block (decorated_definition definition: (function_definition name: (identifier) @name)) @definition.method))
(class_definition body: (block (expression_statement (assignment left: (identifier) @name)) @definition.property))
(class_definition body: (block (expression_statement (assignment left: (identifier) @name type: (_) right: (_)?)) @definition.property))
(import_statement name: (dotted_name) @import.source) @import
(import_from_statement module_name: (dotted_name) @import.source) @import
(import_from_statement module_name: (relative_import) @import.source) @import
(call function: (identifier) @call.name) @call
(call function: (attribute attribute: (identifier) @call.name)) @call
(class_definition name: (identifier) @heritage.class superclasses: (argument_list (identifier) @heritage.extends)) @heritage
(assignment left: (attribute object: (_) @assignment.receiver attribute: (identifier) @assignment.property) right: (_)) @assignment
(augmented_assignment left: (attribute object: (_) @assignment.receiver attribute: (identifier) @assignment.property) right: (_)) @assignment
(call function: (attribute attribute: (identifier) @_fn (#match? @_fn "^(Thread|Process)$")) arguments: (argument_list (keyword_argument name: (identifier) @_kw (#eq? @_kw "target") value: (identifier) @spawn.target))) @spawn
(call function: (attribute attribute: (identifier) @_fn (#match? @_fn "^(create_task|ensure_future)$")) arguments: (argument_list (call function: (identifier) @spawn.target))) @spawn
(call function: (attribute attribute: (identifier) @_fn (#match? @_fn "^(create_task|ensure_future)$")) arguments: (argument_list (call function: (attribute attribute: (identifier) @spawn.target)))) @spawn
(call function: (attribute attribute: (identifier) @_fn (#match? @_fn "^(run|run_until_complete)$")) arguments: (argument_list (call function: (identifier) @spawn.target))) @spawn
(call function: (identifier) @_fn (#eq? @_fn "run_in_threadpool") arguments: (argument_list (identifier) @spawn.target)) @spawn
(call function: (attribute attribute: (identifier) @_fn (#eq? @_fn "submit")) arguments: (argument_list (identifier) @spawn.target)) @spawn
(call arguments: (argument_list (identifier) @delegate.target)) @delegate

``````

