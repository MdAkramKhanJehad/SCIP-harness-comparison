# inputs/validator_hints.yaml

Per-CWE adversarial bypass hints injected into the Stage 11 validation agent's launch prompt, so its penetration-tester persona tries realistic attacks per class.

Source: `inputs/validator_hints.yaml` (lines 1-81)
Executor: code (data); the hint text is model-facing
Called from: `vvaharness/validation/hints/loader.py` (read from ./inputs/validator_hints.yaml relative to the working directory)

// src: inputs/validator_hints.yaml:15-23
// File comments: keep each list at most 6 items ("the agent is told to TRY these, not merely read them"); this is the sole hints source with no packaged fallback; an absent file means no hints; a malformed file is ignored with a warning

// src: inputs/validator_hints.yaml:25-81
Options {
  hints: {
    "CWE-89":   ["stacked queries via ; if driver allows multi-statement", "second-order: value stored then later concatenated elsewhere", "numeric context with no quotes — wrong variable parameterised", "ORDER BY / LIMIT / identifier position (cannot be parameterised)", "comment terminator -- or /* to truncate the intended clause"]
    "CWE-78":   ["argument injection (leading -, --flag=val) when array-form used", "shell metachar in a value the callee itself passes to a shell", "$(...)/ backtick if any downstream eval", "newline / CRLF splitting into a second command"]
    "CWE-79":   ["context mismatch: HTML-encoded value placed in JS string or URL", "javascript: / data: URI in href/src", "DOM clobbering, SVG <script>, template-literal injection", "mXSS via innerHTML round-trip", "event-handler attribute (onerror, onload)"]
    "CWE-22":   ["URL-encoded ..%2f, double-encoded ..%252f", "Windows: ..\\, mixed / and \\, UNC \\\\host\\share", "null byte truncation on legacy runtimes", "symlink inside base dir pointing outside", "absolute path bypass when only ../ is filtered"]
    "CWE-918":  ["decimal/octal/hex IP (2130706433, 0x7f000001, 0177.0.0.1)", "IPv6 [::ffff:127.0.0.1], [::], 0.0.0.0", "DNS rebinding / TOCTOU between resolve and connect", "redirect chain to internal host, gopher:// or file:// scheme", "cloud metadata endpoints (169.254.169.254 etc.)"]
    "CWE-502":  ["gadget chain in an allowed type's transitive deps", "polymorphic type field (@class, $type) pointing to dangerous type", "nested/wrapped payload that passes outer allowlist"]
    "CWE-611":  ["parameter entities (% ent) when general entities disabled", "external DTD via SYSTEM with redirect", "XInclude, XSLT document(), schemaLocation"]
    "CWE-601":  ["scheme-relative //evil.com, backslash /\\evil.com", "userinfo trick https://trusted.com@evil.com", "whitespace / control chars before scheme", "case / unicode normalisation of host"]
    "CWE-798":  ["credential moved but old literal still referenced via fallback", "env var read but default value is the old secret"]
    "CWE-1333": ["input length not bounded before the regex", "alternation still nests under a quantifier"]
  }
}
