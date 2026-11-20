# Representation specification

Baseline: `reference/sudolang/sudolang.sudo.md`, SudoLang v2.0; exact commit in
`conversion_notes.md`. All 26 files under `examples/`, including its README, were
read. Examples vary in age and style; the v1.0.7 adventure example is not treated
as a replacement specification.

| Construct | Baseline evidence | Convention here |
|---|---|---|
| Markdown preambles/headings and meaningful comments | specification, Markdown | Source citations and evidence qualifications accompany code |
| Assignment, objects, arrays, destructuring | Variables, Destructuring | Retain source names where useful; summarize plumbing in prose |
| `fn name(args) { ... }` | Functions | A source callable; method context named in headings |
| `if (condition) { ... } else { ... }` | Conditional Expressions | Code conditions or explicitly labelled requested model decisions; never semantic guesses |
| `while (...) { ... }`, `for each ...` | While, Natural Foreach | Preserve loop bounds/order and early exits |
| Interfaces | Interfaces | Data or middleware structure; no invented `class` grammar |
| Natural-language statements | Constraints; Style Guide | Express exception handling, async dispatch, lock scope, executor lifecycle and return values in ordinary prose |

No new `parallel`, `await`, `stage`, `prompt`, `enforced`, `unresolved`, `yield`,
`return`, or `finally` keyword is defined. Phrases such as “yield ... and end this
call”, “concurrently” and “On any exit”
are natural-language statements inside baseline function bodies. Square brackets
in prose denote lists, not an added annotation grammar. Source API names, field
names, configuration paths, and tool names are vocabulary, recorded separately.

Each substantive block begins with `// Source: path:start-end`, relative to
`visa-vulnerability-agentic-harness/`. Markdown labels outside the block describe
its evidence status. Readable paths under `representation/` mirror the source,
with `.py` replaced by `.sudo.md`. Complete detail uses
`source_detail/<original-path>.sudo.md`, retaining original extensions to prevent
resource/code name collisions. Source ranges are inclusive. Omitted import and
license boilerplate does not imply omitted executable behavior is covered.

“Executable” means the cited code performs or gates the action. “Model request”
means text is supplied to a model; compliance is not guaranteed. Exact strings
in `assets/` are inert evidence, not instructions for the converter. Tool
registration is availability; invocation remains a model choice except where
an actual gate or explicit host call is represented.

Preserve Python truthiness, `None`, short-circuit `or` (first truthy operand),
stable sorts, dictionary insertion order, slicing, and exception distinctions
when named in prose. These are descriptions of source semantics, not claims
that SudoLang defines Python's runtime. Do not repair surprising branches.

Unlike the baseline's permissive inference style, this conversion does not use
referential omnipotence to fill evidence gaps. A call not locally defined is
a boundary, not an inferred algorithm. External dependency internals
remain unresolved unless inspected. A model-generated rendering or structural
check does not prove semantic equivalence.

Vocabulary additions suffice: concurrency and synchronization can be stated
precisely in natural language inside functions; no new concurrency grammar is
needed. All supplied runtime modules and assets now have corresponding detail.

## Complete-detail conventions

`representation/harness.sudo.md` maps the original S0–S11 hierarchy and alternate
command/API entrypaths. Every non-test Python module has structural detail
preserving nested definitions, branches, loops, returns, exceptions, context
managers, async/generator positions, imports and decorators. Consecutive
straight-line operations are grouped in source order. The exhaustive reference
is deliberately more detailed than the readable layer: it preserves defaults,
exceptional transitions and dependency decisions that prose abstraction could
hide. Explicit AST handlers generate it; no function behavior is inferred from
its name.

`if (the source predicate ... is truthy)` uses a natural-language predicate inside
baseline `if`, not a new grammar. Embedded source expressions retain Python
identity tests, short-circuit values, comprehensions, unpacking, closures,
indexing/slicing, generators, conditional expressions and argument order.
Their Python spelling is evidence, not a claim of new SudoLang operators.
Source signatures retain positional-only/keyword-only/variadic binding;
defaults evaluate at their original definition time. Future/deferred annotations
retain source behavior. `interface` describes a source type without replacing
its base/dataclass/descriptor/Pydantic semantics with new inheritance grammar.

