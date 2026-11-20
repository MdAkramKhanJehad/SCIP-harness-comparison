# vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py.evidence.json`. SHA-256: `9b8f9d60154492465741a0e11c4355c4137b8ebdb35af49d46a1379d6cc848d2`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:15-50
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import QueryValidationError; preserve alias and import-time effects. Then Evaluate once frozenset({'ALTER', 'CALL', 'COMMIT', 'CREATE', 'DELETE', 'DETACH', 'DROP', 'EXPORT', 'GRANT', 'IMPORT', 'INSERT', 'LOAD', 'MERGE', 'REMOVE', 'REVOKE', 'ROLLBACK', 'SET', 'SHOW', 'START', 'STOP', 'TRANSACTION', 'TRUNCATE', 'UPDATE', 'UPSERT'}); assign in source target order to _FORBIDDEN.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:51-51
In source order: Evaluate once re.compile('[A-Za-z_][A-Za-z0-9_]*'); assign in source target order to _TOKEN.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:54-64
// Source signature: validate_readonly_cypher(cypher: str) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_readonly_cypher(cypher) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:55-56
  if (the source predicate not cypher.strip() is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:56-56
    Raise QueryValidationError('Cypher query is empty').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:57-58
  In source order: Evaluate once _code_only(cypher); assign in source target order to code. Then Evaluate once [index for index, char in enumerate(code) if char == ';']; assign in source target order to semicolons.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:59-60
  if (the source predicate len(semicolons) > 1 or (semicolons and code[semicolons[0] + 1:].strip()) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:60-60
    Raise QueryValidationError('multiple Cypher statements are not allowed').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:61-62
  In source order: Evaluate once {token.upper() for token in _TOKEN.findall(code)}; assign in source target order to tokens. Then Evaluate once sorted(tokens.intersection(_FORBIDDEN)); assign in source target order to forbidden.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:63-64
  if (the source predicate forbidden is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:64-64
    Raise QueryValidationError(source_template_64_35).
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:67-115
// Source signature: _code_only(cypher: str) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _code_only(cypher) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:68-70
  In source order: For output, assign []; source annotation list[str]. Then Evaluate once 0; assign in source target order to index. Then Evaluate once 'code'; assign in source target order to state.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:71-112
  while (the source predicate index < len(cypher) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:72-73
    In source order: Evaluate once cypher[index]; assign in source target order to char. Then Evaluate once cypher[index + 1] if index + 1 < len(cypher) else ''; assign in source target order to following.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:74-111
    if (the source predicate state == 'code' is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:75-79
      if (the source predicate char == '/' and following == '/' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:76-78
        In source order: Evaluate output.extend('  '); retain side effects and discard the expression result. Then Apply source augmented assignment index += 2 with source evaluation/in-place semantics. Then Evaluate once 'line_comment'; assign in source target order to state.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:79-79
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:80-84
      if (the source predicate char == '/' and following == '*' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:81-83
        In source order: Evaluate output.extend('  '); retain side effects and discard the expression result. Then Apply source augmented assignment index += 2 with source evaluation/in-place semantics. Then Evaluate once 'block_comment'; assign in source target order to state.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:84-84
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:85-89
      if (the source predicate char in {"'", '"', '`'} is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:86-87
        In source order: Evaluate output.append(' '); retain side effects and discard the expression result. Then Evaluate once {"'": 'single', '"': 'double', '`': 'identifier'}[char]; assign in source target order to state.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:89-89
        In source order: Evaluate output.append(char); retain side effects and discard the expression result.
      }
    }
    else {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:90-111
      if (the source predicate state == 'line_comment' is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:91-91
        In source order: Evaluate output.append(source_literal_91_26 if char == source_literal_91_42 else ' '); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:92-93
        if (the source predicate char == source_literal_92_23 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:93-93
          In source order: Evaluate once 'code'; assign in source target order to state.
        }
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:94-111
        if (the source predicate state == 'block_comment' is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:95-95
          In source order: Evaluate output.append(' '); retain side effects and discard the expression result.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:96-99
          if (the source predicate char == '*' and following == '/' is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:97-99
            In source order: Evaluate output.append(' '); retain side effects and discard the expression result. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics. Then Evaluate once 'code'; assign in source target order to state.
          }
        }
        else {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:101-102
          In source order: Evaluate output.append(' '); retain side effects and discard the expression result. Then Evaluate once {'single': "'", 'double': '"', 'identifier': '`'}[state]; assign in source target order to quote.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:103-111
          if (the source predicate char == '\\' and state != 'identifier' and following is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:104-105
            In source order: Evaluate output.append(' '); retain side effects and discard the expression result. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
          }
          else {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:106-111
            if (the source predicate char == quote is truthy) {
              // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:107-111
              if (the source predicate following == quote is truthy) {
                // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:108-109
                In source order: Evaluate output.append(' '); retain side effects and discard the expression result. Then Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
              }
              else {
                // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:111-111
                In source order: Evaluate once 'code'; assign in source target order to state.
              }
            }
          }
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:112-112
    In source order: Apply source augmented assignment index += 1 with source evaluation/in-place semantics.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:113-114
  if (the source predicate state not in {'code', 'line_comment'} is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:114-114
    Raise QueryValidationError('unterminated Cypher string, identifier, or comment').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/query/readonly.py:115-115
  End this invocation with ''.join(output).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.errors import QueryValidationError` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
