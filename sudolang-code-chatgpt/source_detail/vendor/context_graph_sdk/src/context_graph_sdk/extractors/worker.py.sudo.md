# vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py.evidence.json`. SHA-256: `7913d6ef288f772c59badc615689579ac37a9ba72377e47050f701bb3a0327d1`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import pickle; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import cast; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:23-26
In source order: Resolve source import from context_graph_sdk._process import ByteReader, ByteWriter; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.errors import ModelValidationError; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.records import FileExtraction; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.extractors.runtime import MAX_SOURCE_BYTES; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:29-36
// Source signature: extract_work_item(root: str, relative_path: str, language: str) -> FileExtraction
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extract_work_item(root, relative_path, language) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:30-33
  In source order: Retain source documentation literal source_literal_30_4; it is not a model call. Then Resolve source import from context_graph_sdk.extractors.extract import extract_file; preserve alias and import-time effects. Then Evaluate once Path(root) / relative_path; assign in source target order to path.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:34-35
  if (the source predicate path.stat().st_size > MAX_SOURCE_BYTES is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:35-35
    Raise ModelValidationError('source exceeds the extraction size bound').
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:36-36
  End this invocation with extract_file(relative_path, path.read_bytes(), language).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:39-93
// Source signature: extraction_worker(root: str, requests: ByteReader, responses: ByteWriter, max_request_bytes: int, max_result_bytes: int) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn extraction_worker(root, requests, responses, max_request_bytes, max_result_bytes) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:46-46
  In source order: Retain source documentation literal source_literal_46_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:47-93
  Perform the following protected operations {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:48-90
    while (the source predicate True is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:49-52
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:50-50
        In source order: Evaluate once requests.recv_bytes(max_request_bytes); assign in source target order to payload.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:51-52
      On the first matching source exception EOFError, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:52-52
        End this invocation with None.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:53-54
      if (the source predicate not payload is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:54-54
        End this invocation with None.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:55-79
      Perform the following protected operations {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:56-56
        In source order: For decoded, assign pickle.loads(payload); source annotation object.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:57-58
        if (the source predicate not isinstance(decoded, tuple) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:58-58
          Raise ValueError('invalid request shape').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:59-59
        In source order: Evaluate once cast(tuple[object, ...], decoded); assign in source target order to request.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:60-66
        if (the source predicate len(request) != 3 or not isinstance(request[0], int) or (not isinstance(request[1], str)) or (not isinstance(request[2], str)) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:66-66
          Raise ValueError('invalid request shape').
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:67-69
        In source order: Evaluate once request[0]; assign in source target order to index. Then Evaluate once request[1]; assign in source target order to relative_path. Then Evaluate once request[2]; assign in source target order to language.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:70-77
        Perform the following protected operations {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:71-75
          In source order: For result, assign (index, True, extract_work_item(root, relative_path, language)); source annotation tuple[int, bool, object].
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:76-77
        On the first matching source exception BaseException as error, in handler order {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:77-77
          In source order: Evaluate once (index, False, source_template_77_44); assign in source target order to result.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:78-79
      On the first matching source exception Exception as error, in handler order {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:79-79
        In source order: Evaluate once (-1, False, source_template_79_37); assign in source target order to result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:80-80
      In source order: Evaluate once pickle.dumps(result, protocol=pickle.HIGHEST_PROTOCOL); assign in source target order to response.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:81-89
      if (the source predicate len(response) > max_result_bytes is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:82-89
        In source order: Evaluate once pickle.dumps((result[0], False, source_template_86_24), protocol=pickle.HIGHEST_PROTOCOL); assign in source target order to response.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:90-90
      In source order: Evaluate responses.send_bytes(response); retain side effects and discard the expression result.
    }
  }
  On every exit from this protected/handler/normal-completion region {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/extractors/worker.py:92-93
    In source order: Evaluate requests.close(); retain side effects and discard the expression result. Then Evaluate responses.close(); retain side effects and discard the expression result.
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk._process import ByteReader, ByteWriter` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/_process.py.sudo.md`.
- `from context_graph_sdk.errors import ModelValidationError` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/errors.py.sudo.md`.
- `from context_graph_sdk.extractors.records import FileExtraction` at source line 25: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/records.py.sudo.md`.
- `from context_graph_sdk.extractors.runtime import MAX_SOURCE_BYTES` at source line 26: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/runtime.py.sudo.md`.
- `from context_graph_sdk.extractors.extract import extract_file` at source line 31: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/extractors/extract.py.sudo.md`.
