# vvaharness/skills/ssrf/SKILL.md

A lens for server-side request forgery. Its emphasis is that a helper whose contract is to fetch a URL is a sink even when its body is a stub.

Source: `vvaharness/skills/ssrf/SKILL.md` (lines 1-92)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/ssrf/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/ssrf/SKILL.md:1-92
SsrfLens {
  name: "ssrf"
  description: "Hunt Server-Side Request Forgery (CWE-918) — any outbound fetch whose URL, scheme, host or port derives from a request."   // abstracted: the rest of line 3 lists activation triggers (avatar-by-URL, webhooks, URL preview, render-to-PDF, import-from-URL, OAuth discovery, "test connection" probes, proxy passthrough, helpers named download/fetch/get_image/get_base64_image_blob/load_url), states it "Ships probe.sh", and lists keywords
  Constraints {
    // prompt-src: vvaharness/skills/ssrf/SKILL.md:24
    "The application is the attacker's HTTP client: inside the perimeter, holding an instance role."

    // prompt-src: vvaharness/skills/ssrf/SKILL.md:26-34
    constraint HardGate {
      "HARD GATE — all three, or no finding:
        (a) SINK — a call doing network I/O to a URL, host or port, OR a function whose contract is to fetch a URL (parameter `url`/`uri`/`src`/`endpoint`/`callback`, or name in download/fetch/get_*/import_*/render_*) even when its body is stubbed, vendored or unseen;
        (b) SOURCE — the URL derives from a request-controlled channel (query, form, JSON body, header, path segment, webhook registration, uploaded document) or a DB column an untrusted party wrote earlier (second-order);
        (c) NO allow-list of scheme AND host enforced on the address actually connected to."
      "Literal URL, or one only settable through deployment config: DROP."
    }

    // prompt-src: vvaharness/skills/ssrf/SKILL.md:36-44 — the model is told to run the probe (see ssrf/probe.sudo)
    Run "sh .vvaharness/skills/ssrf/probe.sh" (optional argument: subtree) first.
    "An empty ecosystem section means the repo does not use it; empty sink sections do NOT end the hunt."
    Trace helpers to callers with GraphImporters and GraphNeighbors.
    // preserved: the SKILL says reference tables print "only when a sink exists"; the probe prints them when any capped section before line 122 had a hit, including the request-source and url-parameter sections (see ssrf/probe.sudo).

    // prompt-src: vvaharness/skills/ssrf/SKILL.md:46-58
    constraint OpaqueFetchHelper {
      "The `url` PARAMETER is the sink."
      "Never refute on \"the body makes no request\", \"the helper is a stub\" or \"no HTTP library is installed\"."
      WTForms URLField with DataRequired is not a defence (a widget plus a non-emptiness check).
      "ANCHOR the span on the route's call site; when only the helper's contract is in evidence, anchor its `def` line and name the calling route."
    }

    // prompt-src: vvaharness/skills/ssrf/SKILL.md:60-67 — what still counts
    "Blind — status, latency, byte count or error text only — is SSRF"; say which channel the attacker observes.
    "never refute because the response is discarded"; if the body is re-served, severity rises.
    A host check that resolves once, or a deny-list of private literals, does not hold: cite the per-hop redirect rule, the rebinding race, one bypass string.

    // prompt-src: vvaharness/skills/ssrf/SKILL.md:69-79
    constraint Refutations {
      Refute on: a scheme AND host allow-list enforced against the RESOLVED address (pinned connection, redirects re-checked per hop or disabled); an egress proxy configured in this repository or an SSRF-hardened client; a hardcoded URL or fixed base where input fills only path or query; a URL from trusted deployment config with no request field (unless a handler can write that config).
      "NOT refutations: scheme-only checks, a host check on the unresolved string, and syntax validators (`validators.URL()`, `URLField`, `new URL(s)`, `^https?://`) — they constrain the string, not the destination."
    }

    // prompt-src: vvaharness/skills/ssrf/SKILL.md:81-92
    constraint EnumerationRule {
      "One finding per distinct sink site. Two routes calling the same fetch helper are TWO findings, each anchored at its own span"
      The helper is a third finding only if independently reachable; an exported helper with no caller is reported separately or not at all.
      Report SSRF separately from open redirect, path traversal or XXE at the same lines.
      "CWE, exactly one: 918 by default; 611 when an XML parser's external entity is the fetch mechanism; 441 when the endpoint exists to relay arbitrary requests. 601 is open redirect, never a substitute."
    }
  }
}
