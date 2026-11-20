# pyproject.toml

Role: repository/build/operating context, outside scan execution.

Exact source asset: `assets/original/pyproject.toml`. SHA-256 `ad50806ee200b9c1cc2dc28cbf65cadaaa581b0057d97426fb60d07605947e68`.

```sudo
// Source: pyproject.toml:1-163
Preserve this resource's exact nested keys, list order, scalar values and text from its source asset.
Interpretation belongs to its linked source loader; this record does not add an execution stage.
For queries, preserve the original query grammar as data rather than inventing SudoLang query syntax.
For examples, no loaded/active status is assumed.
```

Parsed values (without environment expansion or overlay):

| Key | Value |
|---|---|
| build-system.requires | ["setuptools>=84.0.0,<85"] |
| build-system.build-backend | "setuptools.build_meta" |
| project.name | "vvaharness" |
| project.version | "1.5.1" |
| project.description | "Visa's open-source harness for autonomous vulnerability discovery and validation, using large language models" |
| project.readme | "README.md" |
| project.requires-python | ">=3.11" |
| project.license | "Apache-2.0" |
| project.dependencies | ["pydantic>=2.13.5,<3", "pydantic-settings>=2.15.0,<3", "PyYAML>=6.0.3,<7", "anthropic>=1.11.0,<2.0", "openai>=3.22.1,<4", "httpx>=0.28.1,<1", "httpx2>=2.13.1,<3", "urllib3>=2.8.0,<3", "python-dotenv>=1.2.4,<2", "structlog>=25.1.0,<27", "typer>=0.15.0,<1", "rich>=13.9.0,<15", "typing_extensions>=4.16.0,<5", "claude-agent-sdk>=0.2.163,<0.3", "tree-sitter==0.25.2", "tree-sitter-language-pack==1.15.8", "arcadedb-embedded==26.10.1", "tree-sitter-go==0.25.0", "tree-sitter-python==0.25.0", "tree-sitter-javascript==0.25.0", "tree-sitter-typescript==0.23.2", "tree-sitter-java==0.23.5", "tree-sitter-c-sharp==0.23.5", "tree-sitter-scala==0.26.2", "tree-sitter-c==0.24.2", "tree-sitter-cpp==0.23.4", "tree-sitter-rust==0.24.2", "tree-sitter-ruby==0.23.1", "tree-sitter-php==0.24.1", "tree-sitter-swift==0.7.3", "tree-sitter-dart==0.1.0", "tree-sitter-solidity==1.2.13", "deepagents>=0.7.21,<0.8; python_version >= '3.11'", "langchain>=1.4.3,<2", "langchain-anthropic>=1.7.5,<2", "langchain-openai>=1.6.7,<2", "langgraph>=1.2.12,<2"] |
| project.optional-dependencies.dev | ["pytest>=9.1.1,<10", "pyflakes>=4.0.1,<5", "ruff>=0.16.9,<0.17", "pyright>=1.1.414,<2", "jsonschema>=4.26.0,<5"] |
| project.scripts.vvaharness | "vvaharness.cli:main" |
| tool.setuptools.packages.find.where | [".", "vendor/context_graph_sdk/src"] |
| tool.setuptools.packages.find.include | ["vvaharness*", "context_graph_sdk*"] |
| tool.setuptools.package-data.context_graph_sdk | ["py.typed", "extractors/queries/*.scm"] |
| tool.setuptools.package-data.vvaharness | ["py.typed", "config/profiles/*.yaml", "exploit_verification/payloads/templates/*.yaml", "rules/generic.kb.yaml", "rules/README.md", "sdk/README.md", "validation/hints/*.yaml", "validation/prompts/*.md", "validation/subagents/*.md", "validation/claude_config/**/*", "skills/*/SKILL.md", "skills/*/probe.sh"] |
| tool.setuptools.data-files.share/vvaharness/rules | ["inputs/remediation_policy.yaml", "inputs/remediation_playbook.yaml"] |
| tool.pytest.ini_options.testpaths | ["tests"] |
| tool.pyright.include | ["vvaharness/validation", "vvaharness/backends/harness", "vvaharness/models", "vvaharness/remediation_agent", "vvaharness/detect", "vvaharness/codegraph", "vvaharness/api.py", "vvaharness/orchestrator/artifacts.py", "vvaharness/orchestrator/case_ids.py", "vvaharness/orchestrator/findings_json.py", "vvaharness/util/pricing.py", "vvaharness/util/stage_telemetry.py"] |
| tool.pyright.venvPath | "." |
| tool.pyright.venv | ".venv" |
| tool.pyright.pythonVersion | "3.11" |
| tool.pyright.typeCheckingMode | "standard" |
| tool.pyright.reportMissingImports | true |
| tool.pyright.reportMissingTypeStubs | false |
| tool.pyright.reportPrivateUsage | false |
