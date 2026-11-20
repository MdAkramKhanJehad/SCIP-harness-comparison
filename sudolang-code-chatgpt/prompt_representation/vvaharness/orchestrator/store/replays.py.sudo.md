# vvaharness/orchestrator/store/replays.py — model instruction carriers

Model-request representation: these constraints describe instructions addressed to a model.
They do not execute the host workflow, prove compliance, or require every available tool to be called.
Supply boundary: each request applies only if and when its source caller/loader supplies this content. A text classification alone does not establish delivery; the workflow map and executable source view record supported supply relationships.
Independent clauses remain unordered unless the source explicitly says first/then/before/after or gives procedural steps.
Qualitative words, exceptions, contradictions and example values retain their source meanings.
Exact originals are supporting evidence; the Constraints/conditional blocks below are the behavioral representation.

## save_replays — source lines 33–33

Source context: callable `save_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:33-33
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')
}
```

## save_replays — source lines 35–35

Source context: callable `save_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:35-35
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: UPDATE runs SET updated_at = datetime('now') WHERE run_id = ?
}
```

## save_replays — source lines 37–37

Source context: callable `save_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:37-37
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DELETE FROM ev_replays WHERE run_id = ?
}
```

## cur — source lines 94–94

Source context: callable `delete_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:94-94
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DELETE FROM ev_replays WHERE run_id = ?
}
```

## save_ev_probes — source lines 117–117

Source context: callable `save_ev_probes`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

Exposure boundary: this instruction-bearing text may instead be a host diagnostic. Apply this model-request view only if its caller supplies the text to a model; no such supply is invented.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:117-117
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: INSERT OR IGNORE INTO runs(run_id, repo_root) VALUES (?, '')
}
```

## save_replays — source lines 44–45

Source context: callable `save_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:44-45
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: INSERT OR REPLACE INTO ev_replays(run_id, finding_key, payload, size) VALUES (?, ?, ?, ?)
}
```

## prune_replays — source lines 64–64

Source context: callable `prune_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:64-64
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: DELETE FROM ev_replays WHERE run_id = ? AND finding_key = ?
}
```

## rows — source lines 76–77

Source context: callable `load_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:76-77
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SELECT finding_key, payload, size FROM ev_replays WHERE run_id = ? ORDER BY created_at, finding_key
}
```

## rows — source lines 60–60

Source context: callable `prune_replays`; enclosing call `con.execute`; keyword `none`.
Executable assembly/branches remain in the matching source_detail module. This view converts the message content, not its surrounding code.

```sudo
// Source: vvaharness/orchestrator/store/replays.py:60-60
Constraints {
  The request retains this source rule, criterion or rationale, with its original modal force: SELECT finding_key FROM ev_replays WHERE run_id = ?
}
```

