# inputs/repos.example.csv

Role: configuration/policy/rules/input data; loader controls interpretation.

Exact source asset: `assets/original/inputs/repos.example.csv`. SHA-256 `038a89a1d322c62644d3cc6b29ffdfc8f2cede90450c9b82c4fee44cd92e3599`.

```sudo
// Source: inputs/repos.example.csv:1-18
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

``````text
# Copyright 2026 Visa, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

AppId,RepoName,Path
1,repo1,https://github.com/example-org/repo1.git
2,repo2,https://github.com/example-org/repo2.git
3,repo3,git@github.com:example-org/repo3.git

``````

