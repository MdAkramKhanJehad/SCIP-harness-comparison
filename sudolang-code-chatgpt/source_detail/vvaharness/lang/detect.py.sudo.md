# vvaharness/lang/detect.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/lang/detect.py.evidence.json`. SHA-256: `fa24b86cc4ad2d30ff6a42342668aebfa1fabff49b0dc38841f39e4dcd7b52e2`.

```sudo
// Source: vvaharness/lang/detect.py:15-105
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import re; preserve alias and import-time effects. Then Resolve source import from pathlib import Path, PurePosixPath; preserve alias and import-time effects. Then For EXT_TO_LANG, assign {'.c': 'c-cpp', '.cc': 'c-cpp', '.cpp': 'c-cpp', '.cxx': 'c-cpp', '.h': 'c-cpp', '.hpp': 'c-cpp', '.rs': 'rust', '.go': 'go', '.py': 'python', '.java': 'java', '.js': 'javascript', '.jsx': 'javascript', '.mjs': 'javascript', '.cjs': 'javascript', '.ts': 'typescript', '.tsx': 'typescript', '.mts': 'typescript', '.cts': 'typescript', '.php': 'php', '.rb': 'ruby', '.m': 'objective-c', '.mm': 'objective-c', '.kt': 'kotlin', '.kts': 'kotlin', '.cs': 'csharp', '.pl': 'perl', '.pm': 'perl', '.swift': 'swift', '.scala': 'scala', '.sc': 'scala', '.cbl': 'cobol', '.cob': 'cobol', '.cpy': 'cobol', '.jcl': 'jcl', '.dart': 'dart', '.ex': 'elixir', '.exs': 'elixir', '.erl': 'erlang', '.hrl': 'erlang', '.groovy': 'groovy', '.gvy': 'groovy', '.gy': 'groovy', '.gsh': 'groovy', '.lua': 'lua', '.r': 'r', '.ps1': 'powershell', '.psm1': 'powershell', '.psd1': 'powershell', '.sh': 'shell', '.bash': 'shell', '.zsh': 'shell', '.cmd': 'batch', '.bat': 'batch', '.sql': 'sql', '.ddl': 'sql', '.dml': 'sql', '.tsql': 'sql', '.plsql': 'sql', '.pks': 'sql', '.pkb': 'sql', '.pls': 'sql', '.plb': 'sql', '.prc': 'sql', '.fnc': 'sql', '.trg': 'sql', '.vw': 'sql', '.vb': 'vbnet', '.bas': 'vbnet', '.cls': 'vbnet', '.frm': 'vbnet', '.vbs': 'vbnet', '.abap': 'abap', '.aba': 'abap', '.clj': 'clojure', '.cljs': 'clojure', '.cljc': 'clojure', '.edn': 'clojure', '.hs': 'haskell', '.lhs': 'haskell', '.ml': 'ocaml', '.mli': 'ocaml', '.fs': 'fsharp', '.fsi': 'fsharp', '.fsx': 'fsharp', '.jl': 'julia', '.sol': 'solidity', '.asm': 'assembly', '.s': 'assembly', '.zig': 'zig', '.nim': 'nim', '.nims': 'nim', '.cr': 'crystal', '.tf': 'terraform', '.tfvars': 'terraform', '.hcl': 'terraform', '.bicep': 'bicep', '.html': 'web-template', '.htm': 'web-template', '.jsp': 'web-template', '.jspx': 'web-template', '.jspf': 'web-template', '.tag': 'web-template', '.tagx': 'web-template', '.aspx': 'web-template', '.ascx': 'web-template', '.master': 'web-template', '.cshtml': 'web-template', '.vbhtml': 'web-template', '.phtml': 'web-template', '.erb': 'web-template', '.rhtml': 'web-template', '.ejs': 'web-template', '.hbs': 'web-template', '.handlebars': 'web-template', '.mustache': 'web-template', '.twig': 'web-template', '.pug': 'web-template', '.jade': 'web-template', '.ftl': 'web-template', '.ftlh': 'web-template', '.vm': 'web-template', '.vtl': 'web-template', '.mako': 'web-template', '.j2': 'web-template', '.jinja': 'web-template', '.jinja2': 'web-template', '.vue': 'web-template', '.svelte': 'web-template', '.liquid': 'web-template', '.njk': 'web-template', '.slim': 'web-template', '.haml': 'web-template', '.tpl': 'web-template', '.xhtml': 'web-template'}; source annotation dict[str, str].
// Source: vvaharness/lang/detect.py:108-108
In source order: For TEMPLATE_COMPOUND_SUFFIXES, assign ('.blade.php',); source annotation tuple[str, ...].
// Source: vvaharness/lang/detect.py:111-118
// Source signature: is_web_template(path: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_web_template(path) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/lang/detect.py:112-114
  In source order: Retain source documentation literal source_literal_112_4; it is not a model call. Then Evaluate once path.lower(); assign in source target order to low.
  // Source: vvaharness/lang/detect.py:115-116
  if (the source predicate low.endswith(TEMPLATE_COMPOUND_SUFFIXES) is truthy) {
    // Source: vvaharness/lang/detect.py:116-116
    End this invocation with True.
  }
  // Source: vvaharness/lang/detect.py:117-117
  In source order: Evaluate once low.rpartition('.'); assign in source target order to (_, dot, ext).
  // Source: vvaharness/lang/detect.py:118-118
  End this invocation with bool(dot) and EXT_TO_LANG.get(source_template_118_41) == 'web-template'.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/lang/detect.py:120-174
In source order: For LANG_DISPLAY, assign {'c-cpp': 'C/C++', 'rust': 'Rust', 'go': 'Go', 'python': 'Python', 'java': 'Java', 'javascript': 'JavaScript', 'php': 'PHP', 'ruby': 'Ruby', 'objective-c': 'Objective-C', 'kotlin': 'Kotlin', 'csharp': 'C#/.NET', 'perl': 'Perl', 'swift': 'Swift', 'scala': 'Scala', 'cobol': 'COBOL', 'jcl': 'JCL (z/OS)', 'dart': 'Dart/Flutter', 'elixir': 'Elixir', 'erlang': 'Erlang', 'groovy': 'Groovy', 'lua': 'Lua', 'r': 'R', 'powershell': 'PowerShell', 'shell': 'Shell (bash/sh)', 'batch': 'Windows Batch (.cmd/.bat)', 'web-template': 'Web Templates', 'ansible': 'Ansible', 'terraform': 'Terraform / HCL', 'bicep': 'Azure Bicep', 'dockerfile': 'Dockerfile', 'jenkins': 'Jenkinsfile', 'github-actions': 'GitHub Actions', 'kubernetes': 'Kubernetes / Helm', 'typescript': 'TypeScript', 'sql': 'SQL / PL-SQL / T-SQL', 'vbnet': 'Visual Basic / VB.NET', 'abap': 'ABAP (SAP)', 'clojure': 'Clojure', 'haskell': 'Haskell', 'ocaml': 'OCaml', 'fsharp': 'F#', 'julia': 'Julia', 'solidity': 'Solidity', 'assembly': 'Assembly', 'zig': 'Zig', 'nim': 'Nim', 'crystal': 'Crystal'}; source annotation dict[str, str]. Then Evaluate once re.compile('(?:^|/)(?:ansible|playbooks?|roles|inventories|group_vars|host_vars)(?:/|$)', re.IGNORECASE); assign in source target order to _ANSIBLE_PATH_RX. Then Evaluate once re.compile('^\\s*-?\\s*(hosts|tasks|handlers|become|gather_facts|ansible\\.[\\w.]+)\\s*:', re.MULTILINE); assign in source target order to _ANSIBLE_BODY_RX. Then Evaluate once re.compile(source_literal_166_4, re.IGNORECASE | re.MULTILINE); assign in source target order to _COBOL_BODY_RX. Then Evaluate once re.compile('^//\\S*\\s+(JOB|EXEC|DD|PROC)\\b|^//\\s*SYSIN\\b', re.MULTILINE); assign in source target order to _JCL_BODY_RX.
// Source: vvaharness/lang/detect.py:175-193
In source order: Evaluate once re.compile('(?:^|/)(?:mvs[_-]?code|jcl|cntl|proclib|cobol|copybooks?|jobs)(?:/|$)', re.IGNORECASE); assign in source target order to _MAINFRAME_PATH_RX. Then Evaluate once re.compile('(?:^|/)(?:Dockerfile|Containerfile)(?:\\.[\\w.-]+)?$', re.IGNORECASE); assign in source target order to _DOCKERFILE_NAME_RX. Then Evaluate once re.compile('(?:^|/)Jenkinsfile(?:\\.[\\w.-]+)?$', re.IGNORECASE); assign in source target order to _JENKINSFILE_NAME_RX. Then Evaluate once re.compile('(?:^|/)\\.github/workflows/[^/]+\\.ya?ml$'); assign in source target order to _GHACTIONS_PATH_RX. Then Evaluate once re.compile('(?:^|/)(?:k8s|kubernetes|helm|charts?|manifests?|deploy(?:ments?)?)/.+\\.(?:ya?ml|tpl)$', re.IGNORECASE); assign in source target order to _K8S_PATH_RX.
// Source: vvaharness/lang/detect.py:194-206
In source order: Evaluate once re.compile('^apiVersion:\\s+\\S+', re.MULTILINE); assign in source target order to _K8S_BODY_RX. Then Evaluate once re.compile(source_literal_196_4, re.IGNORECASE); assign in source target order to _IAC_PATH_RX.
// Source: vvaharness/lang/detect.py:209-211
// Source signature: is_iac_file(rel: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_iac_file(rel) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/lang/detect.py:210-210
  In source order: Retain source documentation literal source_literal_210_4; it is not a model call.
  // Source: vvaharness/lang/detect.py:211-211
  End this invocation with bool(_IAC_PATH_RX.search(rel)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/lang/detect.py:214-222
In source order: Evaluate once {'web.xml', 'struts.xml', 'struts-config.xml', 'applicationcontext.xml', 'spring-security.xml', 'beans.xml', 'faces-config.xml', 'shiro.ini', 'security.xml', 'ejb-jar.xml', 'jboss-web.xml', 'weblogic.xml', 'androidmanifest.xml', 'info.plist', 'application.properties', 'application.yml', 'application.yaml', 'appsettings.json', 'web.config', 'app.config'}; assign in source target order to SECURITY_CONFIG_NAMES. Then Evaluate once {'.xml', '.properties'}; assign in source target order to SECURITY_CONFIG_EXTS.
// Source: vvaharness/lang/detect.py:227-232
// Source signature: _read_head(repo_root: Path, rel: str, n: int=4096) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _read_head(repo_root, rel, n) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/lang/detect.py:228-232
  Perform the following protected operations {
    // Source: vvaharness/lang/detect.py:229-230
    Enter source context managers left-to-right: open(repo_root / rel, 'r', encoding='utf-8', errors='replace') bound to fh {
      // Source: vvaharness/lang/detect.py:230-230
      End this invocation with fh.read(n).
    }
    Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  }
  // Source: vvaharness/lang/detect.py:231-232
  On the first matching source exception OSError, in handler order {
    // Source: vvaharness/lang/detect.py:232-232
    End this invocation with ''.
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/lang/detect.py:235-276
// Source signature: _sniff_lang(rel: str, repo_root: Path | None) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sniff_lang(rel, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/lang/detect.py:236-236
  In source order: Retain source documentation literal source_literal_236_4; it is not a model call.
  // Source: vvaharness/lang/detect.py:238-239
  if (the source predicate _DOCKERFILE_NAME_RX.search(rel) is truthy) {
    // Source: vvaharness/lang/detect.py:239-239
    End this invocation with 'dockerfile'.
  }
  // Source: vvaharness/lang/detect.py:240-241
  if (the source predicate _JENKINSFILE_NAME_RX.search(rel) is truthy) {
    // Source: vvaharness/lang/detect.py:241-241
    End this invocation with 'jenkins'.
  }
  // Source: vvaharness/lang/detect.py:242-243
  if (the source predicate _GHACTIONS_PATH_RX.search(rel) is truthy) {
    // Source: vvaharness/lang/detect.py:243-243
    End this invocation with 'github-actions'.
  }
  // Source: vvaharness/lang/detect.py:245-245
  In source order: Evaluate once PurePosixPath(rel).suffix.lower(); assign in source target order to suffix.
  // Source: vvaharness/lang/detect.py:247-258
  if (the source predicate suffix in ('.yml', '.yaml') is truthy) {
    // Source: vvaharness/lang/detect.py:248-249
    if (the source predicate _ANSIBLE_PATH_RX.search(rel) is truthy) {
      // Source: vvaharness/lang/detect.py:249-249
      End this invocation with 'ansible'.
    }
    // Source: vvaharness/lang/detect.py:250-251
    if (the source predicate _K8S_PATH_RX.search(rel) is truthy) {
      // Source: vvaharness/lang/detect.py:251-251
      End this invocation with 'kubernetes'.
    }
    // Source: vvaharness/lang/detect.py:252-257
    if (the source predicate repo_root is truthy) {
      // Source: vvaharness/lang/detect.py:253-253
      In source order: Evaluate once _read_head(repo_root, rel); assign in source target order to head.
      // Source: vvaharness/lang/detect.py:254-255
      if (the source predicate _ANSIBLE_BODY_RX.search(head) is truthy) {
        // Source: vvaharness/lang/detect.py:255-255
        End this invocation with 'ansible'.
      }
      // Source: vvaharness/lang/detect.py:256-257
      if (the source predicate _K8S_BODY_RX.search(head) is truthy) {
        // Source: vvaharness/lang/detect.py:257-257
        End this invocation with 'kubernetes'.
      }
    }
    // Source: vvaharness/lang/detect.py:258-258
    End this invocation with None.
  }
  // Source: vvaharness/lang/detect.py:260-261
  if (the source predicate suffix is truthy) {
    // Source: vvaharness/lang/detect.py:261-261
    End this invocation with None.
  }
  // Source: vvaharness/lang/detect.py:264-275
  if (the source predicate _MAINFRAME_PATH_RX.search(rel) and repo_root is truthy) {
    // Source: vvaharness/lang/detect.py:265-265
    In source order: Evaluate once _read_head(repo_root, rel); assign in source target order to head.
    // Source: vvaharness/lang/detect.py:266-267
    if (the source predicate _JCL_BODY_RX.search(head) is truthy) {
      // Source: vvaharness/lang/detect.py:267-267
      End this invocation with 'jcl'.
    }
    // Source: vvaharness/lang/detect.py:268-269
    if (the source predicate _COBOL_BODY_RX.search(head) is truthy) {
      // Source: vvaharness/lang/detect.py:269-269
      End this invocation with 'cobol'.
    }
  }
  else {
    // Source: vvaharness/lang/detect.py:270-275
    if (the source predicate repo_root is truthy) {
      // Source: vvaharness/lang/detect.py:271-271
      In source order: Evaluate once _read_head(repo_root, rel, 1024); assign in source target order to head.
      // Source: vvaharness/lang/detect.py:272-273
      if (the source predicate _JCL_BODY_RX.search(head) is truthy) {
        // Source: vvaharness/lang/detect.py:273-273
        End this invocation with 'jcl'.
      }
      // Source: vvaharness/lang/detect.py:274-275
      if (the source predicate _COBOL_BODY_RX.search(head) is truthy) {
        // Source: vvaharness/lang/detect.py:275-275
        End this invocation with 'cobol'.
      }
    }
  }
  // Source: vvaharness/lang/detect.py:276-276
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/lang/detect.py:279-291
// Source signature: detect_languages(files: list[str], repo_root: Path | str | None=None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_languages(files, repo_root) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/lang/detect.py:281-283
  In source order: Retain source documentation literal source_literal_281_4; it is not a model call. Then Evaluate once Path(repo_root) if repo_root else None; assign in source target order to root. Then For counts, assign {}; source annotation dict[str, int].
  // Source: vvaharness/lang/detect.py:284-290
  for each f in files {
    // Source: vvaharness/lang/detect.py:285-286
    In source order: Evaluate once PurePosixPath(f).suffix.lower(); assign in source target order to suffix. Then Evaluate once EXT_TO_LANG.get(suffix); assign in source target order to lang.
    // Source: vvaharness/lang/detect.py:287-288
    if (the source predicate lang is None or suffix in ('.yml', '.yaml') is truthy) {
      // Source: vvaharness/lang/detect.py:288-288
      In source order: Evaluate once _sniff_lang(f, root) or lang; assign in source target order to lang.
    }
    // Source: vvaharness/lang/detect.py:289-290
    if (the source predicate lang is truthy) {
      // Source: vvaharness/lang/detect.py:290-290
      In source order: Evaluate once counts.get(lang, 0) + 1; assign in source target order to counts[lang].
    }
  }
  // Source: vvaharness/lang/detect.py:291-291
  End this invocation with [k for k, _ in sorted(counts.items(), key=lambda kv: -kv[1])].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/lang/detect.py:294-315
In source order: For VVAH_LANGUAGES, assign frozenset({'python', 'java', 'javascript', 'typescript', 'go', 'csharp'}); source annotation frozenset[str]. Then For _LANG_ALIASES, assign {'python': 'python', 'py': 'python', 'python3': 'python', 'java': 'java', 'javascript': 'javascript', 'js': 'javascript', 'node': 'javascript', 'typescript': 'typescript', 'ts': 'typescript', 'go': 'go', 'golang': 'go', 'csharp': 'csharp', 'c#': 'csharp', 'cs': 'csharp', 'dotnet': 'csharp', 'kotlin': 'kotlin', 'kt': 'kotlin', 'scala': 'scala', 'ruby': 'ruby', 'rb': 'ruby', 'php': 'php', 'c': 'c-cpp', 'cpp': 'c-cpp', 'c++': 'c-cpp', 'cxx': 'c-cpp'}; source annotation dict[str, str].
// Source: vvaharness/lang/detect.py:317-321
// Source signature: canonical_lang(value: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn canonical_lang(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/lang/detect.py:318-320
  In source order: Retain source documentation literal source_literal_318_4; it is not a model call. Then Evaluate once str(value or '').strip().lower(); assign in source target order to key.
  // Source: vvaharness/lang/detect.py:321-321
  End this invocation with _LANG_ALIASES.get(key, key).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
