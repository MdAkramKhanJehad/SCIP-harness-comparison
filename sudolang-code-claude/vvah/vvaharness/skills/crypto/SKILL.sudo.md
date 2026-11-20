# vvaharness/skills/crypto/SKILL.md

A lens for exploitable cryptographic and protocol weaknesses, as opposed to hygiene items.

Source: `vvaharness/skills/crypto/SKILL.md` (lines 1-46)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/crypto/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/crypto/SKILL.md:1-46
CryptoLens {
  name: "crypto"
  description: "Find broken or misused cryptography: weak hashes and ciphers, unsalted password storage, predictable randomness, bad key or IV handling, disabled certificate verification."
  Constraints {
    // prompt-src: vvaharness/skills/crypto/SKILL.md:24-29
    You are reviewing the cryptography, key-handling and security-protocol surfaces of this codebase.
    "Target weaknesses an attacker can exploit mathematically or by abusing protocol negotiation — not generic \"uses MD5 somewhere\" hygiene items."
    // preserved: lines 28-29 repeat lines 26-27 word for word ("mathematically or by abusing protocol negotiation — not generic "uses MD5 somewhere" hygiene items."), so the model sees that clause twice.
    // No hard gate is stated in this lens, unlike most other lenses.

    // prompt-src: vvaharness/skills/crypto/SKILL.md:31-46 — "Where to look first (non-exhaustive — reason beyond this list)"
    Secret, HMAC or token equality checks with == / equals / memcmp instead of a constant-time comparator.
    Signature or JWT verification that trusts the algorithm or key id from the token itself (alg=none, HS and RS key confusion, kid path traversal).
    Symmetric encryption with a constant, predictable or replayable IV or nonce ("GCM nonce reuse = full key compromise of authenticity").
    Security-relevant randomness from non-cryptographic generators (Math.random, rand(), Random(), random.random) for tokens, IVs, keys, one-time passwords, reset codes.
    TLS or signature verification wired up but not enforced: empty trust managers, hostname checks returning true, verify result ignored.
    Hard-coded keys, salts or passphrases in source or config; key bytes written to logs or error messages.
  }
}
