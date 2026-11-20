# inputs/validator_hints.yaml — supplied guidance and request data

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## CWE-89.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:26-26
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stacked queries via ; if driver allows multi-statement
}
```

## CWE-89.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:27-27
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: second-order: value stored then later concatenated elsewhere
}
```

## CWE-89.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:28-28
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: numeric context with no quotes — wrong variable parameterised
}
```

## CWE-89.3

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:29-29
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: ORDER BY / LIMIT / identifier position (cannot be parameterised)
}
```

## CWE-89.4

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:30-30
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: comment terminator -- or /* to truncate the intended clause
}
```

## CWE-78.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:33-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: argument injection (leading -, --flag=val) when array-form used
}
```

## CWE-78.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:34-34
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: shell metachar in a value the callee itself passes to a shell
}
```

## CWE-78.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:35-35
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: $(...)/ backtick if any downstream eval
}
```

## CWE-78.3

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:36-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: newline / CRLF splitting into a second command
}
```

## CWE-79.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:39-39
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: context mismatch: HTML-encoded value placed in JS string or URL
}
```

## CWE-79.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:40-40
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: javascript: / data: URI in href/src
}
```

## CWE-79.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:41-41
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DOM clobbering, SVG <script>, template-literal injection
}
```

## CWE-79.3

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:42-42
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: mXSS via innerHTML round-trip
}
```

## CWE-79.4

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:43-43
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: event-handler attribute (onerror, onload)
}
```

## CWE-22.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:46-46
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: URL-encoded ..%2f, double-encoded ..%252f
}
```

## CWE-22.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:47-47
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Windows: ..\, mixed / and \, UNC \\host\share
}
```

## CWE-22.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:48-48
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: null byte truncation on legacy runtimes
}
```

## CWE-22.3

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:49-49
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: symlink inside base dir pointing outside
}
```

## CWE-22.4

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:50-50
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: absolute path bypass when only ../ is filtered
}
```

## CWE-918.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:53-53
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: decimal/octal/hex IP (2130706433, 0x7f000001, 0177.0.0.1)
}
```

## CWE-918.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:54-54
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: IPv6 [::ffff:127.0.0.1], [::], 0.0.0.0
}
```

## CWE-918.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:55-55
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DNS rebinding / TOCTOU between resolve and connect
}
```

## CWE-918.3

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:56-56
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: redirect chain to internal host, gopher:// or file:// scheme
}
```

## CWE-918.4

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:57-57
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: cloud metadata endpoints (169.254.169.254 etc.)
}
```

## CWE-502.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:60-60
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: gadget chain in an allowed type's transitive deps
}
```

## CWE-502.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:61-61
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: polymorphic type field (@class, $type) pointing to dangerous type
}
```

## CWE-502.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:62-62
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: nested/wrapped payload that passes outer allowlist
}
```

## CWE-611.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:65-65
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: parameter entities (% ent) when general entities disabled
}
```

## CWE-611.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:66-66
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: external DTD via SYSTEM with redirect
}
```

## CWE-611.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:67-67
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: XInclude, XSLT document(), schemaLocation
}
```

## CWE-601.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:70-70
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: scheme-relative //evil.com, backslash /\evil.com
}
```

## CWE-601.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:71-71
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: userinfo trick https://trusted.com@evil.com
}
```

## CWE-601.2

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:72-72
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: whitespace / control chars before scheme
}
```

## CWE-601.3

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:73-73
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: case / unicode normalisation of host
}
```

## CWE-798.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:76-76
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: credential moved but old literal still referenced via fallback
}
```

## CWE-798.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:77-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: env var read but default value is the old secret
}
```

## CWE-1333.0

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:80-80
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: input length not bounded before the regex
}
```

## CWE-1333.1

Scope: this is guidance/data when selected and supplied by the source loader; no application to every finding is inferred.

```sudo
// Source: inputs/validator_hints.yaml:81-81
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: alternation still nests under a quantifier
}
```

