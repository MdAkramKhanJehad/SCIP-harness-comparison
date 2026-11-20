# P8-validation unresolved

No `// unresolved:` markers in `vvah/vvaharness/validation/**`. All source files in the area were readable.

Grammar notes (no grammar was invented): pass 2 first used `??` (absent-key fallback) and `extends` in case_api.sudo, config/settings/config.sudo and cli/__init__.sudo. In final cleanup these were rewritten in words ("x, or, when absent, y") and as `// source: subclass of ValueError` comments, so no non-SudoLang operator remains.
