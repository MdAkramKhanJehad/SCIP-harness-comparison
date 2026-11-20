"""Independent structural/expression/evidence checks; never execute source behavior."""
from __future__ import annotations

import ast
import copy
import csv
import json
import re
from collections import Counter

from complete_representation import OUT, SRC, digest


def rows(name):
    with (OUT/name).open() as f:return list(csv.DictReader(f,delimiter="\t"))


def main():
    errors=[]; checks=Counter()
    coverage=rows("coverage.tsv")
    actual={p.relative_to(SRC).as_posix() for p in SRC.rglob("*") if p.is_file()}
    if actual!={r["source_path"] for r in coverage}:errors.append("source inventory mismatch")
    texts={}
    for r in coverage:
        p=SRC/r["source_path"]
        if digest(p)!=r["sha256"]:errors.append("source hash changed: "+r["source_path"])
        if r["representation_or_asset"] and not (OUT/r["representation_or_asset"]).is_file():errors.append("missing representation: "+r["source_path"])
        if r["status"]=="pending":errors.append("pending source remains: "+r["source_path"])
        checks["source_hashes"]+=1
    manifest=json.loads((OUT/"structural_manifest.json").read_text())
    for module in manifest:
        rel=module["source"]; raw=(SRC/rel).read_text();texts[rel]=raw
        tree=ast.parse(raw)
        asset=json.loads((OUT/module["evidence"]).read_text())
        if asset["source_text"]!=raw or asset["sha256"]!=digest(SRC/rel):errors.append("source evidence differs: "+rel)
        if module["representation_sha256"]!=digest(OUT/module["representation"]):errors.append("detail changed since rendering: "+rel)
        original=Counter((type(n).__name__,n.lineno,n.end_lineno,n.col_offset) for n in ast.walk(tree) if isinstance(n,ast.stmt))
        rendered=Counter((r["kind"],r["line_start"],r["line_end"],r["column"]) for r in asset["statements"])
        if original!=rendered:errors.append("statement coverage differs: "+rel)
        checks["python_modules"]+=1;checks["python_statements"]+=sum(original.values())
        strings=Counter((n.lineno,n.end_lineno,n.col_offset,n.value) for n in ast.walk(tree) if isinstance(n,ast.Constant) and isinstance(n.value,str))
        extracted=Counter((n["line_start"],n["line_end"],n["column"],n["value"]) for n in asset["strings"])
        if strings!=extracted:errors.append("string extraction differs: "+rel)
        checks["string_nodes"]+=sum(strings.values())
        nodes={}
        for n in ast.walk(tree):
            key=(type(n).__name__,getattr(n,"lineno",0),getattr(n,"col_offset",0))
            nodes.setdefault(key,[]).append(n)
        literals=asset["literals"]
        class Restore(ast.NodeTransformer):
            def visit_Name(self,n):
                if n.id not in literals:return n
                prefix,ln,col=n.id.rsplit("_",2)
                record=literals[n.id]
                kind="JoinedStr" if prefix=="source_template" else "Constant"
                candidates=nodes.get((kind,int(ln),int(col)),[])
                if not candidates:raise ValueError("missing original proxy node "+n.id)
                if prefix=="source_template":
                    if not any(ast.get_source_segment(raw,c)==record["source_expression"] for c in candidates):
                        raise ValueError("template source evidence differs")
                    return ast.parse("("+record["source_expression"]+"\n)",mode="eval").body
                if not any(c.value==record["value"] for c in candidates):raise ValueError("literal source evidence differs")
                return ast.Constant(value=record["value"])
        for expr in asset.get("expressions",[]):
            try:
                if expr["kind"]=="AugAssign":parsed=ast.parse(expr["rendered"]).body[0]
                elif expr["kind"]=="keyword":parsed=ast.parse("f("+expr["rendered"]+")",mode="eval").body.keywords[0]
                else:parsed=ast.parse(expr["rendered"],mode="eval").body
                restored=Restore().visit(parsed)
                candidates=nodes[(expr["kind"],expr["line_start"],expr["column"])]
                expected=expr["original_ast"]
                if not any(ast.dump(c,include_attributes=False)==expected for c in candidates):
                    errors.append(f"original expression missing from source: {rel}:{expr['line_start']}")
                if ast.dump(restored,include_attributes=False)!=expected:
                    errors.append(f"expression mismatch: {rel}:{expr['line_start']}")
            except Exception as e:errors.append(f"expression check error: {rel}:{expr['line_start']}: {e}")
            checks["expression_roundtrips"]+=1
    for r in rows("resource_coverage.tsv"):
        if not r["asset"]:continue
        if (OUT/r["asset"]).read_bytes()!=(SRC/r["source"]).read_bytes():errors.append("resource bytes differ: "+r["source"])
        checks["exact_resource_copies"]+=1
    for r in rows("embedded_python.tsv"):
        raw=(SRC/r["source"]).read_text().splitlines()
        snippet="\n".join(raw[int(r["line_start"])-1:int(r["line_end"])])+"\n"
        tree=ast.parse(snippet); ast.increment_lineno(tree,int(r["line_start"])-1)
        count=sum(isinstance(n,ast.stmt) for n in ast.walk(tree))
        if count!=int(r["statements"]):errors.append("embedded Python coverage differs: "+r["source"])
        checks["embedded_python_statements"]+=count;checks["embedded_python_blocks"]+=1
    for r in rows("source_links.tsv"):
        raw=texts.get(r["source"])
        if raw is None:
            try:raw=(SRC/r["source"]).read_text();texts[r["source"]]=raw
            except UnicodeDecodeError:errors.append("binary source has a line citation: "+r["source"]);continue
        if not 1<=int(r["line_start"])<=int(r["line_end"])<=max(1,len(raw.splitlines())):
            errors.append("invalid citation range: "+str(r))
        line=(OUT/r["representation"]).read_text().splitlines()[int(r["representation_line"])-1].strip()
        if line!=f"// Source: {r['source']}:{r['line_start']}-{r['line_end']}":errors.append("stale citation: "+str(r))
        checks["source_citations"]+=1
    local_targets={m["source"] for m in manifest}
    for r in rows("import_links.tsv"):
        for target in filter(None,r["local_targets"].split(";")):
            if target not in local_targets:errors.append("missing local import detail: "+target)
            checks["local_import_targets"]+=1
    for r in rows("baseline_review.tsv"):
        if digest(OUT/r["path"])!=r["sha256"]:errors.append("baseline changed: "+r["path"])
        checks["baseline_reading_records"]+=1
    examples=list((OUT/"reference/sudolang/examples").rglob("*"))
    checks["example_files"]=sum(p.is_file() for p in examples)
    result={"scope":"static artifact, exact-expression and coverage checks; not runtime/semantic equivalence proof",
            "checks":dict(checks),"coverage_counts":dict(Counter(r["status"] for r in coverage)),
            "errors":errors,"passed":not errors}
    (OUT/"verification.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2));raise SystemExit(bool(errors))


if __name__=="__main__":main()
