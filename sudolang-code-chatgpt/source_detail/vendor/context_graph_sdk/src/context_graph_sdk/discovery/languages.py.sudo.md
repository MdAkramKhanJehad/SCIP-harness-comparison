# vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py.evidence.json`. SHA-256: `445628c7620f62a2c5141db2b75968f04c4d27713e4aaee1d8180f3b90eb9b34`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:15-64
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then For _NATIVE_EXTENSIONS, assign {'.go': 'go', '.ts': 'typescript', '.tsx': 'tsx', '.js': 'javascript', '.jsx': 'javascript', '.mjs': 'javascript', '.cjs': 'javascript', '.py': 'python', '.java': 'java', '.rs': 'rust', '.cc': 'cpp', '.cpp': 'cpp', '.cxx': 'cpp', '.hpp': 'cpp', '.hh': 'cpp', '.hxx': 'cpp', '.h': 'cpp', '.inl': 'cpp', '.ipp': 'cpp', '.tpp': 'cpp', '.c': 'c', '.rb': 'ruby', '.php': 'php', '.kt': 'kotlin', '.kts': 'kotlin', '.cs': 'csharp', '.scala': 'scala', '.sc': 'scala', '.swift': 'swift', '.dart': 'dart', '.sol': 'solidity'}; source annotation dict[str, str]. Then For _SUPPORTING_BY_FILENAME, assign {'dockerfile': 'dockerfile', 'build.sbt': 'scala', 'build.gradle': 'groovy', 'makefile': 'make', 'gnumakefile': 'make', 'bsdmakefile': 'make'}; source annotation dict[str, str].
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:66-87
In source order: For _SUPPORTING_BY_SUFFIX, assign (('.json', 'json'), ('.yaml', 'yaml'), ('.yml', 'yaml'), ('.toml', 'toml'), ('.hcl', 'hcl'), ('.tf', 'hcl'), ('.tfvars', 'hcl'), ('.sql', 'sql'), ('.proto', 'protobuf'), ('.sh', 'bash'), ('.bash', 'bash'), ('.zsh', 'bash'), ('.bashrc', 'bash'), ('.bash_profile', 'bash'), ('.bash_login', 'bash'), ('.profile', 'bash'), ('.zshrc', 'bash'), ('.zprofile', 'bash')); source annotation tuple[tuple[str, str], ...]. Then Evaluate once frozenset({'makefile', 'gnumakefile', 'bsdmakefile'}); assign in source target order to _MAKEFILE_NAMES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:90-102
// Source signature: detect_language(filename: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_language(filename) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:91-91
  In source order: Evaluate once posixpath.basename(filename.replace('\\', '/')).lower(); assign in source target order to name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:92-93
  if (the source predicate name in _MAKEFILE_NAMES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:93-93
    End this invocation with 'make'.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:94-94
  In source order: Evaluate once posixpath.splitext(name); assign in source target order to (_, extension).
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:95-96
  if (the source predicate (language := _NATIVE_EXTENSIONS.get(extension)) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:96-96
    End this invocation with language.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:97-98
  if (the source predicate (language := _SUPPORTING_BY_FILENAME.get(name)) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:98-98
    End this invocation with language.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:99-101
  for each (suffix, language) in _SUPPORTING_BY_SUFFIX {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:100-101
    if (the source predicate name.endswith(suffix) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:101-101
      End this invocation with language.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:102-102
  End this invocation with ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:105-134
In source order: For _DOC_NAME_PREFIXES, assign ('readme', 'architecture', 'contributing', 'design', 'security', 'code_of_conduct', 'code-of-conduct', 'install', 'usage', 'faq', 'history', 'migration', 'upgrading', 'development', 'hacking', 'quickstart', 'tutorial', 'overview', 'api', 'getting-started', 'getting_started', 'guide'); source annotation tuple[str, ...]. Then Evaluate once frozenset({'doc', 'docs', 'documentation', 'wiki', 'guides', 'handbook', 'manual', 'book'}); assign in source target order to _DOC_DIRECTORY_NAMES. Then Evaluate once frozenset({'.md', '.rst', '.txt', '.adoc', '.org'}); assign in source target order to _DOC_EXTENSIONS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:137-148
// Source signature: is_documentation_file(file_path: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_documentation_file(file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:138-140
  In source order: Evaluate once file_path.replace('\\', '/').lower(); assign in source target order to lowered. Then Evaluate once posixpath.basename(lowered); assign in source target order to base. Then Evaluate once posixpath.splitext(base); assign in source target order to (stem, extension).
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:141-142
  if (the source predicate not extension is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:142-142
    End this invocation with base in _DOC_NAME_PREFIXES.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:143-144
  if (the source predicate extension not in _DOC_EXTENSIONS is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:144-144
    End this invocation with False.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:145-147
  for each prefix in _DOC_NAME_PREFIXES {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:146-147
    if (the source predicate stem == prefix or stem.startswith(prefix + '_') or stem.startswith(prefix + '-') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:147-147
      End this invocation with True.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/discovery/languages.py:148-148
  End this invocation with any((part in _DOC_DIRECTORY_NAMES for part in lowered.split('/')[:-1])).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
