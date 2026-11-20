# inputs/cmdb.example.csv

Example configuration-management database export: application profiles (exposure and data sensitivity) looked up by application id and used as scan context.

Source: `inputs/cmdb.example.csv` (lines 1-19)
Executor: code (data)
Called from: `vvaharness/orchestrator/cmdb.py` (see orchestrator/cmdb.sudo)

// src: inputs/cmdb.example.csv:15-19
Options {
  columns: [id, name, externally_facing, pci, pan, pii, parent_id]
  rows: [
    ["0000001", "example-public-payments-api", "Yes", "No", "Yes", "Yes", ""],
    ["0000002", "example-backend-batch-service", "No", "yes", "No", "No", ""],
    ["0000003", "example-marketing-site", "Yes", "yes", "No", "No", ""],
    ["0000004", "example-card-tokenization-component", "", "", "", "", "0000001"]   // blank flags with a parent id
  ]
}
// the mixed "Yes"/"yes" spelling and the blank child row are in the example as shipped
