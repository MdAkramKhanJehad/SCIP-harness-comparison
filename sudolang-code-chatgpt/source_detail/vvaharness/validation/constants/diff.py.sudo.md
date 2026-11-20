# vvaharness/validation/constants/diff.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/validation/constants/diff.py.evidence.json`. SHA-256: `7e516e652dd577c4ec43f552205394c293854b776a1a8308948fee62f180f6ae`.

```sudo
// Source: vvaharness/validation/constants/diff.py:15-28
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then For TRUST_BOUNDARY_RE, assign re.compile('(?i)(auth|session|login|logout|password|crypto|cipher|tls|ssl|token|secret|credential|permission|role|config|settings)\\b'); source annotation re.Pattern[str]. Then For HUNK_HEADER_RE, assign re.compile('^@@ -\\d+(?:,\\d+)? \\+(\\d+)(?:,\\d+)? @@'); source annotation re.Pattern[str].
// Source: vvaharness/validation/constants/diff.py:30-36
In source order: For HUNK_NEW_START_GROUP, assign 1; source annotation int. Then For GIT_HEADER_PREFIX, assign 'diff --git '; source annotation str. Then For GIT_HEADER_MIN_TOKENS, assign 4; source annotation int. Then For OLD_FILE_MARKER, assign '--- '; source annotation str. Then For NEW_FILE_MARKER, assign '+++ '; source annotation str.
// Source: vvaharness/validation/constants/diff.py:38-42
In source order: For MARKER_PATH_START, assign len(NEW_FILE_MARKER); source annotation int. Then For DEV_NULL_PATH, assign '/dev/null'; source annotation str. Then For GIT_PATH_PREFIXES, assign ('a/', 'b/'); source annotation tuple[str, ...]. Then For ADDED_LINE, assign '+'; source annotation str. Then For REMOVED_LINE, assign '-'; source annotation str.
// Source: vvaharness/validation/constants/diff.py:43-43
In source order: For NO_NEWLINE_NOTE, assign '\\'; source annotation str.
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
