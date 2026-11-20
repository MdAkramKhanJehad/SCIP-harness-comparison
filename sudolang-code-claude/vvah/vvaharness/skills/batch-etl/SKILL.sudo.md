# vvaharness/skills/batch-etl/SKILL.md

A lens for batch and ETL jobs, where the attacker is an upstream producer, a scheduler parameter or a shared landing directory rather than a web user.

Source: `vvaharness/skills/batch-etl/SKILL.md` (lines 1-59)
Executor: model (instructions only; no code checks any rule in this file)
Called from: copied into `.vvaharness/skills/batch-etl/` of the scanned repository by `vvaharness/skills/__init__.py` inject_skills; reachable from Stage 2 and Stage 4 model sessions through `skill_root`

// external: the frontmatter `description` is what the agent backend shows the model when it decides whether to load this skill; that selection happens in the backend (`vvaharness/backends/`), outside this batch.
// abstracted: lines 6-20 are the Apache 2.0 license comment; no instruction.

// prompt-src: vvaharness/skills/batch-etl/SKILL.md:1-59
BatchEtlLens {
  name: "batch-etl"
  description: "Find defects specific to batch and ETL paths: unvalidated bulk input, injection through generated statements, and trust placed in upstream-written data."
  role: "You are a Batch / ETL data-pipeline expert."   // prompt-src: vvaharness/skills/batch-etl/SKILL.md:24-24
  Constraints {
    // prompt-src: vvaharness/skills/batch-etl/SKILL.md:24-27
    The target is a file-in, transform, file-out job (mainframe-migrated or scheduler-driven).
    "The attacker model is: an upstream producer, scheduler/operator parameter, or shared landing directory — NOT an interactive web user."

    // prompt-src: vvaharness/skills/batch-etl/SKILL.md:29-34
    constraint HardGate {
      "HARD GATE — for every finding cite (a) the externally-influenced value (job parameter, env var, upstream record field, filename in a watched dir) and (b) the file:line where it reaches a path, command, SQL, or output record WITHOUT validation."
      "If both producer and consumer are inside the same trust domain and the value cannot be set by a lower-privileged party, DROP it."
    }

    // prompt-src: vvaharness/skills/batch-etl/SKILL.md:36-59 — "Where to look first (non-exhaustive — reason beyond this list)"
    Job parameters and environment variables (sys.argv, os.environ, JCL PARM=, scheduler variables) reaching open() / Path() / shutil.* / os.remove without a fixed base directory plus realpath check (path traversal as the batch service account).
    Output file names or staging directories derived from input record fields (traversal or collision through crafted records).
    Shared landing or spool directories: glob("*.dat") or "pick newest by mtime" where any writer can plant a file (time-of-check to time-of-use, untrusted producer).
    Fixed-width, packed-decimal (COMP-3) or EBCDIC parsing: header length used to slice or seek without a cap; sign or zone nibble not validated; off-by-one between COBOL 1-based offsets and Python 0-based slices.
    Record-count or hash-total trailer not verified against the body.
    Emitted CSV or report cells from input records written without stripping leading = + - @ (formula injection).
    subprocess / os.system calling sort, sftp, gpg or database loaders with arguments from job parameters or record fields.
    Idempotency and restart: checkpoint files or "processed" markers in a world-writable directory; a rerun after partial failure double-posts records.
  }
}
