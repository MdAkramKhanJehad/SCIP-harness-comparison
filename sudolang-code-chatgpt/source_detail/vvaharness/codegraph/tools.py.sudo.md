# vvaharness/codegraph/tools.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/codegraph/tools.py.evidence.json`. SHA-256: `81de5345e293ab32889976826395a99301cc68e187533d4cb4b6d7d3c20f5107`.

```sudo
// Source: vvaharness/codegraph/tools.py:15-20
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import functools; preserve alias and import-time effects. Then Resolve source import from collections.abc import Callable, Iterable, Mapping, Sequence; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vvaharness/codegraph/tools.py:22-29
In source order: Resolve source import from context_graph_sdk import SymbolAmbiguousError, SymbolSelector; preserve alias and import-time effects. Then Resolve source import from langchain_core.tools import BaseTool, tool; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness import StreamingOptions; preserve alias and import-time effects. Then Resolve source import from vvaharness.backends.harness.deepagents.tools import build_tools as build_reader_tools; preserve alias and import-time effects. Then Resolve source import from vvaharness.codegraph.handle import GraphHandle; preserve alias and import-time effects.
// Source: vvaharness/codegraph/tools.py:30-37
In source order: Resolve source import from vvaharness.models import ContextPackage; preserve alias and import-time effects. Then Resolve source import from vvaharness.util.counters import COUNTERS; preserve alias and import-time effects. Then Evaluate once {'candidate_limit': 5, 'group_limit': 8, 'call_depth': 2, 'max_nodes': 60, 'max_edges': 120, 'max_paths': 8}; assign in source target order to _CONTEXT_LIMITS. Then Evaluate once {'candidate_limit': 5, 'max_depth': 4, 'max_nodes': 80, 'max_edges': 160, 'max_paths': 10}; assign in source target order to _IMPACT_LIMITS. Then Evaluate once 20; assign in source target order to _REF_CAP.
// Source: vvaharness/codegraph/tools.py:38-54
In source order: Evaluate once 6; assign in source target order to _PATH_CAP. Then Evaluate once source_literal_40_19; assign in source target order to _NEIGHBORS_QUERY. Then Evaluate once source_literal_45_17; assign in source target order to _CALLERS_QUERY. Then Evaluate once source_literal_50_19; assign in source target order to _IMPORTERS_QUERY.
// Source: vvaharness/codegraph/tools.py:57-60
// Source signature: _qname(row: dict) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _qname(row) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:58-59
  In source order: Retain source documentation literal source_literal_58_4; it is not a model call. Then Evaluate once (row.get('file'), row.get('name')); assign in source target order to (file, name).
  // Source: vvaharness/codegraph/tools.py:60-60
  End this invocation with source_template_60_11 if isinstance(file, str) and isinstance(name, str) else ''.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:63-67
// Source signature: _ref(entity: object) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _ref(entity) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:64-66
  In source order: Retain source documentation literal source_literal_64_4; it is not a model call. Then Evaluate once getattr(entity, 'name', None) or getattr(entity, 'qualified_name', None) or ''; assign in source target order to name. Then Evaluate once getattr(entity, 'file_path', None) or getattr(entity, 'path', None) or ''; assign in source target order to path.
  // Source: vvaharness/codegraph/tools.py:67-67
  End this invocation with source_template_67_11 if path and name else str(name or path).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:70-72
// Source signature: _refs(entities: Iterable[object] | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refs(entities) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:71-71
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:72-72
  End this invocation with [r for e in entities or () if (r := _ref(e))][:_REF_CAP].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:75-78
// Source signature: _paths(paths: Iterable[object] | None) -> list[str]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _paths(paths) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:76-76
  In source order: Retain source documentation literal source_literal_76_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:77-78
  End this invocation with [' -> '.join(_refs(getattr(p, 'nodes', ()) or getattr(p, 'entities', ()))) for p in paths or ()][:_PATH_CAP].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:81-83
// Source signature: _selector(file: str, symbol: str | None, line: int | None=None) -> SymbolSelector
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _selector(file, symbol, line) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:82-82
  In source order: Retain source documentation literal source_literal_82_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:83-83
  End this invocation with SymbolSelector(symbol or file, file_path=file, line=line).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:86-95
// Source signature: _resolve_error(file: str, symbol: str, exc: Exception) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _resolve_error(file, symbol, exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:87-87
  In source order: Retain source documentation literal source_literal_87_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:88-94
  if (the source predicate isinstance(exc, SymbolAmbiguousError) is truthy) {
    // Source: vvaharness/codegraph/tools.py:89-90
    In source order: Evaluate once source_template_89_16; assign in source target order to hint.
  }
  else {
    // Source: vvaharness/codegraph/tools.py:92-94
    In source order: Evaluate once source_template_92_16; assign in source target order to hint.
  }
  // Source: vvaharness/codegraph/tools.py:95-95
  End this invocation with {'error': source_template_95_21, 'hint': hint}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:98-100
// Source signature: _cypher_error(exc: Exception) -> dict
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _cypher_error(exc) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:99-99
  In source order: Retain source documentation literal source_literal_99_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:100-100
  End this invocation with {'error': source_template_100_21}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:103-107
// Source signature: _is_empty_result(result: object) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_empty_result(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:104-104
  In source order: Retain source documentation literal source_literal_104_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:105-106
  if (the source predicate isinstance(result, dict) is truthy) {
    // Source: vvaharness/codegraph/tools.py:106-106
    End this invocation with all((not v for v in result.values() if isinstance(v, list))).
  }
  // Source: vvaharness/codegraph/tools.py:107-107
  End this invocation with result is None or (isinstance(result, list) and (not result)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:110-117
// Source signature: _count_result(result: object) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _count_result(result) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:111-111
  In source order: Retain source documentation literal source_literal_111_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:112-117
  if (the source predicate isinstance(result, dict) and 'error' in result is truthy) {
    // Source: vvaharness/codegraph/tools.py:113-113
    In source order: Evaluate COUNTERS.bump('graph_tool_result_error'); retain side effects and discard the expression result.
  }
  else {
    // Source: vvaharness/codegraph/tools.py:114-117
    if (the source predicate _is_empty_result(result) is truthy) {
      // Source: vvaharness/codegraph/tools.py:115-115
      In source order: Evaluate COUNTERS.bump('graph_tool_result_empty'); retain side effects and discard the expression result.
    }
    else {
      // Source: vvaharness/codegraph/tools.py:117-117
      In source order: Evaluate COUNTERS.bump('graph_tool_result_hit'); retain side effects and discard the expression result.
    }
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:120-127
// Source signature: _counted(fn: Callable[..., object]) -> Callable[..., object]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _counted(fn) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:121-121
  In source order: Retain source documentation literal source_literal_121_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:123-126
  // Source: vvaharness/codegraph/tools.py:122-122
  Before creating this callable, evaluate and retain decorators top-to-bottom: functools.wraps(fn).
  // Source: vvaharness/codegraph/tools.py:123-126
  // Source signature: _wrapper(*args: object, **kwargs: object) -> object
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _wrapper(args, kwargs) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:124-125
    In source order: Evaluate once fn(*args, **kwargs); assign in source target order to result. Then Evaluate _count_result(result); retain side effects and discard the expression result.
    // Source: vvaharness/codegraph/tools.py:126-126
    End this invocation with result.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/codegraph/tools.py:127-127
  End this invocation with _wrapper.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:130-132
// Source signature: _community_files(ctx: ContextPackage) -> dict[str, list[str]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _community_files(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:131-131
  In source order: Retain source documentation literal source_literal_131_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:132-132
  End this invocation with {m.name: m.files for m in getattr(ctx, 'modules', None) or ()}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:136-140
// Source: vvaharness/codegraph/tools.py:135-135
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/codegraph/tools.py:136-140
interface GraphToolContext {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/codegraph/tools.py:137-140
  In source order: Retain source documentation literal source_literal_137_4; it is not a model call. Then For handle, declare without assigning a value; source annotation GraphHandle. Then For ctx, declare without assigning a value; source annotation ContextPackage.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/codegraph/tools.py:143-165
// Source signature: _context_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _context_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:144-144
  In source order: Retain source documentation literal source_literal_144_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:148-163
  // Source: vvaharness/codegraph/tools.py:146-147
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool, _counted.
  // Source: vvaharness/codegraph/tools.py:148-163
  // Source signature: GraphContext(file: str, symbol: str, line: int | None=None) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphContext(file, symbol, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:149-150
    In source order: Retain source documentation literal source_literal_149_8; it is not a model call. Then Resolve source import from context_graph_sdk import ContextLimits; preserve alias and import-time effects.
    // Source: vvaharness/codegraph/tools.py:151-155
    Perform the following protected operations {
      // Source: vvaharness/codegraph/tools.py:152-153
      In source order: Evaluate once gtx.handle.graph.context(_selector(file, symbol, line), limits=ContextLimits(**_CONTEXT_LIMITS)); assign in source target order to res.
    }
    // Source: vvaharness/codegraph/tools.py:154-155
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/codegraph/tools.py:155-155
      End this invocation with _resolve_error(file, symbol, exc).
    }
    // Source: vvaharness/codegraph/tools.py:156-163
    End this invocation with {'symbol': _ref(res.symbol), 'callers': _refs(res.callers), 'callees': _refs(res.callees), 'imports': _refs(res.imports), 'implementors': _refs(res.implementors), 'call_paths': _paths(res.call_paths)}.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/codegraph/tools.py:165-165
  End this invocation with GraphContext.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:168-196
// Source signature: _impact_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _impact_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:169-169
  In source order: Retain source documentation literal source_literal_169_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:173-194
  // Source: vvaharness/codegraph/tools.py:171-172
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool, _counted.
  // Source: vvaharness/codegraph/tools.py:173-194
  // Source signature: GraphImpact(file: str, symbol: str, direction: str='upstream', line: int | None=None) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphImpact(file, symbol, direction, line) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:175-178
    In source order: Retain source documentation literal source_literal_175_8; it is not a model call. Then Resolve source import from context_graph_sdk import ImpactDirection, ImpactLimits; preserve alias and import-time effects. Then Evaluate once ImpactDirection.DOWNSTREAM if str(direction).lower().startswith('down') else ImpactDirection.UPSTREAM; assign in source target order to want.
    // Source: vvaharness/codegraph/tools.py:179-183
    Perform the following protected operations {
      // Source: vvaharness/codegraph/tools.py:180-181
      In source order: Evaluate once gtx.handle.graph.impact(_selector(file, symbol, line), want, limits=ImpactLimits(**_IMPACT_LIMITS)); assign in source target order to res.
    }
    // Source: vvaharness/codegraph/tools.py:182-183
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/codegraph/tools.py:183-183
      End this invocation with _resolve_error(file, symbol, exc).
    }
    // Source: vvaharness/codegraph/tools.py:184-184
    In source order: Evaluate once _refs(res.affected); assign in source target order to affected.
    // Source: vvaharness/codegraph/tools.py:185-194
    End this invocation with {'symbol': _ref(res.symbol), 'direction': want.value, 'affected': affected, 'reachable': bool(affected), 'note': 'nothing in the graph reaches this symbol — it is an entry point, dispatched by a framework, or unreachable' if not affected and want is ImpactDirection.UPSTREAM else '', 'paths': _paths(res.paths)}.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/codegraph/tools.py:196-196
  End this invocation with GraphImpact.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:199-223
// Source signature: _neighbors_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _neighbors_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:200-200
  In source order: Retain source documentation literal source_literal_200_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:204-221
  // Source: vvaharness/codegraph/tools.py:202-203
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool, _counted.
  // Source: vvaharness/codegraph/tools.py:204-221
  // Source signature: GraphNeighbors(file: str, function: str) -> dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphNeighbors(file, function) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:205-206
    In source order: Retain source documentation literal source_literal_205_8; it is not a model call. Then Evaluate once {'file': file, 'function': function}; assign in source target order to params.
    // Source: vvaharness/codegraph/tools.py:207-211
    Perform the following protected operations {
      // Source: vvaharness/codegraph/tools.py:208-209
      In source order: Evaluate once [_qname(r.to_dict()) for r in gtx.handle.graph.cypher(_NEIGHBORS_QUERY, params).rows]; assign in source target order to callees.
    }
    // Source: vvaharness/codegraph/tools.py:210-211
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/codegraph/tools.py:211-211
      End this invocation with _cypher_error(exc).
    }
    // Source: vvaharness/codegraph/tools.py:212-217
    Perform the following protected operations {
      // Source: vvaharness/codegraph/tools.py:213-214
      In source order: Evaluate once [_qname(r.to_dict()) for r in gtx.handle.graph.cypher(_CALLERS_QUERY, params).rows]; assign in source target order to callers.
    }
    // Source: vvaharness/codegraph/tools.py:215-217
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/codegraph/tools.py:217-217
      End this invocation with {'callees': [q for q in callees if q], **_cypher_error(exc)}.
    }
    // Source: vvaharness/codegraph/tools.py:218-221
    End this invocation with {'callees': [q for q in callees if q], 'callers': [q for q in callers if q]}.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/codegraph/tools.py:223-223
  End this invocation with GraphNeighbors.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:226-238
// Source signature: _community_of_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _community_of_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:227-227
  In source order: Retain source documentation literal source_literal_227_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:231-236
  // Source: vvaharness/codegraph/tools.py:229-230
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool, _counted.
  // Source: vvaharness/codegraph/tools.py:231-236
  // Source signature: GraphCommunityOf(file: str) -> str | None
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphCommunityOf(file) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:232-232
    In source order: Retain source documentation literal source_literal_232_8; it is not a model call.
    // Source: vvaharness/codegraph/tools.py:233-235
    for each (name, files) in _community_files(gtx.ctx).items() {
      // Source: vvaharness/codegraph/tools.py:234-235
      if (the source predicate file in files is truthy) {
        // Source: vvaharness/codegraph/tools.py:235-235
        End this invocation with name.
      }
    }
    // Source: vvaharness/codegraph/tools.py:236-236
    End this invocation with None.
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/codegraph/tools.py:238-238
  End this invocation with GraphCommunityOf.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:241-254
// Source signature: _importers_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _importers_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:242-242
  In source order: Retain source documentation literal source_literal_242_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:246-252
  // Source: vvaharness/codegraph/tools.py:244-245
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool, _counted.
  // Source: vvaharness/codegraph/tools.py:246-252
  // Source signature: GraphImporters(file: str) -> list[str] | dict
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphImporters(file) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:247-247
    In source order: Retain source documentation literal source_literal_247_8; it is not a model call.
    // Source: vvaharness/codegraph/tools.py:248-251
    Perform the following protected operations {
      // Source: vvaharness/codegraph/tools.py:249-249
      In source order: Evaluate once gtx.handle.graph.cypher(_IMPORTERS_QUERY, {'file': file}).rows; assign in source target order to rows.
    }
    // Source: vvaharness/codegraph/tools.py:250-251
    On the first matching source exception Exception as exc, in handler order {
      // Source: vvaharness/codegraph/tools.py:251-251
      End this invocation with _cypher_error(exc).
    }
    // Source: vvaharness/codegraph/tools.py:252-252
    End this invocation with [p for r in rows if isinstance((p := r.to_dict().get('path')), str)].
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/codegraph/tools.py:254-254
  End this invocation with GraphImporters.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:257-271
// Source signature: _sinks_in_community_tool(gtx: GraphToolContext) -> BaseTool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _sinks_in_community_tool(gtx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:258-258
  In source order: Retain source documentation literal source_literal_258_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:262-269
  // Source: vvaharness/codegraph/tools.py:260-261
  Before creating this callable, evaluate and retain decorators top-to-bottom: tool, _counted.
  // Source: vvaharness/codegraph/tools.py:262-269
  // Source signature: GraphSinksInCommunity(community: str) -> list[dict]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn GraphSinksInCommunity(community) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:263-264
    In source order: Retain source documentation literal source_literal_263_8; it is not a model call. Then Evaluate once set(_community_files(gtx.ctx).get(community, ())); assign in source target order to files.
    // Source: vvaharness/codegraph/tools.py:265-269
    End this invocation with [{'file': s.file, 'line': s.line, 'function': s.function} for s in getattr(gtx.ctx, 'unsafe_sinks', None) or () if s.file in files].
    If execution reaches this end, finish with the source implicit None result.
  }
  At definition time apply the retained decorators bottom-to-top to this callable; bind the resulting object to the source name.
  // Source: vvaharness/codegraph/tools.py:271-271
  End this invocation with GraphSinksInCommunity.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:274-289
In source order: Evaluate once Callable[[GraphToolContext], BaseTool]; assign in source target order to ToolFactory. Then For GRAPH_TOOLS, assign {'GraphContext': _context_tool, 'GraphImpact': _impact_tool, 'GraphNeighbors': _neighbors_tool, 'GraphCommunityOf': _community_of_tool, 'GraphImporters': _importers_tool, 'GraphSinksInCommunity': _sinks_in_community_tool}; source annotation dict[str, ToolFactory]. Then For GRAPH_TOOL_NAMES, assign tuple(GRAPH_TOOLS); source annotation tuple[str, ...]. Then For _PLUGIN_TOOLS, assign {}; source annotation dict[str, ToolFactory].
// Source: vvaharness/codegraph/tools.py:292-297
// Source signature: register_graph_tools(tools: Mapping[str, ToolFactory]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn register_graph_tools(tools) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:293-293
  In source order: Retain source documentation literal source_literal_293_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:294-297
  for each (name, build) in tools.items() {
    // Source: vvaharness/codegraph/tools.py:295-296
    if (the source predicate name in GRAPH_TOOLS or name in _PLUGIN_TOOLS is truthy) {
      // Source: vvaharness/codegraph/tools.py:296-296
      Raise ValueError(source_template_296_29).
    }
    // Source: vvaharness/codegraph/tools.py:297-297
    In source order: Evaluate once build; assign in source target order to _PLUGIN_TOOLS[name].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:300-302
// Source signature: clear_plugin_graph_tools() -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn clear_plugin_graph_tools() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:301-302
  In source order: Retain source documentation literal source_literal_301_4; it is not a model call. Then Evaluate _PLUGIN_TOOLS.clear(); retain side effects and discard the expression result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:305-307
// Source signature: graph_tool_names() -> tuple[str, ...]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn graph_tool_names() {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:306-306
  In source order: Retain source documentation literal source_literal_306_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:307-307
  End this invocation with GRAPH_TOOL_NAMES + tuple(_PLUGIN_TOOLS).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:310-317
// Source signature: _graph_tools(ctx: ContextPackage, allowed: set[str]) -> list[BaseTool]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _graph_tools(ctx, allowed) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:311-312
  In source order: Retain source documentation literal source_literal_311_4; it is not a model call. Then Evaluate once getattr(ctx, 'graph_handle', None); assign in source target order to handle.
  // Source: vvaharness/codegraph/tools.py:313-314
  if (the source predicate handle is None is truthy) {
    // Source: vvaharness/codegraph/tools.py:314-314
    End this invocation with [].
  }
  // Source: vvaharness/codegraph/tools.py:315-316
  In source order: Evaluate once GraphToolContext(handle=handle, ctx=ctx); assign in source target order to gtx. Then Evaluate once {**GRAPH_TOOLS, **_PLUGIN_TOOLS}; assign in source target order to registered.
  // Source: vvaharness/codegraph/tools.py:317-317
  End this invocation with [build(gtx) for name, build in registered.items() if name in allowed].
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:320-329
// Source signature: build_graph_tool_builder(ctx: ContextPackage) -> Callable[..., list[BaseTool]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_graph_tool_builder(ctx) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/codegraph/tools.py:321-321
  In source order: Retain source documentation literal source_literal_321_4; it is not a model call.
  // Source: vvaharness/codegraph/tools.py:323-327
  // Source signature: _build(options: StreamingOptions, *, allowed_tools: Sequence[str] | None) -> list[BaseTool]
  Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
  fn _build(options, allowed_tools) {
    Bind arguments/defaults/annotations exactly as the source signature specifies.
    // Source: vvaharness/codegraph/tools.py:325-326
    In source order: Retain source documentation literal source_literal_325_8; it is not a model call. Then Evaluate once build_reader_tools(options, allowed_tools=allowed_tools); assign in source target order to reader_tools.
    // Source: vvaharness/codegraph/tools.py:327-327
    End this invocation with reader_tools + _graph_tools(ctx, set(options.fact_tools)).
    If execution reaches this end, finish with the source implicit None result.
  }
  // Source: vvaharness/codegraph/tools.py:329-329
  End this invocation with _build.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/codegraph/tools.py:332-334
In source order: Evaluate once ['GRAPH_TOOLS', 'GRAPH_TOOL_NAMES', 'GraphToolContext', 'ToolFactory', 'build_graph_tool_builder', 'clear_plugin_graph_tools', 'graph_tool_names', 'register_graph_tools']; assign in source target order to __all__.
```

