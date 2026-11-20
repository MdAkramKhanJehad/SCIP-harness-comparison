# vvaharness/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/__init__.py.evidence.json`. SHA-256: `15da0807c1d2dfa06e530da1a345f1a5f789a82edb547ac3bc8c720522503ca3`.

```sudo
// Source: vvaharness/__init__.py:15-17
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from importlib.metadata import PackageNotFoundError; preserve alias and import-time effects. Then Resolve source import from importlib.metadata import version as _pkg_version; preserve alias and import-time effects.
// Source: vvaharness/__init__.py:19-23
Perform the following protected operations {
  // Source: vvaharness/__init__.py:21-21
  In source order: Evaluate once _pkg_version('vvaharness'); assign in source target order to __version__.
}
// Source: vvaharness/__init__.py:22-23
On the first matching source exception PackageNotFoundError, in handler order {
  // Source: vvaharness/__init__.py:23-23
  In source order: Evaluate once '1.5.1'; assign in source target order to __version__.
}
// Source: vvaharness/__init__.py:26-32
// Source signature: __getattr__(name: str)
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn __getattr__(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/__init__.py:27-27
  In source order: Retain source documentation literal source_literal_27_4; it is not a model call.
  // Source: vvaharness/__init__.py:28-30
  if (the source predicate name in ('remediate', 'validate') is truthy) {
    // Source: vvaharness/__init__.py:29-29
    In source order: Resolve source import from vvaharness import api; preserve alias and import-time effects.
    // Source: vvaharness/__init__.py:30-30
    End this invocation with getattr(api, name).
  }
  // Source: vvaharness/__init__.py:31-31
  In source order: Evaluate once source_template_31_10; assign in source target order to msg.
  // Source: vvaharness/__init__.py:32-32
  Raise AttributeError(msg).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness import api` at source line 29: `source_detail/vvaharness/__init__.py.sudo.md`.
- `from vvaharness import api` at source line 29: `source_detail/vvaharness/api.py.sudo.md`.
