# vendor/context_graph_sdk/src/context_graph_sdk/discovery/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/discovery/__init__.py.evidence.json`. SHA-256: `aa511e8201001c13d4fc3819473c73df4da9f0bc026ae1a9d2092dc749f9af1a`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/__init__.py:15-40
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from .ignore import DEFAULT_IGNORE_PATTERNS, GitIgnoreMatcher, parse_ignore_lines; preserve alias and import-time effects. Then Resolve source import from .languages import detect_language, is_documentation_file; preserve alias and import-time effects. Then Resolve source import from .walker import DEFAULT_MAX_FILE_BYTES, DOCUMENTATION_CONTENT_BYTES, RepositoryWalk, WalkedFile, read_documentation_text, walk_repository; preserve alias and import-time effects. Then Evaluate once ['DEFAULT_IGNORE_PATTERNS', 'DEFAULT_MAX_FILE_BYTES', 'DOCUMENTATION_CONTENT_BYTES', 'GitIgnoreMatcher', 'RepositoryWalk', 'WalkedFile', 'detect_language', 'is_documentation_file', 'parse_ignore_lines', 'read_documentation_text', 'walk_repository']; assign in source target order to __all__.
```

## Local import links

- `from .ignore import DEFAULT_IGNORE_PATTERNS, GitIgnoreMatcher, parse_ignore_lines` at source line 17: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/ignore.py.sudo.md`.
- `from .languages import detect_language, is_documentation_file` at source line 18: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py.sudo.md`.
- `from .walker import DEFAULT_MAX_FILE_BYTES, DOCUMENTATION_CONTENT_BYTES, RepositoryWalk, WalkedFile, read_documentation_text, walk_repository` at source line 19: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/discovery/walker.py.sudo.md`.
