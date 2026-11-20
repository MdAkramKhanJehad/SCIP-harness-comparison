# Dependency and execution boundaries

All supplied non-test Python code is structurally represented, including the
**89 Python modules in `vendor/context_graph_sdk/`**. Its 16 Tree-sitter queries
are retained as exact data resources; its remaining metadata is indexed too.
No supplied source file or SudoLang example was inaccessible.

`import_links.tsv` resolves local module imports statically, including relative
imports; it is not a whole-program call graph. `call_sites.tsv` retains original
callee expressions and enclosing scopes. Dynamic dispatch, monkeypatching,
plugin entry points and runtime-selected implementations remain conditional.
Re-exports are followed through converted package initializers, not assigned
invented targets.

External implementations below are outside the supplied checkout. Their API
calls, arguments, exceptions, retry gates and contracts are represented at call
sites. Their hidden behavior is not inferred.

| Boundary | Available evidence | Unresolved behavior |
|---|---|---|
| DeepAgents, LangChain, LangGraph and integrations | harness adapters/options/middleware and requirements | library-internal scheduling, middleware composition, retries and provider accounting |
| Anthropic, OpenAI, Claude Agent SDK | API/CLI wrappers, schemas and source tool loops | effective runtime versions, service behavior and model decisions |
| Tree-sitter grammars, ArcadeDB embedded | complete vendored extraction/resolution/backend/query-worker code and exact pins | native parser/database implementation and actual extraction/query results |
| Pydantic, PyYAML, httpx/httpx2 and other runtime packages | source fields/validators, loaders, client calls/options | external coercion, serialization and network behavior beyond supplied code |
| Shell/grep/sed/awk/find/python commands | exact scripts, flags, regexes, quotas, heredocs and embedded Python | tool versions, platform behavior, target results and choice to invoke a probe |
| Git, filesystem, subprocesses, clocks, concurrency primitives | exact calls, arguments, lock/context/wait/shutdown scopes | scheduler order beyond explicit waits, process outcomes and actual runtime state |
| Plugins and operator-provided inputs | loader/interfaces, schemas, trust gates and bundled examples | implementations/data supplied only at a future run |

The prior metadata probe found OpenAI 3.49.0, Pydantic 2.14.3 and httpx 0.28.1 in
the **converter interpreter**, and no metadata there for several other required
packages. These are not established harness runtime versions. Installed libraries
in that unrelated environment are not substituted for a missing exact harness
runtime or claimed as supplied dependency code. No project lockfile or project
virtual environment was found at the checked locations. The requirements and
vendored code are represented; unobserved external services remain unresolved.

Model instructions, examples, personas and schema descriptions remain requests
or data. They do not prove a model read every file, completed a pass, invoked a
tool, or produced correct findings. Executable gates—including gates that
relent—validators, score floors, limits, write policies and host synthesis are
represented separately.

No harness scan, exploit request, remediation write, model call or downstream
flaw analysis was performed. Artifact checks are not harness test results.
