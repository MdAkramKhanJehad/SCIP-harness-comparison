"""Function-level coverage: for every rendered Python file, how many of its functions/classes appear in the pseudocode.

  python3 tools/check_functions.py                 # per-harness totals + worst files
  python3 tools/check_functions.py --harness vvah --min-source 100 --below 0.6 -v

A source function counts as rendered when its name (lowercased, underscores removed) occurs as an identifier in the
pseudocode file that mirrors it. This is a name check, not an equivalence check: it finds files that were summarised
instead of rendered, and the specific functions missing from them. Python sources only.
"""
import argparse
import ast
import re
from pathlib import Path

from harnesses import HARNESSES, PSEUDO


def norm(name):
    return name.replace("_", "").lower()


def source_functions(path):
    try:
        tree = ast.parse(path.read_text(errors="replace"))
    except SyntaxError:
        return None
    out = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.name in ("__init__", "__repr__", "__str__", "__eq__", "__hash__", "__post_init__", "__enter__", "__exit__"):
                continue
            body = getattr(node, "end_lineno", node.lineno) - node.lineno + 1
            out.append((node.name, node.lineno, body))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--harness", choices=[h["key"] for h in HARNESSES])
    ap.add_argument("--min-source", type=int, default=60, help="only report files with at least this many source lines")
    ap.add_argument("--below", type=float, default=0.7, help="report files whose function coverage is below this")
    ap.add_argument("-v", action="store_true", help="list the missing function names")
    ap.add_argument("--only", action="append", default=[], help="only source files whose path contains this text (repeatable); "
                    "with --only, every file is listed with its missing functions and line numbers")
    a = ap.parse_args()
    for h in HARNESSES:
        if a.harness and a.harness != h["key"]:
            continue
        repo, folder = Path(h["repo"]), PSEUDO / h["folder"]
        # source file -> union of identifiers in every pseudocode file that names it (header or src pointer)
        idents, renders = {}, {}
        for p in sorted(folder.rglob("*.pseudo")):
            text = p.read_text()
            words = {norm(w) for w in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", text)}
            first = text.splitlines()[0] if text else ""
            cited = {s.strip() for s in first.removeprefix("// file: ").split(",")} if first.startswith("// file: ") else set()
            cited |= set(re.findall(r"src:\s*([^\s:,;]+\.[a-z]+):\d+", text))
            cited |= set(re.findall(r'@src\("([^":]+):\d+', text))
            for rel in cited:
                idents.setdefault(rel, set()).update(words)
                renders.setdefault(rel, []).append(p.relative_to(folder).as_posix())
        tot_f = tot_hit = n_files = 0
        weak = []
        for rel in sorted(idents):
            src = repo / rel
            if src.suffix != ".py" or not src.is_file():
                continue
            funcs = source_functions(src)
            if not funcs:
                continue
            missing = [(n, ln, sz) for n, ln, sz in funcs if norm(n) not in idents[rel]]
            if a.only and not any(o in rel for o in a.only):
                continue
            n_files += 1
            tot_f += len(funcs)
            tot_hit += len(funcs) - len(missing)
            nlines = len(src.read_text(errors="replace").splitlines())
            if a.only and missing:
                weak.append((rel, nlines, renders[rel], len(funcs), len(missing), missing))
            elif not a.only and nlines >= a.min_source and (len(funcs) - len(missing)) / len(funcs) < a.below:
                weak.append((rel, nlines, renders[rel], len(funcs), len(missing), missing))
        pct = 100 * tot_hit / max(tot_f, 1)
        print(f"[{h['key']}] python files {n_files}, functions/classes {tot_f}, named in pseudocode {tot_hit} ({pct:.0f}%)")
        for rel, nl, files, nf, nm, missing in sorted(weak, key=lambda w: -w[4])[:(400 if a.only else 40)]:
            print(f"  {rel}: source {nl} lines, {nf - nm}/{nf} functions named  (rendered in {', '.join(files)[:90]})")
            if a.v or a.only:
                print("      missing:", ", ".join(f"{n}@{ln}" for n, ln, _ in sorted(missing, key=lambda m: m[1])[:80]))


if __name__ == "__main__":
    main()
