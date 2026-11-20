# vvaharness/util/git_paths.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/git_paths.py.evidence.json`. SHA-256: `c38c3fd22f05a14b2e92a79de886d79be33d13eae6db03cab010b80de5e91f4b`.

```sudo
// Source: vvaharness/util/git_paths.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import itertools; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import from functools import cache; preserve alias and import-time effects.
// Source: vvaharness/util/git_paths.py:21-23
In source order: Resolve source import from pathlib import PurePosixPath; preserve alias and import-time effects. Then Evaluate once '.git'; assign in source target order to GIT_DIR.
// Source: vvaharness/util/git_paths.py:26-29
// Source signature: is_git_metadata(path: str | os.PathLike[str]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_git_metadata(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/git_paths.py:27-28
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call. Then Evaluate once PurePosixPath(os.fspath(path).replace('\\', '/')).parts; assign in source target order to parts.
  // Source: vvaharness/util/git_paths.py:29-29
  End this invocation with any((part.casefold() == GIT_DIR for part in parts)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/git_paths.py:33-36
// Source: vvaharness/util/git_paths.py:32-32
Before creating this callable, evaluate and retain decorators top-to-bottom: cache.
// Source: vvaharness/util/git_paths.py:33-36
// Source signature: git_dir_spellings() -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn git_dir_spellings() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/git_paths.py:34-35
  In source order: Retain source documentation literal source_literal_34_4; it is not a model call. Then Evaluate once [(c.lower(), c.upper()) for c in GIT_DIR[1:]]; assign in source target order to letters.
  // Source: vvaharness/util/git_paths.py:36-36
  End this invocation with tuple(('.' + ''.join(combo) for combo in itertools.product(*letters))).
  If execution reaches this end, finish with the source implicit None result.
}
At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
