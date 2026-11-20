# inputs/known_cves.example.json

Role: configuration/policy/rules/input data; loader controls interpretation.

Exact source asset: `assets/original/inputs/known_cves.example.json`. SHA-256 `acb7861e89f5be862c9a005f76fe427c2526f83f5b1023596cf6e1fad85bcd5a`.

```sudo
// Source: inputs/known_cves.example.json:1-12
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| _license | "Copyright 2026 Visa, Inc. Licensed under the Apache License, Version 2.0 (the \"License\"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 . Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied." |
| cves | [{"id": "CVE-2024-EXAMPLE", "summary": "Heap overflow in parse_header() via crafted Content-Length", "affected_files": ["src/http/parser.c"], "cvss": 8.1, "patched": false}] |
