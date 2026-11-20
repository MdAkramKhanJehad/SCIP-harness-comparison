w# Original conversion instructions

The following is the user-supplied prompt, preserved verbatim.

I will provide:
1. The SudoLang repository/specification (read it full): https://github.com/paralleldrive/sudolang , https://github.com/paralleldrive/sudolang/tree/main/examples  
2. A vulnerability-detection harness: visa-vulnerability-agentic-harness/ 
use sudolang-code-chatgpt/ for all of this. 

Your task is to represent the harness as pseudocode using SudoLang. This representation will support systematic analysis of the harness’s design decisions and behavior.

First, read the SudoLang specification and go through all examples in the supplied SudoLang repository to understand its constructs, conventions, and abstraction style. Then examine the harness source. If anything is inaccessible, identify what you could not inspect. Do not invent syntax, source behavior, or specification details.

1. Establish the representation specification

Use SudoLang as the baseline. Determine whether its existing constructs can represent the harness through vocabulary additions alone.

Prefer existing constructs for conditions, loops, functions, and other behavior. Do not introduce new grammar merely because the harness uses unfamiliar concepts.

Distinguish:
- Constructs defined by the SudoLang specification.
- Harness-specific vocabulary or identifiers introduced within those constructs.
- Proposed language extensions, if existing constructs genuinely cannot express something.

If an extension appears necessary, document the source behavior requiring it, why existing constructs are insufficient, and the proposed change. Do not silently present extensions as standard SudoLang.

2. Generate the harness representation

Represent behavior supported by the source, including relevant executable code, prompts, configuration, and available dependency code.

Maintain the harness flow hierarchy: preserve how the overall workflow is organized into stages, components, substeps, and nested operations, as supported by the source. Preserve their ordering, branching, calling relationships, and parallel execution where specified. Do not flatten the workflow into an unrelated list of operations or invent a hierarchy absent from the source.

Also preserve the original directory and file organization where practical. Clearly map each generated file or section to its original source.

Use an abstraction level that makes the harness’s decisions and workflow understandable. Preserve details relevant to later analysis, including:
- Component ordering and conditional transitions.
- Filters, gates, thresholds, and cutoffs.
- Loops, retries, and termination conditions.
- Model calls and instructions given to models.
- Tool availability and decisions about invoking tools.
- Parallel operations, shared state, and synchronization where specified.

Distinguish behavior enforced by executable code from behavior requested through prompts or left to the model. Do not turn a prompt instruction into a guaranteed execution step or assume that an available tool is always called.

Do not invent ordering, synchronization, checks, or dependency behavior. When behavior cannot be determined from the available material, mark it as unresolved and identify the missing evidence.

Preserve apparent contradictions and unusual behavior rather than correcting them during conversion. The objective is faithful representation, not redesign.

Avoid unnecessary line-by-line expansion. If an abstraction would hide a relevant decision or behavior, retain the necessary detail and explain why.

3. Maintain a separate vocabulary extension record

Create a separate file named vocabulary_extensions.md.

Record every vocabulary term or identifier you introduce beyond the supplied SudoLang baseline. For each entry, include:
- Term or identifier.
- Definition and intended meaning.
- Why it is needed.
- Whether it is a general harness concept or a tool-specific identifier.
- Original source term or wording, if different.
- Source references supporting its meaning.
- Where it is used in the generated representation.
- Whether it is newly introduced or reused from a supplied vocabulary extension.

Distinguish ordinary identifier additions from grammar changes. Do not claim that a user-defined identifier changes the SudoLang language.

Use consistent terminology throughout. Reuse supplied vocabulary when the meaning matches; do not merge concepts merely because their names are similar. Preserve differences in their roles, conditions, and positions in the workflow.

If grammar changes are proposed, record them separately in language_extension_proposals.md.

4. Make the conversion traceable and reviewable

For each substantive pseudocode block, provide the original source path and line range where available. For extracted prompts, include the source location of the prompt.

Review the representation against the source for omitted conditions, altered ordering or hierarchy, invented behavior, and inconsistent vocabulary. Clearly distinguish what you checked from what remains unverified.

Keep a conversion_notes.md file documenting:
- The SudoLang and harness versions or commits, if available.
- The specification and repository examples reviewed, including any inaccessible examples.
- The conversion instructions and any subsequent revisions.
- Files covered and files not covered.
- Abstraction choices and their rationale.
- How the harness flow hierarchy maps to the representation.
- Unresolved behavior and missing source material.
- Source-to-representation examples suitable for manual checking.

Do not claim that model-generated output or agreement between models proves correctness.

5. Keep the scope focused

Produce the representation, its vocabulary record, and conversion documentation. Do not perform downstream flaw analysis, redesign the harness, or invent test results.

If the harness is too large to process at once, work in clearly identified batches and maintain a coverage record. Never present a partial conversion as complete.

Deliver:
1. A brief description of the SudoLang baseline and representation conventions.
2. The SudoLang pseudocode, maintaining the harness flow hierarchy and corresponding source organization.
3. vocabulary_extensions.md.
4. language_extension_proposals.md, only if needed.
5. conversion_notes.md.