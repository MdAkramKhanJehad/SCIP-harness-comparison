# Optional shell procedures and transcript hook

These are executable scripts made available with skills/settings. A model being
told about a probe does not imply it runs the script. Each script has a mirrored
`source_detail/<source>.sudo.md` with its exact ordered command fragments, includes,
exclusions and regexes. This view summarizes control flow without reproducing each
regex as prose. Shell built-ins, grep/awk/sed behavior and external process execution
remain interpreter/tool boundaries; source commands, argument quoting and status
operators are retained verbatim so no shell grammar is invented for SudoLang.

## Shared helper patterns with distinct implementations

```sudo
// Source: vvaharness/skills/injection/probe.sh:18-40
fn hits(label,pat,remaining_arguments) {
  ROOT=first argument to script, default "."; CAP=20; use exact source XD exclusions.
  Print label; grep recursively with extended regex and line numbers, excluding binary matches,
    with supplied pattern/remaining arguments/root; suppress stderr and tolerate grep nonzero.
  if (captured output is empty) { print "(none)" }
  else { print total count and first CAP lines }
}
fn count(label,pattern) {
  Print label; grep matching file names then count lines and strip spaces.
  This counts files, not total match occurrences.
}
```

The injection script invokes these helpers in literal source order: injection
candidate classes, then defense census. Its hard-gate message is printed guidance;
the script does not apply the model's later exploitability judgment itself.

```sudo
// Source: vvaharness/skills/sensitive-data/probe.sh:18-79
fn sensitive_data_probe() {
  Use ROOT default ".", CAP=20, source XD exclusions and sensitive-name expression SENS.
  hits uses grep -rEni (case-insensitive), rather than injection's case-sensitive -rEn.
  Execute error/debug, logging, response/serialization, storage, headers/transport,
    debug/admin-route and settings-constant sections in source order.
  Empty results print "(none)"; nonempty results print count and first 20 hits.
  Preserve CFG/TPL include flags and exact regex arguments from the command evidence.
  End with status 0; printed candidates are not host-validated findings.
}

// Source: vvaharness/skills/iac/probe.sh:18-127
fn iac_probe() {
  Use ROOT default ".", CAP=20 and source XD exclusions.
  hits: case-insensitive recursive line matches, count and cap.
  flist: matching file names via grep -rElI, sort, count and cap.
  nlist: find files while pruning only the source-listed directory names, sort, count and cap.
  First inventory manifest families, then run Terraform/CloudFormation, container,
    Kubernetes, pipeline and remaining source sections in their literal order.
  No absent platform automatically becomes an executable finding; preserve the printed wording.
  End with status 0.
}

// Source: vvaharness/skills/missing-controls/probe.sh:19-163
fn missing_controls_probe() {
  Disable pathname expansion; ROOT defaults "."; initial CAP=MC_PROBE_CAP or 12; WIDTH=140.
  scan constructs --include flags from space-separated globs, then extended regex recursive grep.
  scan2 pipes first match stream through case-insensitive second regex (site AND keyword).
  Both count all captured lines, print at most CAP lines clipped to WIDTH, and note omitted hits.
  files prints matching filenames, with independent cap 15, not CAP.
  Change CAP to 15 for site enumeration, 6 for control-presence sections, 12 for posture sections.
  Preserve source order: sites/credentials/state-change/cookie/session/storage/data/config,
    then controls, then debug/TLS/hash posture. End with status 0.
}

// Source: vvaharness/skills/ssrf/probe.sh:19-174
fn ssrf_probe() {
  Disable pathname expansion; ROOT defaults "."; CAP=SSRF_PROBE_CAP or 12; WIDTH=140.
  scan adds include flags, captures recursive regex matches, prints empty marker or count/capped clipped hits.
  A nonempty scan sets shared FOUND=1. count prints count and only three sample lines.
  Run ecosystem fetch sinks, indirect mechanisms, URL contracts and fetch-named helpers.
  For call sites, filter definition-looking lines, cap by current CAP and clip WIDTH.
  Run request-source section; copy FOUND to SINKS BEFORE posture scan changes FOUND.
  CAP=8 for redirect/resolution/allowlist posture; count internal-target/scheme strings.
  Print declared-client dependency matches capped at 12.
  if (SINKS is nonempty) { print the literal bypass/redirect/rebinding/target reference heredoc }
  End with status 0. Reference text is advice printed by script, not another executed test.
}

// Source: vvaharness/skills/client-side/probe.sh:19-199
fn client_side_probe() {
  ROOT defaults "."; retain separate EXC/JS/TPL/CFG/SRV include/exclude strings.
  scan(label,include_flags,regex,cap=10) uses grep -rEnIs; empty prints marker and returns 0.
  Nonempty output prints first cap lines, clips displayed lines after 200 characters, notes total when greater.
  Attempt embedded Python inventory; failure prints inventory unavailable and continues.
  Inventory counts client extensions excluding selected minified names, directory groups top 10,
    files-of-interest sorted first 30, and first recognized lockfile; package.json without lock emits warning.
  Then execute secret/build/env/HTML/framework/code/URL/source/prototype/message/origin/isolation/storage/JWT/
    logging/authz/validation/identity/transport/redirect/dependency/SRI/public-key/sanitizer sections in source order.
  Per-call cap arguments remain exact in command evidence (10/12/15/40, rather than one global cap).
  End with status 0.
}
```

