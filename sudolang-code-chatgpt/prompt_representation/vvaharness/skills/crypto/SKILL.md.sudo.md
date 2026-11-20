# vvaharness/skills/crypto/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Cryptographic review decisions

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:24-46
Constraints {
  The model's assigned review covers cryptography, key management and protocol security.
  Requested findings concern attacker-exploitable mathematics or protocol negotiation.
  if (the only evidence is generic MD5 hygiene) { The model is asked to omit that candidate. }
  The repeated mathematics/protocol-negotiation exclusion at source lines 28–29 remains a repeated instruction, not an extra review phase.
  Initial search priorities are non-exhaustive; the model is asked to reason beyond them.
  if (secret/HMAC/token equality uses ==, equals or memcmp) {
    The model is asked to examine early-exit timing disclosure against constant-time comparison.
  }
  if (JWT/signature verification trusts the token's algorithm or key id) {
    The requested checks include alg=none, HS/RS confusion and kid path traversal.
  }
  if (an encryption IV/nonce is constant, predictable or derived from replayable input) {
    The requested analysis includes GCM nonce-reuse authenticity compromise.
  }
  The model is asked to inspect non-CSPRNG token/IV/key/OTP/reset-code generation, including Math.random, rand(), Random() and random.random.
  The requested verification checks distinguish configured TLS/signature verification from actual enforcement: empty trust managers, always-true hostname checks and ignored verification results.
  Requested inspection includes literal keys/salts/passphrases in source or config, and key material exposed through logs/errors.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:1-4
Constraints {
  The source declares name = "crypto". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find broken or misused cryptography: weak hashes and ciphers, unsalted password storage, predictable randomness, bad key or IV handling, disabled certificate verification.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is broken or misused cryptography: weak hashes and ciphers, unsalted password storage, predictable randomness, bad key or IV handling, disabled certificate verification.
}
```

# Crypto Lens

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:24-29
Constraints {
  The requested model role and scope are reviewing the cryptography, key-handling, and security-protocol surfaces of this codebase.
  The requested search/review target is weaknesses an attacker can exploit mathematically or by abusing protocol negotiation — not generic "uses MD5 somewhere" hygiene items. mathematically or by abusing protocol negotiation — not generic "uses MD5 somewhere" hygiene items.
}
```

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:31-31
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where to look first (non-exhaustive — reason beyond this list):
}
```

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:32-33
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Secret/HMAC/token equality checks done with `==` / `equals` / `memcmp` instead of a constant-time comparator — early-exit leaks match length.
}
```

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:34-36
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Signature/JWT verification that reads the algorithm or key-id from the token itself and trusts it (alg=none, HS↔RS key confusion, kid path traversal).
}
```

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:37-39
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Symmetric encryption where the IV/nonce is constant, predictable, or derived from data the attacker can replay (GCM nonce reuse = full key compromise of authenticity).
}
```

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:40-42
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Security-relevant randomness drawn from non-CSPRNG sources (`Math.random`, `rand()`, `Random()`, `random.random`) for tokens, IVs, keys, OTPs, reset codes.
}
```

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:43-44
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: TLS / signature verification that is wired up but not enforced — empty trust managers, hostname checks returning `true`, verify result ignored.
}
```

```sudo
// Source: vvaharness/skills/crypto/SKILL.md:45-46
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Hard-coded keys, salts, or passphrases in source or config; key bytes written to logs or error messages.
}
```

