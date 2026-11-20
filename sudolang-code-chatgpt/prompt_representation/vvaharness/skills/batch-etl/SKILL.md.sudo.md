# vvaharness/skills/batch-etl/SKILL.md — model instructions

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## Batch trust-boundary gate

Structured view of the same source instructions, not an additional pass or an assertion of model compliance.

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:24-59
Constraints {
  The requested attacker model is an upstream producer, scheduler/operator parameter or shared landing-directory writer, not an interactive web user.
  A requested finding must cite an externally influenced job/env/record/filename value and the file:line where unvalidated data reaches a path, command, SQL or output record.
  if (producer and consumer share one trust domain and no lower-privileged party can set the value) { The model is asked to drop it. }
  Requested analysis covers canonical base-directory confinement, record-derived path collisions, planted/newest files and TOCTOU, COMP-3/EBCDIC length/sign/zone validation and COBOL/Python indexing differences, trailer counts/hash totals, CSV formula prefixes = + - @, shell/tool arguments, and writable restart/checkpoint state causing double posting.
  The search list is non-exhaustive; no precise exploitability cutoff is added.
}
```

Supply relationship: skills/__init__.py discovers SKILL.md packages and injects temporary copies; S4/S6 route options decide availability. Reading/activation is model-selected except where a prompt requests it.

## Declared request metadata

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:1-4
Constraints {
  The source declares name = "batch-etl". Tool lists here describe the request profile; source loaders determine actual grants.
  The source declares description = "Find defects specific to batch and ETL paths: unvalidated bulk input, injection through generated statements, and trust placed in upstream-written data.". Tool lists here describe the request profile; source loaders determine actual grants.
  The requested search/review target is defects specific to batch and ETL paths: unvalidated bulk input, injection through generated statements, and trust placed in upstream-written data.
}
```

# Batch Etl Lens

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:24-27
Constraints {
  The requested model role and scope are a Batch / ETL data-pipeline expert.
  The request retains this source rule, criterion or rationale, with its original modal force: The target is a file-in → transform → file-out job (mainframe-migrated or scheduler-driven).
  The request retains this source rule, criterion or rationale, with its original modal force: The attacker model is: an upstream producer, scheduler/operator parameter, or shared landing directory — NOT an interactive web user.
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:29-34
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: HARD GATE — for every finding cite (a) the externally-influenced value (job parameter, env var, upstream record field, filename in a watched dir) and (b) the file:line where it reaches a path, command, SQL, or output record WITHOUT validation.
  The requested conditional/temporal rule is: If both producer and consumer are inside the same trust domain and the value cannot be set by a lower-privileged party, DROP it.
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:36-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Where to look first (non-exhaustive — reason beyond this list):
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:37-40
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Job parameters / env vars (sys.argv, os.environ, JCL PARM=, scheduler variables) flowing into open()/Path()/shutil.* / os.remove without a fixed base-directory + realpath check — path traversal lets an upstream caller read/overwrite arbitrary files as the batch service account
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:41-42
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The requested model reply must contain filenames or staging dirs derived from input RECORD fields (account no, merchant id) — traversal / collision via crafted records
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:43-45
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Shared landing / spool directories: glob('*.dat') or "pick newest by mtime" where any writer to that dir can plant a file the job will ingest or overwrite (TOCTOU / untrusted-producer)
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:46-50
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Fixed-width / packed-decimal (COMP-3) / EBCDIC parsing: length taken from the record header and used to slice/seek without capping to the buffer; sign-nibble / zone-nibble not validated → negative amounts or index wrap; off-by-one between COBOL 1-based PIC offsets and Python 0-based slices
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:51-52
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Record-count / hash-total trailer NOT verified against the body — truncation or injection of extra records goes undetected
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:53-55
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Emitted CSV / report files: cells sourced from input records written without stripping leading = + - @ (formula injection into downstream Excel consumers)
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:56-57
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: subprocess / os.system invoking sort, sftp, gpg, db loaders with arguments built from job params or record fields
}
```

```sudo
// Source: vvaharness/skills/batch-etl/SKILL.md:58-59
// Source list marker -; preserve its source grouping, not an invented execution order.
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: Idempotency / restart: checkpoint files or "processed" markers in a world-writable dir; rerun after partial failure double-posts records
}
```

