# vvaharness/validation/constants/test_inventory.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/test_inventory.py.evidence.json`. SHA-256: `c889d53f9d04d6cbfbe3b823b0e168fad901ed9e33b4cf80753d1efca38af379`.

```sudo
// Source: vvaharness/validation/constants/test_inventory.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then For PY_TEST_EXACT_NAMES, assign frozenset({'conftest.py', 'tests.py', 'test.py'}); source annotation frozenset[str]. Then Evaluate once 'test_'; assign in source target order to PY_TEST_NAME_PREFIX. Then Evaluate once '_test.py'; assign in source target order to PY_TEST_NAME_SUFFIX.
// Source: vvaharness/validation/constants/test_inventory.py:22-32
In source order: For JS_TEST_SUFFIXES, assign ('.test.js', '.test.jsx', '.test.ts', '.test.tsx', '.spec.js', '.spec.jsx', '.spec.ts', '.spec.tsx'); source annotation tuple[str, ...]. Then For NEGATIVE_TEST_MARKERS, assign ('pytest.raises', 'assertRaises', 'with raises', 'expect_exception', 'toThrow', 'rejects', 'should fail', 'assert.throws', 'malformed', 'invalid', 'fake', 'mock', 'exploit', 'payload'); source annotation tuple[str, ...].
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../../prompt_representation/vvaharness/validation/constants/test_inventory.py.sudo.md). Exact strings in the evidence asset support this conversion.
