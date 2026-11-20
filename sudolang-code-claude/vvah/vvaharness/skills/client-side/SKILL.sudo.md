# vvaharness/skills/client-side/SKILL.md

A lens for browser-delivered code. Its central rule is that a check made only in the frontend is itself the finding, reported at the server line that omits it.

Source: `vvaharness/skills/client-side/SKILL.md` (lines 1-110)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/client-side/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/client-side/SKILL.md:1-110
ClientSideLens {
  name: "client-side"
  description: "Weaknesses in browser-delivered code — JS/TS, JSX/TSX, Vue, Svelte, Angular, HTML, templates, bundler and Docker config."   // abstracted: the remaining description (line 3) lists the sink classes, "and above all security decisions made only in the frontend (disabled buttons, hidden fields, is_admin render gates, a client-computed user_id) that the server never repeats", says it "Ships probe.sh", and ends "Activate on frontend/, public/, static/, src/components/, bundler config, or .js/.jsx/.ts/.tsx/.vue/.svelte/.html files."
  Constraints {
    // prompt-src: vvaharness/skills/client-side/SKILL.md:24-29
    "Nothing shipped to the client is secret"
    "A client-side control is not a security control"
    "a check that exists only in the frontend IS the finding — the defect is the server-side absence it conceals."
    "Nothing upstream hands you frontend code; go look."

    // prompt-src: vvaharness/skills/client-side/SKILL.md:31-39 — the model is told to run the probe (see client-side/probe.sudo)
    Run "sh .vvaharness/skills/client-side/probe.sh [root]" first.
    "A *missing* section means the probe broke; `... N hits total` means the cap truncated, so grep that class yourself. It locates, it decides nothing below."

    // prompt-src: vvaharness/skills/client-side/SKILL.md:41-51
    constraint HardGate {
      A finding requires ALL of:
      1. "A construct with a line span" — sink call, storage write, literal secret, listener, build key, pin. "Not \"the SPA should validate input\"."
      2. "A named consequence to an asset"
      3. "For a \"the frontend enforces X\" claim, the server gap in hand" — "Unreachable backend: unverified, downgrade, never assert."
      4. "Exactly one most-specific CWE", `CweGuidance`-checked: "`innerHTML` XSS is CWE-79 not CWE-20, client-enforced authorization CWE-602 not CWE-284, a server trusting a client `user_id` CWE-639 not CWE-863."
    }

    // prompt-src: vvaharness/skills/client-side/SKILL.md:53-73 — "Judgement the probe cannot make"
    "Client-supplied identity — highest value here." A handler reading data.get("user_id") instead of the authenticated principal is CWE-639 "at the server line", with the client line as evidence.
    "Client-side JWT decode is unauthenticated parsing". "Build-inlined env is published"; ask only whether the value is secret.
    Origin checks by indexOf / startsWith / endsWith are bypassable; "only strict equality against an allow-list refutes." postMessage(data, "*") with a token is CWE-201.
    A base URL from window.location.hostname with cross-origin credentials: check the server for Origin reflection with Allow-Credentials: true.
    Shipped artifacts: a dev-server CMD (CWE-489); COPY . . without a .dockerignore entry; no lockfile beside npm install.
    Toggles that persist nowhere; a password form with only a new-password field (CWE-620); startsWith("/") does not refute a redirect; a bound only in markup is no bound.

    // prompt-src: vvaharness/skills/client-side/SKILL.md:75-88 — "FP CHECKS — what REFUTES"
    A sanitizer on the path; React / Vue / Svelte default interpolation "is **not** a finding".
    A literal or closed-enumeration sink value; setTimeout with a function reference; setAttribute on a non-URL, non-on* attribute.
    A secret that is public by design (pk_live_, Firebase, Sentry DSN, Maps) — name which and refute.
    The server repeats the check; a client-sent id used only as a lookup target while the handler derives the actor is not CWE-639.
    The pin is patched — name the version.
    "Say which you checked; an unqualified frontend finding reads as a lint rule."

    // prompt-src: vvaharness/skills/client-side/SKILL.md:90-104
    constraint EnumerationRule {
      "One finding per distinct site, with its own file and `line_start..line_end` on the construct a fix edits."
      Anchor token storage at the write; every raw-HTML sink, every client-supplied-identity request and every vulnerable pin is its own finding; one component usually holds several classes — emit each with its own CWE.
      "Never collapse into \"frontend security issues\" — a blanket finding is credited once."
    }

    // prompt-src: vvaharness/skills/client-side/SKILL.md:106-110
    "A client file is proof that a server-side parameter is attacker-controlled."
    "Read the client to learn which server parameters to distrust, then report the server line."
  }
}
