# vvaharness/skills/missing-controls/SKILL.md

A lens for weaknesses that are an absent control. It inverts the method: enumerate every site where a control belongs, then judge each site.

Source: `vvaharness/skills/missing-controls/SKILL.md` (lines 1-146)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/missing-controls/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/missing-controls/SKILL.md:1-146
AbsentControlLens {
  name: "missing-controls"
  description: "Find weaknesses that consist of an ABSENT control — no rate limit, no session invalidation, no cookie flags, debug left on, secrets or PII stored in cleartext — by enumerating every site the control belongs and checking each."
  Constraints {
    // prompt-src: vvaharness/skills/missing-controls/SKILL.md:24-31
    This lens hunts for a hole, not a construct; nothing upstream will point at these.
    "The method is inverted. Instead of \"is this construct dangerous?\", ask **\"what should be here, and is it?\"**"
    // note: this SKILL.md does not tell the model to run its probe.sh; the probe exists beside it (see missing-controls/probe.sudo) and the Stage 4 prompt tells the model that a lens shipping a probe.sh can be run (vvaharness/pipeline/stages/s4/prompts.py:214, 276-277; outside this batch).

    // prompt-src: vvaharness/skills/missing-controls/SKILL.md:33-45
    constraint HardGate {
      A finding requires all three:
      1. "The site is real and reachable." Not a hypothetical.
      2. "The control genuinely belongs there." Name the asset and the actor; "\"Every endpoint should have rate limiting\" is not analysis"
      3. "It is absent on THIS path", and you checked. "Look, then conclude."
      "If the control exists anywhere on the path, **refute** and say where it is."
    }

    // prompt-src: vvaharness/skills/missing-controls/SKILL.md:47-56
    constraint EnumerateBeforeConcluding {
      "Grep the whole repository for every site of the kind it protects, then decide site by site."
      "Report one finding per absent site, each with its own file and line. If it is present everywhere you enumerated, refute and say how many sites you checked."
    }

    // prompt-src: vvaharness/skills/missing-controls/SKILL.md:58-121 — the controls and where each belongs
    ControlCatalogue {
      "Anti-automation on credential and cost endpoints — CWE-307, CWE-799": sites are login, registration, password reset, OTP / MFA, token refresh, email send, payment, upload, expensive search; "Storage without enforcement is a decoy."   // prompt-src: vvaharness/skills/missing-controls/SKILL.md:60-69
      "Session termination — CWE-613, CWE-384": logout, password, email or role change, deactivation; the classic hole is a logout that returns 200 while the issued JWT stays valid.   // prompt-src: vvaharness/skills/missing-controls/SKILL.md:71-79
      "Cookie and transport flags — CWE-614, CWE-1004, CWE-1275, CWE-319": every set_cookie write and every session config key; "**Report per site.** A config-level default does not cover an explicit `set_cookie` that overrides it"   // prompt-src: vvaharness/skills/missing-controls/SKILL.md:81-88
      "Deployment and debug posture — CWE-16, CWE-215, CWE-489": app.run(debug=True), DEBUG = True, ALLOWED_HOSTS = ["*"], stack traces to the client, exposed admin or metrics endpoints, default credentials in seeds; report the class the evidence supports.   // prompt-src: vvaharness/skills/missing-controls/SKILL.md:90-99
      "Data at rest and in transit — CWE-312, CWE-311, CWE-319, CWE-359": PII stored in plain columns, real-looking seed values, unencrypted cache or queue secrets, verify=False; stored-in-cleartext and returned-in-a-response are separate findings.   // prompt-src: vvaharness/skills/missing-controls/SKILL.md:101-110
      "Request forgery and origin trust — CWE-352, CWE-942, CWE-1021": covered by the csrf lens; "Enumerate every state-changing handler".   // prompt-src: vvaharness/skills/missing-controls/SKILL.md:112-115
      "Authorization": covered by the access-control lens; translate its Spring / JAX-RS examples to the framework in front of you.   // prompt-src: vvaharness/skills/missing-controls/SKILL.md:117-121
    }

    // prompt-src: vvaharness/skills/missing-controls/SKILL.md:123-139
    constraint FalsePositiveDiscipline {
      Refute when the control is present anywhere on the path (middleware, base class, dependency, router-level decorator, framework default); when the endpoint is public by design and holds no scarce resource; when sensitive data is synthetic "**and** the file is not shipped or seeded into a running environment. If it *is* seeded, it is a finding."; when the target is a fixed constant.
      "Say which of these you checked."
    }

    // prompt-src: vvaharness/skills/missing-controls/SKILL.md:141-146
    Output: one finding per absent site, naming the file and line the fix must edit; the rationale states what was enumerated, how many sites, which had the control and which did not.
  }
}
