# vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/__init__.py.evidence.json`. SHA-256: `d55a19465ece7bab595e773d9f5f811e37acfb53777d47c54f644faf7ad99918`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/__init__.py:15-26
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from .cpp import load_vcpkg_dependencies; preserve alias and import-time effects. Then Resolve source import from .dotnet import load_csproj_dependencies, load_solution_manifests; preserve alias and import-time effects. Then Resolve source import from .golang import load_go_dependencies, load_go_manifests; preserve alias and import-time effects. Then Resolve source import from .jvm import load_gradle_build_dependencies, load_gradle_lockfile_dependencies, load_gradle_settings_manifests, load_pom_dependencies, load_pom_manifests; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/__init__.py:27-39
In source order: Resolve source import from .makefile import load_makefile_processes; preserve alias and import-time effects. Then Resolve source import from .node import load_package_json_dependencies, load_package_json_manifests, load_pnpm_workspace_manifests; preserve alias and import-time effects. Then Resolve source import from .php import load_composer_dependencies; preserve alias and import-time effects. Then Resolve source import from .python_pkg import load_pyproject_dependencies, load_pyproject_manifests, load_requirements_dependencies; preserve alias and import-time effects. Then Resolve source import from .resolution_config import load_resolution_settings; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/__init__.py:40-71
In source order: Resolve source import from .ruby import load_gemfile_dependencies; preserve alias and import-time effects. Then Resolve source import from .rust import load_cargo_dependencies, load_cargo_manifests; preserve alias and import-time effects. Then Resolve source import from .sbt import load_sbt_dependencies; preserve alias and import-time effects. Then Resolve source import from .swift import load_swift_package_dependencies, load_swift_package_manifests; preserve alias and import-time effects. Then Evaluate once (load_go_dependencies, load_package_json_dependencies, load_cargo_dependencies, load_requirements_dependencies, load_composer_dependencies, load_gemfile_dependencies, load_csproj_dependencies, load_swift_package_dependencies, load_pom_dependencies, load_gradle_lockfile_dependencies, load_gradle_build_dependencies, load_vcpkg_dependencies, load_pyproject_dependencies, load_sbt_dependencies, load_makefile_processes, load_go_manifests, load_package_json_manifests, load_pnpm_workspace_manifests, load_pom_manifests, load_cargo_manifests, load_pyproject_manifests, load_gradle_settings_manifests, load_solution_manifests, load_swift_package_manifests, load_resolution_settings); assign in source target order to ALL_LOADERS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/__init__.py:73-73
In source order: Evaluate once ['ALL_LOADERS']; assign in source target order to __all__.
```

## Local import links

- `from .cpp import load_vcpkg_dependencies` at source line 17: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/cpp.py.sudo.md`.
- `from .dotnet import load_csproj_dependencies, load_solution_manifests` at source line 18: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/dotnet.py.sudo.md`.
- `from .golang import load_go_dependencies, load_go_manifests` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/golang.py.sudo.md`.
- `from .jvm import load_gradle_build_dependencies, load_gradle_lockfile_dependencies, load_gradle_settings_manifests, load_pom_dependencies, load_pom_manifests` at source line 20: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/jvm.py.sudo.md`.
- `from .makefile import load_makefile_processes` at source line 27: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/makefile.py.sudo.md`.
- `from .node import load_package_json_dependencies, load_package_json_manifests, load_pnpm_workspace_manifests` at source line 28: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/node.py.sudo.md`.
- `from .php import load_composer_dependencies` at source line 33: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/php.py.sudo.md`.
- `from .python_pkg import load_pyproject_dependencies, load_pyproject_manifests, load_requirements_dependencies` at source line 34: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/python_pkg.py.sudo.md`.
- `from .resolution_config import load_resolution_settings` at source line 39: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/resolution_config.py.sudo.md`.
- `from .ruby import load_gemfile_dependencies` at source line 40: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/ruby.py.sudo.md`.
- `from .rust import load_cargo_dependencies, load_cargo_manifests` at source line 41: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/rust.py.sudo.md`.
- `from .sbt import load_sbt_dependencies` at source line 42: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/sbt.py.sudo.md`.
- `from .swift import load_swift_package_dependencies, load_swift_package_manifests` at source line 43: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/project/manifests/swift.py.sudo.md`.
