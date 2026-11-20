# inputs/known_cves.example.json

Example known-CVE input passed to the scan's model stages (Stage 1 context, Stage 2, Stage 3 related CVEs, Stage 8 prompts).

Source: `inputs/known_cves.example.json` (lines 1-12)
Executor: code (data)
Called from: `vvaharness/orchestrator/scan.sudo` (load_cves(knob("inject.cve_file")))

// src: inputs/known_cves.example.json:3-11
Options {
  cves: [ { id: "CVE-2024-EXAMPLE", summary: "Heap overflow in parse_header() via crafted Content-Length", affected_files: ["src/http/parser.c"], cvss: 8.1, patched: false } ]
}
