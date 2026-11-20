# vvaharness/skills/sibling-instances/SKILL.md

A procedure, used only after a weakness is confirmed, for sweeping the whole repository for other sites of the same pattern and other classes at the same site.

Source: `vvaharness/skills/sibling-instances/SKILL.md` (lines 1-89)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/sibling-instances/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/sibling-instances/SKILL.md:1-89
SiblingInstanceSweep {
  name: "sibling-instances"
  description: "After confirming a weakness, sweep the repository for every other site of the same pattern and report each one — a class confirmed at one location is almost never present at only one location."
  Constraints {
    // prompt-src: vvaharness/skills/sibling-instances/SKILL.md:24-30
    Once a class is confirmed at one site the question becomes "where else?"; "Reporting one instance of a repeated defect is a partial answer that reads like a complete one."

    // prompt-src: vvaharness/skills/sibling-instances/SKILL.md:32-35
    constraint WhenThisApplies {
      "Only **after** a confirmation. Do not sweep for a class you just refuted, and do not sweep speculatively for classes you have no evidence of — that is how precision dies."
    }

    // prompt-src: vvaharness/skills/sibling-instances/SKILL.md:37-53
    fn sweep():executor=model {
      1. Name the confirmed pattern concretely enough to search for (sink call, algorithm name, missing decorator, unset flag).
      2. Grep the whole repository, with two or three phrasings (for example `hashlib.md5` and `md5(`).
      3. "Open every hit and judge it on its own evidence. A hit is a candidate, not a finding."
      4. "Report one finding per confirmed site", each with its own file and line span; do not fold several sites into one finding.
      5. "Do not pad." Near-identical findings at the same construct are duplicates.
    }

    // prompt-src: vvaharness/skills/sibling-instances/SKILL.md:55-73 — recurring patterns, most to least reliable
    Query construction; hashing and randomness (for example MD5 in a model's set_password and inline in the registration handler); regexes with nested quantifiers; outbound requests; deserialization; cookie writes and header setters; decorator omissions.

    // prompt-src: vvaharness/skills/sibling-instances/SKILL.md:75-81
    Before leaving a location, ask what else is wrong with it; "Two classes at one line are two findings, not one broad finding."

    // prompt-src: vvaharness/skills/sibling-instances/SKILL.md:83-89
    Rationale requirement: state the sweep term, the candidate hit count and the confirmed count.
  }
}
