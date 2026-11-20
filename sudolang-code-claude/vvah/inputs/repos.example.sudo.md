# inputs/repos.example.csv

Example batch input: the repositories a batch scan clones and scans, each with its application id.

Source: `inputs/repos.example.csv` (lines 1-18)
Executor: code (data)
Called from: `vvaharness/orchestrator/batch.py` (see orchestrator/batch.sudo)

// src: inputs/repos.example.csv:15-18
Options {
  columns: [AppId, RepoName, Path]
  rows: [["1", "repo1", "https://github.com/example-org/repo1.git"], ["2", "repo2", "https://github.com/example-org/repo2.git"], ["3", "repo3", "git@github.com:example-org/repo3.git"]]
}