## Local import links

- `from context_graph_sdk import SymbolAmbiguousError, SymbolSelector` at source line 22: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/__init__.py.sudo.md`.
- `from vvaharness.backends.harness import StreamingOptions` at source line 25: `source_detail/vvaharness/backends/harness/__init__.py.sudo.md`.
- `from vvaharness.backends.harness.deepagents.tools import build_tools as build_reader_tools` at source line 26: `source_detail/vvaharness/backends/harness/deepagents/tools.py.sudo.md`.
- `from vvaharness.codegraph.handle import GraphHandle` at source line 29: `source_detail/vvaharness/codegraph/handle.py.sudo.md`.
- `from vvaharness.models import ContextPackage` at source line 30: `source_detail/vvaharness/models/__init__.py.sudo.md`.
- `from vvaharness.util.counters import COUNTERS` at source line 31: `source_detail/vvaharness/util/counters.py.sudo.md`.
- `from context_graph_sdk import ContextLimits` at source line 150: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/__init__.py.sudo.md`.
- `from context_graph_sdk import ImpactDirection, ImpactLimits` at source line 176: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/__init__.py.sudo.md`.

<!-- converted-model-instructions -->
Model behavior requested by this source: [converted instructions](../../../prompt_representation/vvaharness/codegraph/tools.py.sudo.md). Exact strings in the evidence asset support this conversion.
