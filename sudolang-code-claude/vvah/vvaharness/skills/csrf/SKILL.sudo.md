# vvaharness/skills/csrf/SKILL.md

A lens for state-changing endpoints that a forged cross-origin request can trigger, with a framework-by-framework checklist.

Source: `vvaharness/skills/csrf/SKILL.md` (lines 1-102)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/csrf/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/csrf/SKILL.md:1-102
CsrfLens {
  name: "csrf"
  description: "Find state-changing requests that a third-party origin can forge: missing or unverified CSRF tokens, unsafe SameSite, and CORS that trusts a reflected Origin with credentials."
  role: "You are a Cross-Site Request Forgery (CSRF) expert."   // prompt-src: vvaharness/skills/csrf/SKILL.md:24-24
  Constraints {
    // prompt-src: vvaharness/skills/csrf/SKILL.md:24-27
    "the attacker model is a logged-in user visiting a malicious page that silently fires a request to this application."

    // prompt-src: vvaharness/skills/csrf/SKILL.md:29-37
    constraint HardGate {
      "HARD GATE — a finding requires ALL THREE:
        (a) an endpoint that performs a state change (write, delete, transfer, update password, change email, modify settings — NOT a read-only GET),
        (b) the endpoint authenticates via cookie or HTTP basic auth (stateful session), AND
        (c) there is no effective CSRF defence: no synchronizer token verified on this specific handler, no SameSite=Strict/Lax cookie attribute, no Origin/Referer check on this path, and no custom request header requirement."
      "If any one of (a)–(c) is absent, DROP the finding."
    }

    // prompt-src: vvaharness/skills/csrf/SKILL.md:39-47
    constraint CsrfExemptException {
      An explicit exemption (@csrf_exempt in Django, @csrf.exempt in Flask, csrf.disable(), skip_before_action :verify_authenticity_token in Rails) removes CSRF protection at the framework level.
      "Report EVERY such state-changing handler as a CSRF finding even when it currently appears to be unauthenticated"
      "Condition (b) is SATISFIED by the explicit exemption decorator alone."
    }

    // prompt-src: vvaharness/skills/csrf/SKILL.md:49-94 — "Where to look first (non-exhaustive — reason beyond this list)"
    Django: @csrf_exempt views; CsrfViewMiddleware missing from MIDDLEWARE (global bypass); state-changing GET handlers (the middleware protects only unsafe methods); forms without {% csrf_token %}; no @require_POST so GET is also accepted; AJAX endpoints relying only on the session cookie without an X-CSRFToken or body token check.
    Flask: CSRFProtect not applied globally or per blueprint while views accept POST with session auth; @csrf.exempt on state-changing routes; a before-request check that skips non-safe methods.
    Express: csurf missing or applied to only some routes; session cookie without SameSite Strict or Lax and no custom header check.
    Spring MVC: .csrf().disable(), or request matchers excluding state-changing paths (protection is on by default); SameSite unset and no token checked.
    Rails: protect_from_forgery bypassed, or skip_before_action :verify_authenticity_token on state-changing actions.
    Cross-cutting: JSON APIs relying only on Content-Type: application/json; logout endpoints without protection (forced logout); "Password/email change endpoints are the highest-severity CSRF target — always check these specifically."

    // prompt-src: vvaharness/skills/csrf/SKILL.md:96-102
    constraint EnumerationRule {
      "report EACH ONE as a SEPARATE finding with its own function name, file, and line number. Do NOT collapse all instances into a single omnibus finding."
    }
  }
}
