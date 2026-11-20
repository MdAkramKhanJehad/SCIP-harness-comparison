# vvaharness/backends/harness/deepagents/profiles.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## _READ_BEFORE_ANSWERING — source lines 33–36

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:33-36
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: <investigate_before_answering> Never describe code the model have not opened.
  The request retains this source rule, criterion or rationale, with its original modal force: Reading one file and generalising from it is the single most common way this task is failed: the answer is graded on what is actually in the repo, not on what a repo of this kind usually contains.
  The requested conditional/temporal rule is: Before the model commit to any answer, open every file your answer depends on.
  The requested conditional/temporal rule is: If the model have named a path, the model must have read it.
  The requested conditional/temporal rule is: If a tool returned nothing, that is a fact about your query, not a fact about the repo — re-query differently rather than concluding the thing is absent. </investigate_before_answering>
}
```

## _PARALLEL_TOOL_CALLS — source lines 38–41

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:38-41
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: <use_parallel_tool_calls> Decide every file and lookup the model need, then issue those calls together in one batch rather than one at a time.
  The request retains this source rule, criterion or rationale, with its original modal force: Reading five files is five calls in parallel, not five sequential turns.
  The request retains this source rule, criterion or rationale, with its original modal force: Only serialise a call whose arguments genuinely depend on a previous result.
  The requested model behavior excludes guess a parameter or use a placeholder to avoid a lookup. </use_parallel_tool_calls>
}
```

## _REFLECT_IN_WRITING — source lines 43–46

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:43-46
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: <tool_result_reflection> After each batch of tool results, state to yourself what the model now know that the model did not before, and what is still unverified.
  The request retains this source rule, criterion or rationale, with its original modal force: Let that decide the next batch.
  The requested model behavior excludes proceed to the final answer while a load-bearing claim is still unverified. </tool_result_reflection>
}
```

## _REFLECT_WITHOUT_WRITING — source lines 48–51

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:48-51
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: <tool_result_reflection> After each batch of tool results, settle what the model now know that the model did not before, and what is still unverified, and let that decide the next batch — but do not write that stocktake out.
  The request retains this source rule, criterion or rationale, with its original modal force: It is a decision, not a deliverable, and on this route everything the model write is generated text that the answer has to be reached through.
  The requested model behavior excludes proceed to the final answer while a load-bearing claim is still unverified. </tool_result_reflection>
}
```

## _ENUMERATE_DO_NOT_SUMMARISE — source lines 53–56

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:53-56
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: <enumerate_do_not_summarise> When the output schema asks for a list, the list is the deliverable and its length is part of the answer.
  The request retains this source rule, criterion or rationale, with its original modal force: One broad item that folds several distinct cases together is a worse answer than several narrow items, and anything the model fold in is lost — nothing downstream can recover it.
  The request retains this source rule, criterion or rationale, with its original modal force: Exhaust the cases the model have evidence for before the model stop.
  The requested model behavior excludes stop at the first few because they feel representative, and do not merge two cases because they happen to share a file. </enumerate_do_not_summarise>
}
```

## _BEAT_THE_CLOCK — source lines 58–63

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:58-63
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: <the_clock_is_part_of_the_task> the model are on a wall clock and it is shorter than this work takes if the model narrate it.
  The request retains this source rule, criterion or rationale, with its original modal force: A session that runs out of time is not trimmed at the end — it is cut off and restarted from its own transcript, so every second spent on text the model did not have to produce is paid twice and the second pass starts from nothing.
  The request retains this source rule, criterion or rationale, with its original modal force: Three habits cost the whole budget and buy no coverage: writing the model's reasoning out rather than reasoning and moving on, restating a tool result the model have already been shown, and spending a turn per file where one batch would have answered the question.
  The requested evidence/output includes what you read as `path:line` and go on.
}
```

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:58-63
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: None of this is licence to answer with less.
  The request retains this source rule, criterion or rationale, with its original modal force: The number of items the model emit is set by the evidence and is never reduced to make the clock; a short answer that omits half the repo is the expensive outcome, not the cheap one.
  The request retains this source rule, criterion or rationale, with its original modal force: Shorten the path to the answer, never the answer. </the_clock_is_part_of_the_task>
}
```

## _DO_NOT_NARRATE — source lines 65–68

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:65-68
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: <do_not_narrate> Everything the model write before the final answer is taken out of the room the answer itself has to fit in, and a reply cut off mid-structure is discarded whole rather than truncated.
  The request retains this source rule, criterion or rationale, with its original modal force: So do not restate, quote or paraphrase code the model have read — cite it as `path:line` and move on.
  The requested model behavior excludes narrate your plan or your progress.
  The requested model behavior excludes summarise your own tool results back to yourself in writing.
  The request retains this source rule, criterion or rationale, with its original modal force: This shortens the sentences and never the list: the number of items is set by the evidence and is never reduced to save room. </do_not_narrate>
}
```

## __all__ — source lines 24–24

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:24-24
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: PER_MODEL_PROFILE_KEYS
}
```

## __all__ — source lines 25–25

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:25-25
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: PROFILED_PROVIDERS
}
```

## __all__ — source lines 26–26

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:26-26
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: STAGE_PROFILE_KEYS
}
```

## __all__ — source lines 27–27

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:27-27
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: register_vvah_harness_profiles
}
```

## __all__ — source lines 28–28

Source context: callable `<module>`; enclosing call `none`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/backends/harness/deepagents/profiles.py:28-28
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: stage_profile_suffix
}
```

