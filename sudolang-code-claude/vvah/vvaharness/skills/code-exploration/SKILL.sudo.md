# vvaharness/skills/code-exploration/SKILL.md

Not a vulnerability lens. It is the coverage procedure every lens is meant to run on top of: write down an inventory of the whole tree, read files to the last line, follow edges, and report coverage arithmetic.

Source: `vvaharness/skills/code-exploration/SKILL.md` (lines 1-285)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/code-exploration/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/code-exploration/SKILL.md:1-285
ExhaustiveRepositoryExploration {
  name: "code-exploration"
  description: "Exhaustive repository exploration procedure — Glob the whole tree into a written inventory, group it by directory, and account for every file including templates, Dockerfiles, compose and k8s manifests, nginx/uwsgi/gunicorn config, CI workflows, dotfiles, SQL migrations, static assets and __init__.py. Load FIRST, before any lens, when you are asked to map a repository, enumerate its attack surface, find entry points, decide what is in scope, or conclude that something is absent."   // abstracted: the last sentence of line 3 names the reading, graph-edge and coverage-report topics
  Constraints {
    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:24-33
    "A lens pointed at 38% of a repository finds at most 38% of its bugs, and reports that fraction in the confident tone of a complete answer."
    "Never go looking for `app.py` or `routes/` because this file mentions them, and never report a finding you have not read in the tree in front of you."
    // note: this SKILL.md never names its probe.sh (see code-exploration/probe.sudo); the Stage 4 prompt tells the model that a lens shipping a probe.sh can be run (vvaharness/pipeline/stages/s4/prompts.py:214, 276-277; outside this batch).

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:35-61 — "The measured failure"
    // abstracted: two measured examples (17 of 45 files nameable; a 23-file application with an unopened frontend/ tree) and two finding shapes (a short entry module holding a hardcoded signing key and an SSTI sink; a frontend component that decodes the JWT and posts the user id the handler trusts). Motivation only; the rules follow.

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:63-73
    constraint HardGate {
      Every finding from this pass requires all four:
      1. "An inventory exists, written down, before any conclusion."
      2. "The file was opened and read to its last line."
      3. "A repo-relative path and a real `line_start..line_end`" from the numbered Read output, "plus exactly one most-specific CWE id."
      4. "For any absence claim" name the files opened looking for the control; "An absence asserted against an unread directory is not a finding, it is the shape of one."
    }

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:75-110
    fn enumerate():executor=model {
      "`Glob` first, always, and never start from the file you were handed."   // Glob "**/*"
      Split the inventory by directory, write the group list as the plan, mark each group open or closed; the counts must sum to the inventory size.
      "**Coverage is the set difference between the inventory and the set of files you have opened.**" "If the difference is non-empty you are not done, you are mid-pass."
      Check that the inventory is not lying: "`Glob` truncates at 500 hits"; a path outside scan scope returns an "excluded from the scan scope" error and is recorded as excluded, not clean; "Do not substitute a graph node list for the inventory." (the graph skips the dot-namespace)
    }

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:112-170 — file classes a source-only sweep skips
    // abstracted: glob lists per class (templates and views; container and orchestration; CI/CD; dependency manifests; dotfiles and env templates; SQL and migrations; static assets; __init__.py, base classes and shared helpers) with the markers to grep and four central-control shapes. Reference material; each class carries findings and must be globbed by name.

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:172-193
    constraint ReadToTheEnd {
      "A file read halfway produces exactly the same false \"absent\" conclusion as a file never read, and produces it with more confidence."
      Watch for truncation markers; "**Continue from the last line number you were shown.**" (offset is 0-based, so a page ending at displayed line 2000 continues at offset 2000).
      Confirm the end: "(file is empty or offset past EOF)" or a short page without a truncation marker; "Assumption is not proof."
      The reader decodes only the first 800,000 characters and caps a page at 200,000; past that the end marker is false, so grep for a construct near the end and record the file as partially read.
      "`Grep` is for locating, never for concluding."
    }

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:195-221
    constraint FollowTheEdges {
      A handler that renders a template, a model it writes (with base class, migration, serializer), a config key it reads, and a parent template it extends are all in scope.
      "**Use the graph with its real signatures; do not guess.**" GraphImporters(file); GraphNeighbors(file, function) "needs BOTH arguments"; GraphCommunityOf(file) then GraphSinksInCommunity(community); CweGuidance(cwe_id).
      "**An empty graph answer is a signal, not an all-clear.**" GraphImporters sees module-level imports only; read the __init__.py yourself.
      "Graph hits *add to* the inventory-driven sweep, never replace it."
    }

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:223-242
    constraint Refutations {
      "Refute and say so; a refutation with a named search is a result."
      The control exists somewhere unread (open __init__.py, base class, router registration, middleware, reverse-proxy config); the template autoescapes (only an explicit safe marker defeats it); the file is not shipped (dockerignore, tests, documentation: "do not report a write-up of a bug as the bug"); the config is an example with placeholders; the value is a fixed literal; "**You only read a prefix.**"
    }

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:244-265
    constraint EnumerationRule {
      "**One finding per distinct site, each with its own file and its own line span.**"
      A noisy grep is sorted, not counted: two password-writing sites are two findings; a verifier reading the same digest is a hit to judge. "State which you counted and why."
      Never collapse into an omnibus finding; "do not pad — the *same* construct reported twice is a duplicate, not coverage."
      Before leaving a file, ask what else is wrong with it.
    }

    // prompt-src: vvaharness/skills/code-exploration/SKILL.md:267-285
    constraint ReportCoverage {
      Close with inventory size, files opened, files read to the end, files refused as out of scope; "**The named list of what you did not finish, and why**"; which directory groups are closed and open.
      "Exploration ends when the set difference between the inventory and the files you have read to the end is empty, or when every remaining element of it is listed in your coverage report with a reason. Those are the only two endings."
    }
  }
}
