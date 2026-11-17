"""Check every file:line citation and quotation in the analysis documents against the real repositories.

  python3 verify_citations.py 01-high-level-design-conflicts.md 02-mid-level-conflicts.md

For each paragraph: every `path:line` (and `path:line` to `:line`) must name an existing file and an in-range line; every
double-quoted phrase of three or more words must occur (ignoring case and whitespace) within five lines of a cited line of
a file cited in the same paragraph, or anywhere in a cited file. Reports what cannot be confirmed.
"""
import re
import sys
from pathlib import Path

ROOT = Path("/home/spl/akram/harness-comparison")
REPOS = [ROOT / "VulnHunter", ROOT / "visa-vulnerability-agentic-harness"]
CITE = re.compile(r"`([A-Za-z0-9_./\-]+\.[A-Za-z0-9]+):(\d+)`(?:\s*(?:to|and)\s*`:(\d+)`)?")


def resolve(path):
    for r in REPOS:
        if (r / path).is_file():
            return r / path
    return None


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[`*_]", "", s)).strip().lower()


bad = total_c = total_q = 0
for doc in sys.argv[1:]:
    text = Path(doc).read_text()
    for pno, para in enumerate(re.split(r"\n\s*\n", text), 1):
        cites = []
        for m in CITE.finditer(para):
            path, a, b = m.group(1), int(m.group(2)), m.group(3)
            total_c += 1
            f = resolve(path)
            if not f:
                if "/" in path and not path.startswith(("docs/", "inputs/")) and "." in path:
                    print(f"{doc} para {pno}: file not found {path}"); bad += 1
                continue
            n = len(f.read_text(errors="replace").splitlines())
            for ln in [a] + ([int(b)] if b else []):
                if ln > n:
                    print(f"{doc} para {pno}: {path}:{ln} beyond end of file ({n} lines)"); bad += 1
            cites.append((f, a, int(b) if b else a))
        for q in re.findall(r'"([^"\n]{12,}?)"', para):
            if len(q.split()) < 3:
                continue
            total_q += 1
            nq = norm(q)
            found = False
            for f, a, b in cites:
                lines = f.read_text(errors="replace").splitlines()
                near = norm(" ".join(lines[max(0, a - 6): b + 5]))
                if nq in near or nq in norm(" ".join(lines)):
                    found = True
                    break
            if not found and cites:
                print(f"{doc} para {pno}: quotation not found in cited files: \"{q[:90]}\""); bad += 1
print(f"checked {total_c} citations and {total_q} quotations; {bad} problems")
