# vvaharness/remediation_agent/frameworks.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/remediation_agent/frameworks.py.evidence.json`. SHA-256: `6f5d6d4452034ece17a8d2914a71ece32d997a8b2e6986e4dd0df0f3e406a46e`.

```sudo
// Source: vvaharness/remediation_agent/frameworks.py:15-61
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then For _EXT_LANG, assign {'.py': 'python', '.pyi': 'python', '.java': 'java', '.kt': 'java', '.scala': 'java', '.groovy': 'java', '.js': 'javascript', '.jsx': 'javascript', '.mjs': 'javascript', '.ts': 'javascript', '.tsx': 'javascript', '.cs': 'csharp', '.go': 'go', '.rb': 'ruby', '.php': 'php', '.c': 'c', '.h': 'c', '.cc': 'cpp', '.cpp': 'cpp', '.cxx': 'cpp', '.hpp': 'cpp', '.rs': 'rust'}; source annotation dict[str, str]. Then For _MANIFESTS, assign {'requirements.txt': {'django': 'django', 'flask': 'flask', 'sqlalchemy': 'sqlalchemy', 'fastapi': 'fastapi'}, 'pyproject.toml': {'django': 'django', 'flask': 'flask', 'sqlalchemy': 'sqlalchemy', 'fastapi': 'fastapi'}, 'Pipfile': {'django': 'django', 'flask': 'flask', 'sqlalchemy': 'sqlalchemy'}, 'package.json': {'"react"': 'react', '"next"': 'react', '"express"': 'express', '"vue"': 'vue', '"angular"': 'angular'}, 'pom.xml': {'spring-boot': 'spring', '<groupId>org.springframework': 'spring', 'hibernate': 'hibernate'}, 'build.gradle': {'org.springframework': 'spring', 'spring-boot': 'spring'}, 'Gemfile': {'rails': 'rails', 'sinatra': 'sinatra'}, 'go.mod': {'gin-gonic': 'gin', 'gorilla/mux': 'gorilla'}}; source annotation dict[str, dict[str, str]].
// Source: vvaharness/remediation_agent/frameworks.py:64-66
// Source signature: language_for(file_path: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn language_for(file_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/frameworks.py:65-65
  In source order: Retain source documentation literal source_literal_65_4; it is not a model call.
  // Source: vvaharness/remediation_agent/frameworks.py:66-66
  End this invocation with _EXT_LANG.get(Path(file_path or '').suffix.lower(), 'default').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/remediation_agent/frameworks.py:69-82
// Source signature: detect_frameworks(repo_root: str | Path) -> set[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_frameworks(repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/remediation_agent/frameworks.py:70-72
  In source order: Retain source documentation literal source_literal_70_4; it is not a model call. Then Evaluate once Path(repo_root); assign in source target order to root. Then For found, assign set(); source annotation set[str].
  // Source: vvaharness/remediation_agent/frameworks.py:73-81
  for each (fname, markers) in _MANIFESTS.items() {
    // Source: vvaharness/remediation_agent/frameworks.py:74-81
    for each p in list(root.glob(fname)) + list(root.glob(source_template_74_57)) {
      // Source: vvaharness/remediation_agent/frameworks.py:75-78
      Perform the following protected operations {
        // Source: vvaharness/remediation_agent/frameworks.py:76-76
        In source order: Evaluate once p.read_text(encoding='utf-8', errors='replace').lower(); assign in source target order to txt.
      }
      // Source: vvaharness/remediation_agent/frameworks.py:77-78
      On the first matching source exception OSError, in handler order {
        // Source: vvaharness/remediation_agent/frameworks.py:78-78
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vvaharness/remediation_agent/frameworks.py:79-81
      for each (needle, fw) in markers.items() {
        // Source: vvaharness/remediation_agent/frameworks.py:80-81
        if (the source predicate needle.lower() in txt is truthy) {
          // Source: vvaharness/remediation_agent/frameworks.py:81-81
          In source order: Evaluate found.add(fw); retain side effects and discard the expression result.
        }
      }
    }
  }
  // Source: vvaharness/remediation_agent/frameworks.py:82-82
  End this invocation with found.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
