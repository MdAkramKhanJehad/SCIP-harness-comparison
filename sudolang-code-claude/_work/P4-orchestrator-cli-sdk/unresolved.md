# Unresolved: P4-orchestrator-cli-sdk

- vvah/vvaharness/orchestrator/store/_schema.sudo — _DDL_V2 and _DDL_V3 do not create ix_runs_updated, so a migrated database has it only if the version 1 schema created it — missing evidence: the version 1 DDL, which is not in the source

No source file in this area was unreadable. No grammar change to SudoLang was needed.

## Drift found in scan.sudo (not edited, per brief)

- scan.sudo Stage 1 comment "// model role: preprocess" and Stage 3 comment "// model role: decompose": neither `pipeline/stages/s1_preprocess.py` nor `pipeline/stages/s3_decompose.py` makes a model call (no backend call in either; `sdk/stages.py:80` says s3 is "deterministic: one InvestigationUnit per threat, zero model calls"). `scan.py:598-599` and `:675-676` only use `_m("preprocess")` / `_m("decompose")` as console labels.
- Harness source comment `orchestrator/entry.py:323` cites "scan.py :917-920, :950-952", which no longer match scan.py (source-side staleness, not a rendering defect).
