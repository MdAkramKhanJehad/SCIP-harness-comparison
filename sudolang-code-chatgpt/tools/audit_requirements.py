"""Independent output-facing audit of source hierarchy, evidence and vocabulary.

This inspects artifacts rather than executing the harness or inferring model behavior.
It supplements check_complete.py; neither establishes semantic equivalence.
"""
from __future__ import annotations

import ast
import bisect
import copy
import csv
import json
import re
from collections import Counter
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
SRC = OUT.parent / 'visa-vulnerability-agentic-harness'


def read_rows(path):
    with path.open() as stream:
        yield from csv.DictReader(stream, delimiter='\t')


def node_key(node):
    return type(node).__name__, node.lineno, node.end_lineno, node.col_offset


def main():
    errors = []
    counts = Counter()
    manifest = json.loads((OUT/'structural_manifest.json').read_text())
    inventory = list(read_rows(OUT/'coverage.tsv'))
    actual_python = {p.relative_to(SRC).as_posix() for p in SRC.rglob('*.py')
                     if 'tests' not in p.relative_to(SRC).parts}
    if {m['source'] for m in manifest} != actual_python:
        errors.append('manifest does not cover exactly all supplied non-test Python')
    if len(inventory) != len({r['source_path'] for r in inventory}):
        errors.append('duplicate coverage rows')

    def audit_detail(rel, tree, asset, target, evidence_path):
        text = target.read_text()
        lines = text.splitlines()
        if f'Evidence: `{evidence_path}`.' not in text:
            errors.append('wrong evidence header: '+str(target.relative_to(OUT)))
        if not (OUT/evidence_path).is_file(): errors.append('missing evidence '+evidence_path)
        fence = lines.index('```sudo') + 1
        preorder = []
        depths = {}
        parents = {}
        def visit(node, depth=0):
            if isinstance(node, ast.stmt):
                preorder.append(node_key(node)); depths[node_key(node)] = depth; depth += 1
            for child in ast.iter_child_nodes(node):
                parents[child] = node
                visit(child, depth)
        visit(tree)
        records = asset['statements']
        recorded = [(r['kind'],r['line_start'],r['line_end'],r['column']) for r in records]
        if preorder != recorded: errors.append('statement order mismatch: '+rel)
        positions = [r['representation_line']+fence-1 for r in records]
        if positions != sorted(positions): errors.append('rendered statement order mismatch: '+rel)
        distinct = sorted(set(positions))
        ranges = {}
        by_key = {node_key(n):n for n in ast.walk(tree) if isinstance(n,ast.stmt)}
        for r, start, key in zip(records,positions,recorded):
            if start >= len(lines): errors.append('bad statement location: '+rel); continue
            indent = len(lines[start])-len(lines[start].lstrip())
            if indent != 2*depths[key]: errors.append(f'source nesting mismatch: {rel}:{r["line_start"]}')
            end_idx = bisect.bisect_right(distinct,start)
            end = distinct[end_idx] if end_idx<len(distinct) else lines.index('```',fence)
            region = '\n'.join(lines[start:end])
            ranges[key] = region
            node = by_key[key]
            markers = {
                'If':'if (the source predicate ', 'While':'while (the source predicate ',
                'For':'for each ', 'AsyncFor':'for each ',
                'Try':'Perform the following protected operations {',
                'With':'Enter source context managers left-to-right:',
                'AsyncWith':'Await and enter source context managers left-to-right:',
                'Return':'End this invocation with ', 'Raise':'Raise ',
                'Break':'Leave the immediately enclosing source loop',
                'Continue':'Continue the immediately enclosing source loop',
                'Assert':'Enforce source assert ',
            }
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
                marker = f'fn {node.name}('
                if '// Source signature: '+node.name+'('+ast.unparse(node.args)+')' not in region:
                    errors.append(f'signature mismatch: {rel}:{node.lineno}')
                counts['function_signatures'] += 1
            elif isinstance(node,ast.ClassDef): marker = 'interface '+node.name+' {'
            else: marker = markers.get(type(node).__name__)
            if marker and marker not in region: errors.append(f'missing rendered {type(node).__name__}: {rel}:{node.lineno}')
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and node.decorator_list:
                if 'evaluate and retain decorators top-to-bottom:' not in region:
                    errors.append(f'missing decorator pre-evaluation: {rel}:{node.lineno}')
                counts['decorated_definitions'] += 1
            counts['statement_output_locations'] += 1
        nodes = {}
        for node in ast.walk(tree):
            if hasattr(node,'lineno'): nodes.setdefault((type(node).__name__,node.lineno,node.col_offset),[]).append(node)
        raw_source = (SRC/rel).read_text()
        class RestoreEvidence(ast.NodeTransformer):
            def visit_Name(self,node):
                record=asset['literals'].get(node.id)
                if record is None:return node
                prefix,ln,col=node.id.rsplit('_',2)
                kind='JoinedStr' if prefix=='source_template' else 'Constant'
                options=nodes.get((kind,int(ln),int(col)),[])
                for original in options:
                    correct = (ast.get_source_segment(raw_source,original)==record.get('source_expression')
                               if kind=='JoinedStr' else original.value==record.get('value'))
                    if correct:return copy.deepcopy(original)
                raise ValueError('evidence proxy has no matching source value: '+node.id)
        for expr in asset.get('expressions',[]):
            if expr['rendered'] not in text:
                errors.append(f'expression missing from actual pseudocode: {rel}:{expr["line_start"]}')
            matches = nodes.get((expr['kind'],expr['line_start'],expr['column']),[])
            found = False
            for node in matches:
                if ast.dump(node,include_attributes=False)!=expr['original_ast']: continue
                found = True
                parent = node
                while not isinstance(parent,(ast.stmt,ast.ExceptHandler)) and parent in parents:
                    parent = parents[parent]
                if isinstance(parent,ast.stmt):
                    region=ranges.get(node_key(parent),'')
                    if expr['rendered'] not in region:
                        errors.append(f'expression in wrong statement: {rel}:{expr["line_start"]}')
                break
            if not found:errors.append(f'original expression absent from source: {rel}:{expr["line_start"]}')
            try:
                if expr['kind']=='AugAssign': parsed=ast.parse(expr['rendered']).body[0]
                elif expr['kind']=='keyword':parsed=ast.parse('f('+expr['rendered']+')',mode='eval').body.keywords[0]
                else:parsed=ast.parse(expr['rendered'],mode='eval').body
                if ast.dump(RestoreEvidence().visit(parsed),include_attributes=False)!=expr['original_ast']:
                    errors.append(f'output expression roundtrip mismatch: {rel}:{expr["line_start"]}')
            except Exception as exc:errors.append(f'output expression audit error: {rel}:{expr["line_start"]}: {exc}')
            counts['expressions_present_in_output'] += 1
        names = set(re.findall(r'\bsource_(?:literal|template)_\d+_\d+\b',text))
        if names != set(asset['literals']): errors.append('literal/template proxy coverage mismatch: '+rel)
        counts['resolved_evidence_identifiers'] += len(names)
        counts['detailed_python_units'] += 1

    for module in manifest:
        rel=module['source']
        audit_detail(rel,ast.parse((SRC/rel).read_text()),json.loads((OUT/module['evidence']).read_text()),
                     OUT/module['representation'],module['evidence'])
    for row in read_rows(OUT/'embedded_python.tsv'):
        rel=row['source']; raw=(SRC/rel).read_text()
        begin,end=int(row['line_start']),int(row['line_end'])
        snippet='\n'.join(raw.splitlines()[begin-1:end])+'\n'
        tree=ast.parse(snippet); ast.increment_lineno(tree,begin-1)
        evidence_path='assets/'+rel+f'.embedded-L{begin}.evidence.json'
        asset=json.loads((OUT/evidence_path).read_text())
        if asset['source_text']!=snippet:errors.append('embedded source mismatch: '+rel)
        audit_detail(rel,tree,asset,OUT/row['representation'],evidence_path)
        counts['embedded_python_units'] += 1
    # Vocabulary uses must resolve to actual files and source ranges. Scope and role
    # are independent identity dimensions; a repeated spelling is not one shared meaning.
    vocab_keys=set(); spellings={}
    line_counts={}; representation_line_counts={}
    for table in ['vocabulary_symbols.tsv','resource_vocabulary.tsv']:
        for row in read_rows(OUT/table):
            key=(row['source'],row.get('scope',''),row['identifier'],row['role'])
            vocab_keys.add(key)
            spellings.setdefault((row['source'],row['identifier']),set()).add(row.get('scope',''))
            source=SRC/row['source']
            if row['source'] not in line_counts:line_counts[row['source']]=len(source.read_text().splitlines())
            if not 1<=int(row['line_start'])<=int(row['line_end'])<=line_counts[row['source']]:
                errors.append('vocabulary source span invalid: '+str(key))
            for use in row['used_in'].split('; '):
                name,sep,line=use.rpartition(':')
                if not sep or not line.isdigit(): name=use;line=None
                target=OUT/name
                if not target.is_file(): errors.append('missing vocabulary use '+use)
                elif line:
                    if name not in representation_line_counts:representation_line_counts[name]=len(target.read_text().splitlines())
                    if not 1<=int(line)<=representation_line_counts[name]:errors.append('invalid vocabulary use '+use)
            counts['vocabulary_rows_checked'] += 1
    counts['same_spelling_distinct_scopes']=sum(len(scopes)>1 for scopes in spellings.values())
    # All exact non-Python resources are evidence, not implied executable stages.
    for row in read_rows(OUT/'resource_coverage.tsv'):
        if row['asset']:
            if (OUT/row['asset']).read_bytes()!=(SRC/row['source']).read_bytes():errors.append('resource mismatch: '+row['source'])
            counts['resource_bytes_checked']+=1
    for table in ['configuration_values.tsv','prompt_locations.tsv']:
        for row in read_rows(OUT/table):
            rel=row['source']
            if rel not in line_counts:line_counts[rel]=len((SRC/rel).read_text().splitlines())
            if not 1<=int(row['line_start'])<=int(row['line_end'])<=line_counts[rel]:
                errors.append(f'invalid {table} source span: {rel}:{row["line_start"]}-{row["line_end"]}')
            if 'asset' in row and not (OUT/row['asset']).is_file():errors.append('missing prompt evidence '+row['asset'])
            counts[table.removesuffix('.tsv')+'_spans_checked']+=1
    result={'scope':'source/output structure, evidence links, scoped vocabulary and resource audit; no runtime equivalence claim',
            'checks':dict(counts),'errors':errors,'passed':not errors}
    (OUT/'audit_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    raise SystemExit(bool(errors))


if __name__=='__main__':main()