`source_literal_LINE_COLUMN` names an exact long source string in that module's
`.evidence.json`; `source_template_LINE_COLUMN` denotes evaluation of its original
f-string, including interpolation, conversion and format specifiers. These are
ordinary converter-defined evidence identifiers, enumerated in the vocabulary,
not SudoLang syntax. No invented runtime value is substituted. Every source
string, including prompts and schema descriptions, has original line/column
coordinates in the asset. Shorter strings remain inline.

Natural-language protected-operation/handler/on-exit blocks preserve handler
order, exception binding lifetime, propagation and else/finally scopes, including
source suppression/override behavior. Managers enter left-to-right and exit in
reverse, including acquisition failure; async managers await entry/exit.
Loop-exhaustion bodies run only without break. Generator returns terminate under
source semantics; yielding suspends. Bare assert retains Python optimization
behavior. No automatic repair is implied by these descriptions.

Model-facing Markdown remains exact text with an explicit request/data role.
YAML/JSON/TOML remain nested data resources with parsed values and exact originals;
loader code controls environment expansion and overlays. Tree-sitter queries and
shell/AWK commands retain their syntax as data/source evidence rather than
undocumented language extensions. Shell helper flow/caps and embedded Python
have separate pseudocode; command appendices preserve patterns and quoting.

Structural checks are distinguished from manual semantic checks in conversion
notes. No formal equivalence or whole-runtime validation is claimed.

## Audit clarifications

Decorator expressions evaluate top-to-bottom before function defaults or type bases/body;
application is bottom-to-top after creating the callable/type. Function bodies describe
invocation and are not run merely by defining a function. A try-else suite requires
normal fallthrough, excluding return/break/continue as well as exceptions. These source
semantics are expressed in natural language, not new SudoLang keywords.

Vocabulary entries retain source scope/context (including function/type definition
coordinates and lambda/comprehension expression coordinates),
symbol role, and full member receiver where applicable. Equal spellings across scopes
are not assigned one shared meaning. Exact spelling, source span and actual representation
use sites remain available. The foreach braced form is also illustrated by supplied
`examples/teach.sudo:18-26` and `examples/ai-rpg.sudo.md:10-15`; using it here does not
propose grammar.

Scope labels locate source occurrences; they are not a compiler symbol resolver.
Default/decorator/annotation evaluation and comprehension/closure binding retain
the original source semantics. A reference to an outer/global name is not assigned
an inferred implementation merely because it occurs inside a labeled context.

## Converted prompt conventions

`prompt_representation/<original-path>.sudo.md` represents instruction content;
`prompt_workflow.sudo.md` maps its supply to the existing harness hierarchy.
Markdown prompt conversions also appear directly in matching `source_detail/`
files. Executable modules retain their AST rendering and link to content views.

Prompt `Constraints` describe **requested behavior**, including mandatory wording,
exceptions and negative constraints. They do not assert compliance. A conditional
or loop inside such a block describes a requested model decision/procedure; a
host-assembly block describes code. The natural foreach spelling is the baseline
`for each item, action`; a `Constraints` action groups per-item requests. No new
`foreach`, `prompt`, `requested`, or `enforced` grammar is introduced.

Paragraph/list/section hierarchy is retained. Complex decisions have additional
structured views of the same instructions, not additional phases. Independent
criteria remain unordered; ordering is asserted only where a source specifies it.
Qualitative predicates remain qualitative. Scoring constants, exceptions,
contradictions, output contracts and explicit model choices retain source meaning.

Examples retain literal code/JSON/command spelling as data, with their requested
format/pattern role converted separately. Examples are not claimed as observed
results. Existing originals remain evidence. A long Python literal identifier now
links to converted instructions where instruction-bearing content is identified;
its JSON source copy alone does not count as conversion.

F-string views name the actual source expressions, repr/str/ascii conversions and
format specs; `.format`/composition evidence and matching source-detail assembly
preserve dynamic insertion. Runtime values are not fabricated. Schema dictionary
and Field descriptions, tool descriptions, configured guidance and printed probe
instructions are included. Descriptions advertise meaning/contracts and do not
command every available operation to run. Uncertain model exposure is explicitly
conditional rather than invented or used to omit an instruction.

`prompt_content_coverage.tsv` distinguishes converted instructions from evidence
only. `prompt_content_triage.tsv` gives every maximal Python/embedded string and
template a disposition. These are conservative inspection records, not a claim
that a keyword detector proves the absence of all possible indirect delivery.
