# Qualitative analysis of conflicts and contradictions in VulnHunter and VVAH

This folder compares two vulnerability-detection harnesses in three layers. The first two layers ask where the two harnesses make incompatible choices. The third layer examines low-level contradictions within each harness and between the two harnesses.

| Layer | Question | File |
|---|---|---|
| One: high-level design | Where do the two harnesses make opposite architectural decisions? | `01-high-level-design-conflicts.md` |
| Two: mechanisms | Where do comparable mechanisms follow rules that cannot both hold? | `02-mid-level-conflicts.md` |
| Three: contradictions inside VulnHunter | Where does VulnHunter disagree with itself? | `03-low-level-contradictions-within-vulnhunter.md` |
| Three: contradictions inside VVAH | Where does VVAH disagree with itself? | `04-low-level-contradictions-within-vvah.md` |
| Three: contradictions between the harnesses | Which specific rules make VVAH and VulnHunter treat the same case differently? | [05-low-level-contradictions-between-vvah-and-vulnhunter.md](05-low-level-contradictions-between-vvah-and-vulnhunter.md) |

The two harnesses are VulnHunter (a collection of prompt-driven Claude Code skills with a Python launcher; repository `VulnHunter/`, commit 6d25b5c) and VVAH, the Visa Vulnerability Agentic Harness (a Python pipeline of stages that call models; repository `visa-vulnerability-agentic-harness/`, package `vvaharness` version 1.5.1, commit 0e6f00d). Neither repository was modified.

## How to read the layers

Start with layer one for the shape of each harness and the reasons the two cannot be compared knob for knob. Use layer two when a particular mechanism matters (severity, verification, deduplication, context, tools, fixing). Use layer three to find places where a harness does not do what its own text says; these matter whenever a knob is treated as a lever, because a lever that is ignored, inert or overridden will show no effect.

Each finding gives its evidence as `path:line` relative to the harness repository, with knob identifiers in code formatting. Knob identifiers come from the registries `../vulnhunter.knobs.yaml` and `../vvah.knobs.yaml`; the rendered pseudocode is in `../pseudocode/`.

## Evidence labels

- **Verified in source.** The cited lines were opened and the text says what is claimed.
- **Verified in earlier reading.** The fact was read in the source earlier in this study and recorded in research notes with its location, but the line was not reopened when the document was written.
- **Verified in pseudocode only.** The fact appears in the rendered pseudocode and in the registry, but the source line was not independently reopened.
- **Inferred.** The conclusion follows from verified facts and is not stated in the source. Inferred conclusions are marked so that they can be tested.

## How the analysis was checked

All citations and quotations in layers one and two were checked mechanically with `verify_citations.py`: every cited file must exist, every cited line must be inside the file, and every quotation of three or more words must occur near a cited line. While that check was being prepared, several statements in the first drafts were found to be wrong and were corrected (for example, the consensus rule in VulnHunter's verification phase eliminates candidates by agreement and does not skip the verification of agreed candidates, which reversed the point of one conflict). The layer-three documents were produced by two reviewers, one per harness, who were required to confirm each finding in both places in the source and to list candidates they could not confirm.

## Limits

- The analysis reads text and configuration. It does not run either harness, so statements about consequences describe what the text and code imply, not measured behaviour. Where a consequence depends on how a model behaves, the evidence label is *inferred*.
- Exploit verification in VVAH (its optional live-attack stage) was excluded from this study by decision and is mentioned only where needed to describe the design.
- Layer three is a sample of confirmed contradictions, not a proof that no others exist.

## Glossary

Terms are written out in full throughout the documents. Where a name is a literal identifier (a file, function, knob or enumeration value) it is shown in code formatting exactly as it appears in the source.

- **Adversarial verification:** a pass whose job is to try to refute a candidate finding.
- **Common Weakness Enumeration:** the public catalogue of software weakness types; a weakness label looks like CWE-79.
- **Common Vulnerability Scoring System:** a standard method for scoring severity from a vector of attributes.
- **Disposition:** the outcome recorded for an input after tracing it (candidate, safe, no match, cross class, design intent).
- **Hard gate:** a condition a candidate must satisfy before it is recorded.
- **Knob:** any value, rule or switch that can be changed to change behaviour, whether it lives in a configuration file, in prompt text or in a code constant.
- **Profile:** a shipped configuration file that overrides VVAH's built-in defaults.
- **Route:** one of the ways VVAH reaches a model (command line, software development kit, OpenAI-compatible interface, deepagents graph).
- **Stage and phase:** VVAH is divided into numbered stages and VulnHunter into named phases; each is named with its meaning where used.
- **Sink:** a place in the code where dangerous input would cause harm, such as a database query or a command invocation.
