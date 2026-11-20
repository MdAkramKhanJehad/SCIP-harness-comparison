# SudoLang representation of vvaharness

**Status: batch 1; partial conversion.** The whole harness is not yet converted.
Start with [representation conventions](representation_specification.md), then
[scan entry](representation/vvaharness/orchestrator/entry.sudo.md) and
[scan workflow](representation/vvaharness/orchestrator/scan.sudo.md).

This batch represents the scan command, orchestrator, checkpoint facade, and S4
investigation scheduling/session/prompt construction, including three middleware
components. Calls into other modules are explicit boundaries awaiting conversion.
The file-level [coverage ledger](coverage.tsv) includes every supplied harness file,
including the vendored SDK. An inventory or an exact asset copy is not a conversion.

Deliverables:

- [Representation specification](representation_specification.md)
- [Mirrored pseudocode tree](representation/)
- [Vocabulary additions](vocabulary_extensions.md)
- [Conversion notes, limits, and manual checks](conversion_notes.md)
- [Coverage ledger](coverage.tsv) and [SudoLang reading record](baseline_review.tsv)

The supplied [SudoLang repository](https://github.com/paralleldrive/sudolang) is
pinned locally in `reference/sudolang/`. The baseline is `sudolang.sudo.md`, v2.0.
Functions, interfaces, assignments, `if`/`else`, `while`, `for each`, and natural
language statements suffice for this batch. No grammar extension is proposed.

The output is documentation for analysis, not an instruction to run a security
scan or to emulate missing dependencies. No scan or model invocation was run.
