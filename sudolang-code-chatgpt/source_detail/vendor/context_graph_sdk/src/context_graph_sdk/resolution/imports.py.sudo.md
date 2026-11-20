# vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py.evidence.json`. SHA-256: `9d5feaa4714824f3e06f36a7ef2a0390f16eb593945e1e36c6d9e0110662e899`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:15-27
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.models import LocalRelationshipType; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult, file_local_id, folder_local_id; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:29-36
In source order: Evaluate once ('.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs'); assign in source target order to _TS_EXTENSIONS. Then Evaluate once ('index.ts', 'index.tsx', 'index.js', 'index.jsx'); assign in source target order to _TS_INDEX_FILES. Then Evaluate once ('.py', '.pyi'); assign in source target order to _PY_EXTENSIONS. Then Evaluate once ('.java', '.kt', '.scala', '.groovy'); assign in source target order to _JVM_EXTENSIONS. Then Evaluate once ('.go', '.ts', '.tsx', '.js', '.jsx', '.py', '.java', '.rs', '.rb', '.php', '.cs', '.kt', '.swift', '.sol'); assign in source target order to _GENERIC_EXTENSIONS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:39-40
// Source signature: is_relative_import(import_path: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_relative_import(import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:40-40
  End this invocation with import_path.startswith(('./', '../')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:43-58
In source order: Evaluate once frozenset({'go', 'typescript', 'tsx', 'javascript', 'python', 'java', 'kotlin', 'rust', 'csharp', 'php', 'ruby', 'swift'}); assign in source target order to _DEDICATED_RESOLVER_LANGUAGES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:61-83
// Source signature: resolve_imports(context: ResolutionContext, result: ResolutionResult) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn resolve_imports(context, result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:62-62
  In source order: For resolved_pairs, assign []; source annotation list[tuple[str, str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:63-82
  for each (from_path, file_result) in context.extraction.files {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:64-64
    In source order: Evaluate once context.file_language.get(from_path, ''); assign in source target order to language.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:65-82
    for each imported in file_result.imports {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:66-66
      In source order: Evaluate once _resolve_one(context, from_path, imported.source, language); assign in source target order to target.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:67-71
      if (the source predicate target is None and language in _DEDICATED_RESOLVER_LANGUAGES is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:71-71
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:72-76
      if (the source predicate target is None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:73-76
        if (the source predicate is_relative_import(imported.source) or imported.source.startswith('.') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:74-74
          In source order: Evaluate once _resolve_generic_relative(context, from_path, imported.source); assign in source target order to target.
        }
        else {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:76-76
          In source order: Evaluate once _resolve_generic_absolute(context, imported.source); assign in source target order to target.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:77-78
      if (the source predicate target is None or target == from_path is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:78-78
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:79-82
      if (the source predicate result.add_edge(file_local_id(from_path), LocalRelationshipType.IMPORTS, file_local_id(target)) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:82-82
        In source order: Evaluate resolved_pairs.append((from_path, target)); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:83-83
  In source order: Evaluate _add_folder_edges(context, result, resolved_pairs); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:86-107
// Source signature: _resolve_one(context: ResolutionContext, from_path: str, import_path: str, language: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_one(context, from_path, import_path, language) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:89-90
  if (the source predicate language == 'go' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:90-90
    End this invocation with _resolve_go(context, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:91-92
  if (the source predicate language in ('typescript', 'tsx', 'javascript') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:92-92
    End this invocation with _resolve_ts_js(context, from_path, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:93-94
  if (the source predicate language == 'python' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:94-94
    End this invocation with _resolve_python(context, from_path, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:95-96
  if (the source predicate language in ('java', 'kotlin') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:96-96
    End this invocation with _resolve_jvm(context, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:97-98
  if (the source predicate language == 'rust' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:98-98
    End this invocation with _resolve_rust(context, from_path, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:99-100
  if (the source predicate language == 'csharp' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:100-100
    End this invocation with _resolve_csharp(context, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:101-102
  if (the source predicate language == 'php' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:102-102
    End this invocation with _resolve_php(context, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:103-104
  if (the source predicate language == 'ruby' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:104-104
    End this invocation with _resolve_ruby(context, from_path, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:105-106
  if (the source predicate language == 'swift' is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:106-106
    End this invocation with _resolve_swift(context, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:107-107
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:110-122
// Source signature: _go_package_file(context: ResolutionContext, directory: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _go_package_file(context, directory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:111-113
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call. Then Evaluate once directory.rstrip('/'); assign in source target order to directory. Then For fallback, assign None; source annotation str | None.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:114-121
  for each name in context.files_in_dir(directory) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:115-116
    if (the source predicate not name.endswith('.go') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:116-116
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:117-117
    In source order: Evaluate once posixpath.join(directory, name) if directory else name; assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:118-119
    if (the source predicate not name.endswith('_test.go') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:119-119
      End this invocation with candidate.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:120-121
    if (the source predicate fallback is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:121-121
      In source order: Evaluate once candidate; assign in source target order to fallback.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:122-122
  End this invocation with fallback.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:125-137
// Source signature: _resolve_go(context: ResolutionContext, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_go(context, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:126-126
  In source order: Evaluate once context.settings.go_module_path; assign in source target order to module.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:127-130
  if (the source predicate module and import_path.startswith(module) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:128-128
    In source order: Evaluate once import_path.removeprefix(module).removeprefix('/'); assign in source target order to relative.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:129-130
    if (the source predicate relative is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:130-130
      End this invocation with _go_package_file(context, relative).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:131-131
  In source order: Evaluate once import_path.split('/'); assign in source target order to parts.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:132-136
  if (the source predicate len(parts) >= 2 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:133-136
    for each index in range(len(parts)) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:134-134
      In source order: Evaluate once _go_package_file(context, '/'.join(parts[index:])); assign in source target order to found.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:135-136
      if (the source predicate found is not None is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:136-136
        End this invocation with found.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:137-137
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:140-148
// Source signature: _lookup_ts_file(context: ResolutionContext, base_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _lookup_ts_file(context, base_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:141-141
  In source order: Evaluate once context.lookup_with_extensions(base_path, _TS_EXTENSIONS); assign in source target order to found.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:142-143
  if (the source predicate found is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:143-143
    End this invocation with found.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:144-147
  for each index_file in _TS_INDEX_FILES {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:145-145
    In source order: Evaluate once posixpath.join(base_path, index_file); assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:146-147
    if (the source predicate context.has_file(candidate) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:147-147
      End this invocation with candidate.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:148-148
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:151-176
// Source signature: _resolve_ts_js(context: ResolutionContext, from_path: str, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_ts_js(context, from_path, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:152-154
  if (the source predicate import_path.startswith('.') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:153-153
    In source order: Evaluate once posixpath.normpath(posixpath.join(posixpath.dirname(from_path), import_path)); assign in source target order to resolved.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:154-154
    End this invocation with _lookup_ts_file(context, resolved).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:155-169
  for each (pattern, targets) in context.settings.ts_config_paths {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:156-169
    if (the source predicate pattern.endswith('*') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:157-157
      In source order: Evaluate once pattern[:-1]; assign in source target order to prefix.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:158-164
      if (the source predicate import_path.startswith(prefix) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:159-159
        In source order: Evaluate once import_path.removeprefix(prefix); assign in source target order to rest.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:160-164
        for each target in targets {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:161-162
          In source order: Evaluate once posixpath.join(target.removesuffix('*'), rest); assign in source target order to candidate. Then Evaluate once _lookup_ts_file(context, posixpath.normpath(candidate)); assign in source target order to found.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:163-164
          if (the source predicate found is not None is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:164-164
            End this invocation with found.
          }
        }
      }
    }
    else {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:165-169
      if (the source predicate import_path == pattern is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:166-169
        for each target in targets {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:167-167
          In source order: Evaluate once _lookup_ts_file(context, target); assign in source target order to found.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:168-169
          if (the source predicate found is not None is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:169-169
            End this invocation with found.
          }
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:170-175
  if (the source predicate context.settings.ts_config_base_url is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:171-173
    In source order: Evaluate once _lookup_ts_file(context, posixpath.join(context.settings.ts_config_base_url, import_path)); assign in source target order to found.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:174-175
    if (the source predicate found is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:175-175
      End this invocation with found.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:176-176
  End this invocation with _lookup_ts_file(context, import_path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:179-202
// Source signature: _resolve_python(context: ResolutionContext, from_path: str, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_python(context, from_path, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:180-181
  if (the source predicate import_path.startswith('.') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:181-181
    End this invocation with _resolve_python_relative(context, from_path, import_path).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:182-183
  In source order: Evaluate once import_path.replace('.', '/'); assign in source target order to module_path. Then Evaluate once context.lookup_with_extensions(module_path, _PY_EXTENSIONS); assign in source target order to found.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:184-185
  if (the source predicate found is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:185-185
    End this invocation with found.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:186-186
  In source order: Evaluate once posixpath.join(module_path, '__init__.py'); assign in source target order to package_init.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:187-188
  if (the source predicate context.has_file(package_init) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:188-188
    End this invocation with package_init.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:189-189
  In source order: Evaluate once posixpath.dirname(from_path); assign in source target order to directory.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:190-201
  while (the source predicate directory not in ('', '.') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:191-192
    In source order: Evaluate once posixpath.join(directory, module_path); assign in source target order to candidate. Then Evaluate once context.lookup_with_extensions(candidate, _PY_EXTENSIONS); assign in source target order to found.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:193-194
    if (the source predicate found is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:194-194
      End this invocation with found.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:195-195
    In source order: Evaluate once posixpath.join(candidate, '__init__.py'); assign in source target order to init.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:196-197
    if (the source predicate context.has_file(init) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:197-197
      End this invocation with init.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:198-198
    In source order: Evaluate once posixpath.dirname(directory); assign in source target order to parent.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:199-200
    if (the source predicate parent == directory is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:200-200
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:201-201
    In source order: Evaluate once parent; assign in source target order to directory.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:202-202
  End this invocation with context.lookup_suffix('/' + module_path + '.py').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:205-222
// Source signature: _resolve_python_relative(context: ResolutionContext, from_path: str, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_python_relative(context, from_path, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:208-210
  In source order: Evaluate once len(import_path) - len(import_path.lstrip('.')); assign in source target order to dots. Then Evaluate once import_path[dots:]; assign in source target order to rest. Then Evaluate once posixpath.dirname(from_path); assign in source target order to directory.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:211-212
  for each _ in range(dots - 1) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:212-212
    In source order: Evaluate once posixpath.dirname(directory); assign in source target order to directory.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:213-220
  if (the source predicate rest is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:214-215
    In source order: Evaluate once posixpath.join(directory, rest.replace('.', '/')); assign in source target order to candidate. Then Evaluate once context.lookup_with_extensions(candidate, _PY_EXTENSIONS); assign in source target order to found.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:216-217
    if (the source predicate found is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:217-217
      End this invocation with found.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:218-218
    In source order: Evaluate once posixpath.join(candidate, '__init__.py'); assign in source target order to init.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:219-220
    if (the source predicate context.has_file(init) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:220-220
      End this invocation with init.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:221-221
  In source order: Evaluate once posixpath.join(directory, '__init__.py'); assign in source target order to package_init.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:222-222
  End this invocation with package_init if context.has_file(package_init) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:225-225
In source order: Evaluate once ('src/main/java/', 'src/main/kotlin/', 'src/'); assign in source target order to _JVM_SOURCE_DIRS.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:228-234
// Source signature: _jvm_file_in_dir(context: ResolutionContext, directory: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _jvm_file_in_dir(context, directory) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:229-233
  for each prefix in ('', 'src/main/java/', 'src/main/kotlin/') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:230-230
    In source order: Evaluate once prefix + directory; assign in source target order to full.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:231-233
    for each name in context.files_in_dir(full) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:232-233
      if (the source predicate posixpath.splitext(name)[1] in ('.java', '.kt', '.scala') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:233-233
        End this invocation with posixpath.join(full, name).
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:234-234
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:237-257
// Source signature: _resolve_jvm(context: ResolutionContext, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_jvm(context, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:238-238
  In source order: Evaluate once import_path.replace('.', '/'); assign in source target order to module_path.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:239-240
  if (the source predicate module_path.endswith('/*') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:240-240
    End this invocation with _jvm_file_in_dir(context, module_path[:-2]).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:241-241
  In source order: Evaluate once context.lookup_with_extensions(module_path, _JVM_EXTENSIONS); assign in source target order to found.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:242-243
  if (the source predicate found is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:243-243
    End this invocation with found.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:244-247
  for each source_dir in _JVM_SOURCE_DIRS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:245-245
    In source order: Evaluate once context.lookup_with_extensions(source_dir + module_path, _JVM_EXTENSIONS); assign in source target order to found.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:246-247
    if (the source predicate found is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:247-247
      End this invocation with found.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:248-248
  In source order: Evaluate once import_path.split('.'); assign in source target order to parts.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:249-256
  if (the source predicate len(parts) >= 2 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:250-251
    In source order: Evaluate once parts[-1]; assign in source target order to class_name. Then Evaluate once '/'.join(parts[:-1]); assign in source target order to package_dir.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:252-256
    for each source_dir in ('', *_JVM_SOURCE_DIRS) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:253-253
      In source order: Evaluate once source_dir + package_dir; assign in source target order to directory.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:254-256
      for each name in context.files_in_dir(directory) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:255-256
        if (the source predicate posixpath.splitext(name)[0] == class_name is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:256-256
          End this invocation with posixpath.join(directory, name).
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:257-257
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:260-269
// Source signature: _lookup_rust_module(context: ResolutionContext, base_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _lookup_rust_module(context, base_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:261-268
  for each candidate in (base_path + '.rs', posixpath.join(base_path, 'mod.rs'), posixpath.join(base_path, 'lib.rs'), base_path) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:267-268
    if (the source predicate context.has_file(candidate) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:268-268
      End this invocation with candidate.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:269-269
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:272-293
// Source signature: _resolve_rust(context: ResolutionContext, from_path: str, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_rust(context, from_path, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:273-273
  In source order: Evaluate once import_path.find('{'); assign in source target order to brace.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:274-275
  if (the source predicate brace >= 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:275-275
    In source order: Evaluate once import_path[:brace].rstrip(':'); assign in source target order to import_path.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:276-277
  In source order: Evaluate once import_path.removesuffix('::*'); assign in source target order to import_path. Then Evaluate once import_path.replace('::', '/'); assign in source target order to module_path.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:278-279
  if (the source predicate module_path.startswith('crate/') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:279-279
    End this invocation with _lookup_rust_module(context, 'src/' + module_path.removeprefix('crate/')).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:280-284
  if (the source predicate module_path.startswith('super/') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:281-281
    In source order: Evaluate once posixpath.dirname(posixpath.dirname(from_path)); assign in source target order to parent.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:282-284
    End this invocation with _lookup_rust_module(context, posixpath.join(parent, module_path.removeprefix('super/'))).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:285-289
  if (the source predicate module_path.startswith('self/') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:286-286
    In source order: Evaluate once posixpath.dirname(from_path); assign in source target order to directory.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:287-289
    End this invocation with _lookup_rust_module(context, posixpath.join(directory, module_path.removeprefix('self/'))).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:290-290
  In source order: Evaluate once _lookup_rust_module(context, 'src/' + module_path); assign in source target order to found.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:291-292
  if (the source predicate found is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:292-292
    End this invocation with found.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:293-293
  End this invocation with _lookup_rust_module(context, module_path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:296-308
// Source signature: _resolve_csharp(context: ResolutionContext, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_csharp(context, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:297-297
  In source order: Evaluate once import_path.replace('.', '/'); assign in source target order to namespace_path.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:298-299
  if (the source predicate context.has_file(namespace_path + '.cs') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:299-299
    End this invocation with namespace_path + '.cs'.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:300-300
  In source order: Evaluate once context.settings.csharp_root_namespace; assign in source target order to root.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:301-304
  if (the source predicate root and import_path.startswith(root) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:302-302
    In source order: Evaluate once import_path.removeprefix(root).removeprefix('.').replace('.', '/'); assign in source target order to relative.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:303-304
    if (the source predicate relative and context.has_file(relative + '.cs') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:304-304
      End this invocation with relative + '.cs'.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:305-307
  for each name in context.files_in_dir(namespace_path) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:306-307
    if (the source predicate name.endswith('.cs') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:307-307
      End this invocation with posixpath.join(namespace_path, name).
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:308-308
  End this invocation with context.lookup_suffix('/' + namespace_path + '.cs').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:311-327
// Source signature: _resolve_php(context: ResolutionContext, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_php(context, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:312-312
  In source order: Evaluate once import_path.replace('\\', '/'); assign in source target order to namespace_path.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:313-320
  for each (prefix, directories) in context.settings.composer_psr4 {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:314-314
    In source order: Evaluate once prefix.replace('\\', '/'); assign in source target order to normalized.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:315-320
    if (the source predicate namespace_path.startswith(normalized) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:316-316
      In source order: Evaluate once namespace_path.removeprefix(normalized); assign in source target order to relative.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:317-320
      for each directory in directories {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:318-318
        In source order: Evaluate once posixpath.join(directory.rstrip('/'), relative) + '.php'; assign in source target order to candidate.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:319-320
        if (the source predicate context.has_file(candidate) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:320-320
          End this invocation with candidate.
        }
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:321-322
  if (the source predicate context.has_file(namespace_path + '.php') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:322-322
    End this invocation with namespace_path + '.php'.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:323-323
  In source order: Evaluate once context.lookup_suffix('/' + namespace_path + '.php'); assign in source target order to found.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:324-325
  if (the source predicate found is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:325-325
    End this invocation with found.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:326-326
  In source order: Evaluate once namespace_path.rsplit('/', 1)[-1]; assign in source target order to class_name.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:327-327
  End this invocation with context.lookup_suffix('/' + class_name + '.php').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:330-342
// Source signature: _resolve_ruby(context: ResolutionContext, from_path: str, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_ruby(context, from_path, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:331-335
  if (the source predicate import_path.startswith('.') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:332-332
    In source order: Evaluate once posixpath.normpath(posixpath.join(posixpath.dirname(from_path), import_path)); assign in source target order to resolved.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:333-334
    if (the source predicate context.has_file(resolved + '.rb') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:334-334
      End this invocation with resolved + '.rb'.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:335-335
    End this invocation with resolved if context.has_file(resolved) else None.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:336-337
  if (the source predicate context.has_file(import_path + '.rb') is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:337-337
    End this invocation with import_path + '.rb'.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:338-341
  for each prefix in ('lib/', 'app/', 'src/') {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:339-339
    In source order: Evaluate once prefix + import_path + '.rb'; assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:340-341
    if (the source predicate context.has_file(candidate) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:341-341
      End this invocation with candidate.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:342-342
  End this invocation with context.lookup_suffix('/' + import_path + '.rb').
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:345-355
// Source signature: _resolve_swift(context: ResolutionContext, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_swift(context, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:346-349
  In source order: Evaluate once [directory for name, directory in context.settings.swift_targets if name == import_path]; assign in source target order to directories. Then Evaluate directories.append('Sources/' + import_path); retain side effects and discard the expression result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:350-353
  for each directory in directories {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:351-353
    for each name in context.files_in_dir(directory) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:352-353
      if (the source predicate name.endswith('.swift') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:353-353
        End this invocation with posixpath.join(directory, name).
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:354-354
  In source order: Evaluate once import_path + '.swift'; assign in source target order to candidate.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:355-355
  End this invocation with candidate if context.has_file(candidate) else None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:358-371
// Source signature: _resolve_generic_relative(context: ResolutionContext, from_path: str, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_generic_relative(context, from_path, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:361-361
  In source order: Evaluate once posixpath.normpath(posixpath.join(posixpath.dirname(from_path), import_path)); assign in source target order to resolved.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:362-363
  if (the source predicate context.has_file(resolved) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:363-363
    End this invocation with resolved.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:364-364
  In source order: Evaluate once context.lookup_with_extensions(resolved, _GENERIC_EXTENSIONS); assign in source target order to found.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:365-366
  if (the source predicate found is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:366-366
    End this invocation with found.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:367-370
  for each index_file in _TS_INDEX_FILES {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:368-368
    In source order: Evaluate once posixpath.join(resolved, index_file); assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:369-370
    if (the source predicate context.has_file(candidate) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:370-370
      End this invocation with candidate.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:371-371
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:374-384
// Source signature: _resolve_generic_absolute(context: ResolutionContext, import_path: str) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_generic_absolute(context, import_path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:375-379
  In source order: Retain source documentation literal source_literal_375_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:380-383
  for each extension in _GENERIC_EXTENSIONS {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:381-381
    In source order: Evaluate once context.lookup_suffix(import_path + extension); assign in source target order to found.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:382-383
    if (the source predicate found is not None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:383-383
      End this invocation with found.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:384-384
  End this invocation with context.lookup_suffix(import_path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:387-398
// Source signature: _add_folder_edges(context: ResolutionContext, result: ResolutionResult, resolved_pairs: list[tuple[str, str]]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _add_folder_edges(context, result, resolved_pairs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:390-398
  for each (from_path, to_path) in resolved_pairs {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:391-392
    In source order: Evaluate once posixpath.dirname(from_path); assign in source target order to from_dir. Then Evaluate once posixpath.dirname(to_path); assign in source target order to to_dir.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:393-394
    if (the source predicate from_dir == to_dir is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:394-394
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:395-398
    if (the source predicate from_dir in context.folders and to_dir in context.folders is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/resolution/imports.py:396-398
      In source order: Evaluate result.add_edge(folder_local_id(from_dir), LocalRelationshipType.IMPORTS, folder_local_id(to_dir)); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.models import LocalRelationshipType` at source line 21: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/models.py.sudo.md`.
- `from context_graph_sdk.resolution.context import ResolutionContext, ResolutionResult, file_local_id, folder_local_id` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/resolution/context.py.sudo.md`.
