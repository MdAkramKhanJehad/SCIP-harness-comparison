# vendor/context_graph_sdk/pyproject.toml

Role: repository/build/operating context, outside scan execution.

Exact source asset: `assets/original/vendor/context_graph_sdk/pyproject.toml`. SHA-256 `8fcfaa16a8480325a401120f8edbd72df611b1c09edf9f95eeea62fb21ed6a21`.

```sudo
// Source: vendor/context_graph_sdk/pyproject.toml:1-94
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| build-system.requires | ["setuptools>=77"] |
| build-system.build-backend | "setuptools.build_meta" |
| project.name | "context-graph-sdk" |
| project.version | "0.1.0" |
| project.description | "Python-native code graph SDK" |
| project.readme | "README.md" |
| project.license | "Apache-2.0" |
| project.license-files | ["LICENSE"] |
| project.requires-python | ">=3.11" |
| project.keywords | ["code-graph", "cypher", "sdk"] |
| project.classifiers | ["Development Status :: 2 - Pre-Alpha", "Programming Language :: Python :: 3", "Programming Language :: Python :: 3.11", "Programming Language :: Python :: 3.12", "Typing :: Typed"] |
| project.dependencies | ["arcadedb-embedded==26.10.1", "tree-sitter==0.25.2", "tree-sitter-go==0.25.0", "tree-sitter-python==0.25.0", "tree-sitter-javascript==0.25.0", "tree-sitter-typescript==0.23.2", "tree-sitter-java==0.23.5", "tree-sitter-c-sharp==0.23.5", "tree-sitter-scala==0.26.2", "tree-sitter-c==0.24.2", "tree-sitter-cpp==0.23.4", "tree-sitter-rust==0.24.2", "tree-sitter-ruby==0.23.1", "tree-sitter-php==0.24.1", "tree-sitter-swift==0.7.3", "tree-sitter-dart==0.1.0", "tree-sitter-solidity==1.2.13", "tree-sitter-language-pack==1.15.8"] |
| project.optional-dependencies.mcp | ["mcp>=1.30,<2"] |
| dependency-groups.dev | ["mcp>=1.30,<2", "pyright>=1.1.400", "pytest>=8.3", "ruff>=0.11"] |
| tool.setuptools.packages.find.where | ["src"] |
| tool.setuptools.packages.find.include | ["context_graph_sdk*"] |
| tool.setuptools.package-data.context_graph_sdk | ["py.typed", "extractors/queries/*.scm"] |
| tool.ruff.target-version | "py311" |
| tool.ruff.line-length | 100 |
| tool.ruff.exclude | [".venv", "**/.venv"] |
| tool.ruff.lint.select | ["E", "F", "I", "UP", "B", "SIM", "RUF"] |
| tool.pyright.include | ["src", "tests", "example"] |
| tool.pyright.exclude | [".venv", "**/.venv"] |
| tool.pyright.pythonVersion | "3.11" |
| tool.pyright.typeCheckingMode | "strict" |
| tool.pytest.ini_options.testpaths | ["tests"] |
| tool.pytest.ini_options.addopts | "-q" |
