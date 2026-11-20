# vvaharness/evidence/__init__.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/evidence/__init__.py.evidence.json`. SHA-256: `3318f12cd170717a696ac581225bd69bdcfdacc82cccd2d3171ae1078b426805`.

```sudo
// Source: vvaharness/evidence/__init__.py:15-31
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.api_artefacts import _API_SURFACE_GLOBS, gather_api_artefacts; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.configs import _CONFIG_EXTS, _CONFIG_REP_RAW_CEILING, _config_rep_contents, _select_config_reps, gather_config_reps; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.docs import _DOC_CANDIDATES, _DOC_EXTRA_MAX, _DOC_NAME_RX, gather_docs; preserve alias and import-time effects.
// Source: vvaharness/evidence/__init__.py:32-87
In source order: Resolve source import from vvaharness.evidence.gather import ThreatEvidence, _cap_int, gather; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.manifests import _MANIFEST_CANDIDATES, _MANIFEST_RAW_CEILING, _apply_manifest_total_cap, _find_manifests, _structural_truncate, gather_manifests; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.read import _cap_text, _contained, _read_capped; preserve alias and import-time effects. Then Resolve source import from vvaharness.evidence.render import render_api_artefacts_block, render_components_block, render_config_reps_block, render_docs_block, render_entry_points_block, render_inventory_block, render_language_block, render_manifests_block, render_modules_block; preserve alias and import-time effects. Then Evaluate once ['_API_SURFACE_GLOBS', '_CONFIG_EXTS', '_CONFIG_REP_RAW_CEILING', '_DOC_CANDIDATES', '_DOC_EXTRA_MAX', '_DOC_NAME_RX', '_MANIFEST_CANDIDATES', '_MANIFEST_RAW_CEILING', 'ThreatEvidence', '_apply_manifest_total_cap', '_cap_int', '_cap_text', '_config_rep_contents', '_contained', '_find_manifests', '_read_capped', '_select_config_reps', '_structural_truncate', 'gather', 'gather_api_artefacts', 'gather_config_reps', 'gather_docs', 'gather_manifests', 'render_api_artefacts_block', 'render_components_block', 'render_config_reps_block', 'render_docs_block', 'render_entry_points_block', 'render_inventory_block', 'render_language_block', 'render_manifests_block', 'render_modules_block']; assign in source target order to __all__.
```

## Local import links

- `from vvaharness.evidence.api_artefacts import _API_SURFACE_GLOBS, gather_api_artefacts` at source line 18: `source_detail/vvaharness/evidence/api_artefacts.py.sudo.md`.
- `from vvaharness.evidence.configs import _CONFIG_EXTS, _CONFIG_REP_RAW_CEILING, _config_rep_contents, _select_config_reps, gather_config_reps` at source line 19: `source_detail/vvaharness/evidence/configs.py.sudo.md`.
- `from vvaharness.evidence.docs import _DOC_CANDIDATES, _DOC_EXTRA_MAX, _DOC_NAME_RX, gather_docs` at source line 26: `source_detail/vvaharness/evidence/docs.py.sudo.md`.
- `from vvaharness.evidence.gather import ThreatEvidence, _cap_int, gather` at source line 32: `source_detail/vvaharness/evidence/gather.py.sudo.md`.
- `from vvaharness.evidence.manifests import _MANIFEST_CANDIDATES, _MANIFEST_RAW_CEILING, _apply_manifest_total_cap, _find_manifests, _structural_truncate, gather_manifests` at source line 33: `source_detail/vvaharness/evidence/manifests.py.sudo.md`.
- `from vvaharness.evidence.read import _cap_text, _contained, _read_capped` at source line 41: `source_detail/vvaharness/evidence/read.py.sudo.md`.
- `from vvaharness.evidence.render import render_api_artefacts_block, render_components_block, render_config_reps_block, render_docs_block, render_entry_points_block, render_inventory_block, render_language_block, render_manifests_block, render_modules_block` at source line 42: `source_detail/vvaharness/evidence/render.py.sudo.md`.
