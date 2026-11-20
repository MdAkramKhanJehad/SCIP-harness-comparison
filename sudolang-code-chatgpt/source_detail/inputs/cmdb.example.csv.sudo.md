# inputs/cmdb.example.csv

Role: configuration/policy/rules/input data; loader controls interpretation.

Exact source asset: `assets/original/inputs/cmdb.example.csv`. SHA-256 `96a6a87a6e784084cca9d221c602b530cba3aa4c72b5fc5fc3f3137a9adf4c06`.

```sudo
// Source: inputs/cmdb.example.csv:1-19
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

id,name,externally_facing,pci,pan,pii,parent_id
0000001,example-public-payments-api,Yes,No,Yes,Yes,
0000002,example-backend-batch-service,No,yes,No,No,
0000003,example-marketing-site,Yes,yes,No,No,
0000004,example-card-tokenization-component,,,,,0000001

``````