The two embedded Python inventories (client-side and code-exploration) have their
own structural SudoLang renderings with **original shell-file line coordinates**;
see `embedded_python.tsv`. They are not omitted as string literals.

```sudo
// Source: vvaharness/skills/code-exploration/probe.sh:20-223
fn code_exploration_probe() {
  Disable pathname expansion; ROOT defaults "."; failed cd prints aborted message and exits 0.
  Build EXCL flags in a loop over exact PRUNE names; retain separate template/source/config include flags.
  sec prints section heading; emit prints "(none)" only when its string argument is empty.
  if (python3 executable exists) {
    Run embedded inventory walk with sorted subdirectories/files and exact pruning.
    Count full retained inventory; report directory groups first 40 and pruned sample first 12;
      class samples first 15, dotfiles first 20, empty files first 10.
  } else { grep text-file fallback, normalize paths, sort and cap 60 }
  Execute source-ordered escape/render/inheritance/transport/deploy/CI/control/debug/credential/registration/SQL sections.
  Most pattern outputs are capped at 20; transport-config file list is capped at 12,
    then each selected file is examined for TLS/listen/line counts.
  Control-presence loop reports matching file count for each literal header/control pattern.
  Preserve the printed exhaustive/absence/locates-does-not-conclude messages as source wording;
    do not infer exhaustive code analysis from these capped regex searches.
  End with status 0.
}

// Source: vvaharness/skills/templates/probe.sh:20-269
fn templates_probe() {
  ROOT defaults "."; disable pathname expansion; preserve SKIP/TPL/SRC flags.
  norm collapses horizontal whitespace and clips to 170 columns.
  dedup sorts uniquely by file then numeric line using source sort flags.
  emit(cap) reads at most 3000 input lines; empty prints marker and returns 0;
    otherwise count retained input, print first cap and truncation note when applicable.
  Cache at most 5000 nonempty template-file names; tpl_files prints them when nonempty.
  tgrep and sgrep use template/host include flags respectively and tolerate failed/no-match grep.
  Run inventory/layout/escape/config/output/SSTI/URL/event sections in literal source order.
  Script-context AWK tracks script-tag nesting per file; prints interpolated script lines,
    classifies RAW versus ENCODED? by exact source pattern, clips snippet to 150.
  Then run CSS/unquoted-attribute and Go template sections.
  Form AWK accumulates each form span, including multiple forms on one line;
    flush at closing form, next file, or end. Classify method, token vocabulary, action text.
  Sort form records and retain first 2000; display count groups capped 10 and no-token forms capped 60.
  Run helper/CSRF/error/config/debug/sanitizer/render/CSP sections in order, using each source emit cap.
  Preserve literal claims in section labels as printed/model guidance; regex output alone is not a confirmed finding.
  End with status 0.
}

// Source: vvaharness/validation/claude_config/hooks/logging/capture_transcript.sh:19-35
fn capture_transcript_hook(environment,stdin) {
  Disable exit-on-error.
  if (VALIDATION_DEBUG_TRANSCRIPT is empty/unset) { exit with status 0 before reading stdin }
  Read stdin; use jq transcript_path default empty, suppress jq stderr; replace leading tilde with HOME via sed.
  Read VALIDATION_LOG_DIR, default empty.
  If transcript path is empty, not an existing file, or log dir empty, exit 0.
  Destination is log_dir/subagents/transcript.jsonl.
  Best-effort mkdir parent and copy raw transcript, suppressing stderr; tolerate copy failure.
  Exit 0. Default opt-out is executable; debug opt-in copies unredacted source transcript.
}
```

Exact regex, AWK state transitions, command flag ordering and shell short-circuit
operators remain in each mirrored source-command appendix because normalizing
them would risk changing the script. No new SudoLang shell or regex grammar is proposed.
