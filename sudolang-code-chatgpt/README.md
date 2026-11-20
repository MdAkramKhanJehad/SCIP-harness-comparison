# SudoLang representation of vvaharness

Start with the [harness workflow](representation/harness.sudo.md) and the [prompt workflow](prompt_workflow.sudo.md). The prompt conversion now includes behavioral instructions, not just copies of prompt text.

| Output location | Meaning |
|---|---|
| `representation/` | Readable scan stages, orchestration, components, configuration and shell flow |
| `source_detail/` | Source-mirrored detailed pseudocode; Markdown prompts contain converted instructions, and code/data views link to their prompt conversions |
| `prompt_representation/` | Converted roles, procedures, gates, constraints, tool guidance, model choices and output requirements, mirroring original source paths |
| `assets/` | Supporting exact source strings, expressions and resource copies; these are evidence, not the behavioral conversion |
| `reference/sudolang/` | Pinned specification and all supplied examples |
| `tools/` | Conversion, indexing and static review scripts |
| `history/` | Earlier partial-delivery records; not current coverage |

For example, [crypto instructions](source_detail/vvaharness/skills/crypto/SKILL.md.sudo.md) contain requested review decisions and exclusions; [validation system instructions](prompt_representation/vvaharness/validation/prompts/system.md.sudo.md) contain the requested parent/persona procedure.

The conversion covers 542 production Python modules, two embedded Python blocks and 132 other supplied resources. All 945 supplied files are inventoried; 271 tests/fixtures remain explicitly excluded from production conversion. Prompt review triages every maximal Python string/template and separately classifies every non-test resource. Of these sources, 215 have converted instruction views: 27 Markdown files, 179 Python files, four guidance/configuration files and five shell feedback files.

SudoLang v2.0 supplies functions, interfaces, `Constraints`, conditions, `for each`, `while` and natural-language statements. Source names reuse the existing vocabulary where meanings match. No grammar extension is needed. Host execution, model requests and model-selected choices are labelled separately; conditional supply does not imply compliance or tool invocation.

- [Representation conventions](representation_specification.md)
- [Vocabulary record](vocabulary_extensions.md)
- [Conversion notes, manual review anchors and limitations](conversion_notes.md)
- [Requirements review](requirements_review.md)
- [Source index](source_index.md) and [per-file coverage](coverage.tsv)
- [Prompt content coverage](prompt_content_coverage.tsv), [carrier triage](prompt_content_triage.tsv) and [prompt verification](prompt_verification.json)
- [Structural verification](verification.json), [source/output audit](audit_results.json) and [dependency boundaries](dependency_boundaries.md)

Static checks establish artifact consistency and coverage properties; they do not prove semantic equivalence or model compliance. Unavailable dependency internals, runtime values and actual model choices remain unresolved. No harness source was changed and no scan, model call, exploit verification or remediation was run.
