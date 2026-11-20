"""Combine completed structural/resource coverage with readable views and vocabulary."""
from __future__ import annotations

import ast
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

from complete_representation import OUT, SRC, cell, digest, tsv


def read_rows(name):
    with (OUT / name).open() as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    manifest = json.loads((OUT / "structural_manifest.json").read_text())
    python = {r["source"]: r for r in manifest}
    resources = {r["source"]: r for r in read_rows("resource_coverage.tsv")}
    prompt_content = {r["source"]:r for r in read_rows("prompt_content_coverage.tsv")}
    coverage = []
    prompt_locations = []
    prompts = []
    component = defaultdict(list)
    for p in sorted(SRC.rglob("*")):
        if not p.is_file(): continue
        rel = p.relative_to(SRC).as_posix()
        if rel in python:
            m = python[rel]
            status, target, note = "represented-structural", m["representation"], "complete local AST rendering; external runtime behavior remains explicit boundary"
            e = json.loads((OUT / m["evidence"]).read_text())
            prompts.append([rel,len(e["strings"]),m["evidence"],digest(p),"all literals/templates; only caller determines model-facing use; behavioral view: "+prompt_content.get(rel,{}).get("representation","none identified; see triage")])
            for index, literal in enumerate(e['strings']):
                prompt_locations.append([rel,literal['line_start'],literal['line_end'],literal['column'],
                    m['evidence'],f"strings[{index}]",literal['context']+'; source caller determines model-facing use; instruction conversion: '+prompt_content.get(rel,{}).get("representation","none identified; see triage")])
        elif rel in resources:
            row = resources[rel]
            status,target,note=row["status"],row["representation"],row["role"]
            if status=="excluded-test": note="test/fixture excluded from runtime conversion; inventoried and hashed, not executed"
            if status=="prompt-document": prompts.append([rel,"whole document",row["asset"],digest(p),row["role"]])
            if status not in ('excluded-test','context-binary') and p.stat().st_size:
                prompt_locations.append([rel,1,max(1,len(p.read_text().splitlines())),0,row['asset'],
                    'complete exact source asset',row['role']+'; text/data, not guaranteed model use'])
        else: raise AssertionError(f"unclassified source: {rel}")
        pc = prompt_content.get(rel,{})
        coverage.append([rel,len(p.read_bytes().splitlines()),digest(p),status,target,note,pc.get("status","no instruction-bearing carrier identified; see triage"),pc.get("representation",""),pc.get("notes","repository tests excluded" if status=="excluded-test" else "all maximal Python strings triaged")])
        key="/".join(rel.split("/")[:2])
        component[key].append((rel,status,target))
    tsv(OUT/"coverage.tsv",["source_path","lines","sha256","status","representation_or_asset","notes","prompt_content_status","model_instruction_representation","prompt_content_notes"],coverage)
    tsv(OUT/"prompt_assets.tsv",["source","string_nodes","asset","source_sha256","role"],prompts)
    for row in read_rows('embedded_python.tsv'):
        asset_path='assets/'+row['source']+f".embedded-L{row['line_start']}.evidence.json"
        evidence=json.loads((OUT/asset_path).read_text())
        for index, literal in enumerate(evidence['strings']):
            prompt_locations.append([row['source'],literal['line_start'],literal['line_end'],literal['column'],
                asset_path,f"strings[{index}]",literal['context']+' in embedded Python; caller determines model-facing use'])
    for row in read_rows('configuration_values.tsv'):
        if row['yaml_type']=='tag:yaml.org,2002:str':
            prompt_locations.append([row['source'],row['line_start'],row['line_end'],0,
                'assets/original/'+row['source'],'YAML key '+row['key'],
                'source data string, including prompt templates/instructions; loader determines model-facing use'])
    tsv(OUT/'prompt_locations.tsv',['source','line_start','line_end','column','asset','lookup','role'],prompt_locations)

    links=[]
    for root in [OUT/"representation",OUT/"source_detail",OUT/"prompt_representation"]:
        for path in sorted(root.rglob("*.sudo.md")):
            for ln,line in enumerate(path.read_text().splitlines(),1):
                match=re.match(r"\s*// Source: (.+):(\d+)-(\d+)\s*$",line)
                if match:
                    source,start,end=match.groups()
                    links.append([path.relative_to(OUT).as_posix(),ln,source,int(start),int(end)])
    for ln,line in enumerate((OUT/'prompt_workflow.sudo.md').read_text().splitlines(),1):
        match=re.match(r"\s*// Source: (.+):(\d+)-(\d+)\s*$",line)
        if match:
            source,start,end=match.groups();links.append(['prompt_workflow.sudo.md',ln,source,int(start),int(end)])
    tsv(OUT/"source_links.tsv",["representation","representation_line","source","line_start","line_end"],links)

    concept_header=[
      "# Vocabulary additions", "",
      "All entries are ordinary identifiers/concepts within SudoLang v2.0; none changes its grammar. "
      "No vocabulary-extension file was supplied. Source spellings are reused when meanings match; "
      "source scopes, symbol roles and member receivers keep distinct meanings separate. No entry is reused from a supplied extension.", "",
      "The exhaustive tables below record each source binding/member/parameter/key and each converter "
      "literal/template identifier, with its local definition, original spelling, need, kind, source and use. "
      "A local source expression anchors a binding's meaning; an imported API is not thereby assigned "
      "unobserved implementation behavior. Evidence names also occur in the linked module's JSON asset. "
      "Ordinary English explanatory prose and baseline constructs are not newly declared identifiers.", "",
      "## Representation concepts", "", "| Term | Definition | Why needed | Kind | Original wording | Source | Used in | Reuse |",
      "|---|---|---|---|---|---|---|---|"]
    concepts=[
      ("S0–S11","Original ordered scan stages from seed through validation","preserve workflow hierarchy","tool-specific","stage ids","vvaharness/orchestrator/scan.py:569-1066","representation/harness.sudo.md"),
      ("model request","Instruction text given to a model; compliance is not guaranteed","separate requested behavior from host execution","general harness concept","prompt/system/schema description","vvaharness/pipeline/stages/s4/prompts.py:423-444","representation/harness.sudo.md"),
      ("source predicate","Truthiness test of the exact cited source expression","retain gates without adding operator grammar","general harness concept","Python condition","every source_detail module with If/While","source_detail/"),
      ("structural detail","Nested statement rendering preserving the source organization and expression evidence","review low-level decisions omitted from concise map","general harness concept","converter term; no original identifier","structural_manifest.json","source_detail/"),
      ("source_literal_LINE_COLUMN","Exact original long string at a source coordinate; each instantiated name is enumerated below","retain full prompt text without repeating it at each use","general harness concept","unnamed source string","assets/<module>.evidence.json","source_detail/"),
      ("source_template_LINE_COLUMN","Original f-string evaluated at its source site, with unchanged interpolation","avoid freezing or inventing dynamic prompt text","general harness concept","unnamed source f-string","assets/<module>.evidence.json","source_detail/"),
      ("checkpoint","Typed JSON state keyed by path-derived run_id and step in SQLite","describe resume and provenance","general harness concept","checkpoint","vvaharness/orchestrator/checkpoints.py:241-301","representation/vvaharness/orchestrator/checkpoints.sudo.md"),
      ("evidence gate","Source middleware conditionally rejecting premature outcomes, with finite relent behavior","retain code-versus-prompt distinction","general harness concept","EvidenceGate","vvaharness/backends/harness/deepagents/evidence_gate.py:80-223","representation/vvaharness/backends/harness/deepagents/evidence_gate.sudo.md"),
      ("None","Source no-value sentinel, distinct from false/empty collections","preserve optional-value branches","general harness concept","None","vvaharness/orchestrator/checkpoints.py:266-301","source_detail/"),
      ("EV","Optional exploit-verification path nested inside S6","preserve live/static branching","tool-specific","exploit verification","vvaharness/exploit_verification/verify/router.py:301-607","representation/harness.sudo.md"),
    ]
    for term,definition,why,kind,original,source,used in concepts:
        concept_header.append("| "+" | ".join(map(cell,[term,definition,why,kind,original,source,used,"newly recorded; no supplied extension reused"]))+" |")
    vocabulary=concept_header
    symbols=read_rows("vocabulary_symbols.tsv")+read_rows("resource_vocabulary.tsv")
    seen=set()
    grouped=defaultdict(list)
    for row in symbols:
        key=(row["source"],row.get("scope", "module"),row["identifier"],row["role"])
        if key in seen: continue
        seen.add(key);grouped[row["source"]].append(row)
    # Explicit identifiers introduced by the readable converter wrappers and their argument names.
    for file in sorted((OUT/"representation").rglob("*.sudo.md")):
        source="";start=end=1
        for ln,line in enumerate(file.read_text().splitlines(),1):
            m=re.match(r"\s*// Source: (.+):(\d+)-(\d+)",line)
            if m: source,start,end=m.group(1),int(m.group(2)),int(m.group(3))
            f=re.search(r"\bfn ([\w.]+)\(([^)]*)\)",line)
            if f:
                for name in [f.group(1),*re.findall(r"\b[A-Za-z_]\w*\b",f.group(2))]:
                    key=(source,f"readable {file.relative_to(OUT)}:{ln}",name,"readable source-procedure/parameter vocabulary")
                    if key in seen:continue
                    seen.add(key)
                    grouped[source].append({"source":source,"identifier":name,"role":"readable source-procedure/parameter vocabulary",
                        "definition":line.strip(),"line_start":start,"line_end":end,
                        "used_in":f"{file.relative_to(OUT)}:{ln}",
                        "scope":f"readable {file.relative_to(OUT)}:{ln}",
                        "original_identifier":name.rsplit('.',1)[-1] if name==f.group(1) else name,
                        "reuse":"newly recorded; wrapper spelling may differ from original callable; original source procedure at cited span"})
    for source,entries in sorted(grouped.items()):
        vocabulary += ["",f"## `{source}`","","| Identifier | Source scope/context | Definition and local meaning | Why needed | Kind | Original wording | Source | Used in | Reuse |",
                       "|---|---|---|---|---|---|---|---|---|"]
        for r in sorted(entries,key=lambda x:(x["identifier"],x.get("scope",""),x["role"])):
            converter="converter" in r["role"] or "wrapper" in r["reuse"]
            original=r.get("original_identifier") or ("unnamed original literal/template or wrapper; source span defines it" if converter else r["identifier"])
            kind="general harness evidence identifier" if "converter" in r["role"] else "tool-specific identifier"
            vocabulary.append("| "+" | ".join(map(cell,[r["identifier"],r.get("scope","module"),r["role"]+": "+r["definition"][:700],
              "retain exact local binding, decision, schema/key or evidence reference without inference",kind,original,
              f"{source}:{r['line_start']}-{r['line_end']}",r["used_in"],r["reuse"]]))+" |")
    vocabulary += ["", "## Converted prompt vocabulary", "",
      "Existing source-scoped vocabulary was checked before adding these entries. Existing local meanings are reused; same spellings in different contexts are not merged. These are ordinary identifiers, not grammar changes. The existing `model request` concept also applies throughout `prompt_representation/` and `prompt_workflow.sudo.md`.", "",
      "| Identifier | Definition | Why needed | Kind | Original | Source | Used in | Reuse | Previous lookup |",
      "|---|---|---|---|---|---|---|---|---|"]
    for r in read_rows('prompt_vocabulary.tsv'):
        vocabulary.append('| '+' | '.join(map(cell,[r['identifier'],r['definition'],r['why'],r['kind'],r['original'],
            r['source']+':'+r['line_start']+'-'+r['line_end'],r['used_in'],r['reuse'],r['previous']]))+' |')
    (OUT/"vocabulary_extensions.md").write_text("\n".join(vocabulary)+"\n")
    nav=["# Source organization and component index","","Every source file is classified in coverage.tsv. Runtime detail and converted prompt instructions mirror original paths. Prompt behavior is expanded in [prompt_workflow.sudo.md](prompt_workflow.sudo.md); exact resources are evidence, not instruction conversion.",""]
    for key,entries in sorted(component.items()):
        nav += [f"## {key}","","| Source | Treatment | Representation |","|---|---|---|"]
        for source,status,target in entries:
            nav.append("| "+" | ".join(map(cell,[source,status,(target or "excluded test/fixture")+("; converted model requests: "+prompt_content[source]["representation"] if source in prompt_content and prompt_content[source]["status"].startswith("converted") else "")]))+" |")
        nav.append("")
    (OUT/"source_index.md").write_text("\n".join(nav)+"\n")
    print(json.dumps({"source_files":len(coverage),"python_modules":len(python),"resources_and_tests":len(resources),
                      "source_links":len(links),"vocabulary_entries":len(seen)+len(read_rows("prompt_vocabulary.tsv")),"prompt_vocabulary_entries":len(read_rows("prompt_vocabulary.tsv"))},indent=2))


if __name__=="__main__":main()
