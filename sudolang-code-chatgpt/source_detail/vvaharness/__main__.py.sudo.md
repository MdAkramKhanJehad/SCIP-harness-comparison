# vvaharness/__main__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/__main__.py.evidence.json`. SHA-256: `020a2764a412f29f3b8d7aca6c8ca90751725dce1214c74b3e58caa8c6830225`.

```sudo
// Source: vvaharness/__main__.py:15-17
In source order: Resolve source import import sys; preserve alias and import-time effects. Then Resolve source import from vvaharness.cli import main; preserve alias and import-time effects.
// Source: vvaharness/__main__.py:19-20
if (the source predicate __name__ == '__main__' is truthy) {
  // Source: vvaharness/__main__.py:20-20
  In source order: Evaluate sys.exit(main()); retain side effects and discard the expression result.
}
```

## Local import links

- `from vvaharness.cli import main` at source line 17: `source_detail/vvaharness/cli/__init__.py.sudo.md`.
