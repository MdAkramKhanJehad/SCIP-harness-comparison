# vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py.evidence.json`. SHA-256: `e1aa6c2244d3e8e84b737b668939b0bc1580a5fdb47ba9baf39cf98a0124872f`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import import posixpath; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:23-34
In source order: Resolve source import from context_graph_sdk.analysis.inputs import AnalysisInputs, AnalysisNode; preserve alias and import-time effects. Then Resolve source import from context_graph_sdk.analysis.leiden import Adjacency, LeidenOptions, leiden, modularity; preserve alias and import-time effects. Then Evaluate once ('Function', 'Method', 'Class'); assign in source target order to CALLABLE_COMMUNITY_LABELS. Then Evaluate once frozenset({'structs', 'internal', 'util', 'utils', 'common', 'helper', 'helpers', 'lib', 'src', 'pkg', 'cmd', 'app', 'types', 'models', 'shared', 'core', 'base', 'misc', 'data', 'root'}); assign in source target order to _GENERIC_PACKAGE_NAMES.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:38-43
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:37-37
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:38-43
interface CommunityRecord {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:39-43
  In source order: For local_id, declare without assigning a value; source annotation str. Then For name, declare without assigning a value; source annotation str. Then For modularity, declare without assigning a value; source annotation float. Then For size, declare without assigning a value; source annotation int. Then For member_ids, declare without assigning a value; source annotation tuple[str, ...].
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:46-64
// Source signature: build_call_adjacency(inputs: AnalysisInputs) -> Adjacency
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn build_call_adjacency(inputs) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:47-48
  In source order: Retain source documentation literal source_literal_47_4; it is not a model call. Then For adjacency, assign {}; source annotation Adjacency.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:49-63
  for each (source_id, target_id, _, confidence) in inputs.edges {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:50-51
    In source order: Evaluate once inputs.nodes.get(source_id); assign in source target order to source. Then Evaluate once inputs.nodes.get(target_id); assign in source target order to target.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:52-53
    if (the source predicate source is None or target is None is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:53-53
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:54-58
    if (the source predicate source.label not in CALLABLE_COMMUNITY_LABELS or target.label not in CALLABLE_COMMUNITY_LABELS is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:58-58
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:59-63
    In source order: Evaluate once confidence if confidence > 0 else 1.0; assign in source target order to weight. Then Evaluate adjacency.setdefault(source.id, {}); retain side effects and discard the expression result. Then Evaluate adjacency.setdefault(target.id, {}); retain side effects and discard the expression result. Then Evaluate once adjacency[source.id].get(target.id, 0.0) + weight; assign in source target order to adjacency[source.id][target.id]. Then Evaluate once adjacency[target.id].get(source.id, 0.0) + weight; assign in source target order to adjacency[target.id][source.id].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:64-64
  End this invocation with adjacency.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:67-122
// Source signature: detect_communities(inputs: AnalysisInputs, options: LeidenOptions | None=None) -> list[CommunityRecord]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn detect_communities(inputs, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:71-71
  In source order: Evaluate once build_call_adjacency(inputs); assign in source target order to adjacency.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:72-73
  if (the source predicate not adjacency is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:73-73
    End this invocation with [].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:74-74
  In source order: Evaluate once leiden(adjacency, options); assign in source target order to result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:75-76
  if (the source predicate not result.membership is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:76-76
    End this invocation with [].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:78-81
  In source order: Evaluate once split_disconnected_communities(adjacency, result.membership); assign in source target order to membership. Then Evaluate once modularity(adjacency, membership); assign in source target order to overall_modularity. Then For groups, assign {}; source annotation dict[int, list[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:82-83
  for each (node_id, community) in membership.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:83-83
    In source order: Evaluate groups.setdefault(community, []).append(node_id); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:85-86
  In source order: For used_labels, assign {}; source annotation dict[str, int]. Then For records, assign []; source annotation list[CommunityRecord].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:87-121
  for each community_id in sorted(groups) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:88-89
    In source order: Evaluate once sorted(groups[community_id]); assign in source target order to members. Then Evaluate once _derive_name(inputs.nodes, members, community_id); assign in source target order to name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:90-111
    if (the source predicate used_labels.get(name, 0) > 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:91-91
      In source order: Evaluate once _derive_name(inputs.nodes, members, community_id, exclude=name); assign in source target order to alternative.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:92-111
      if (the source predicate alternative != name and used_labels.get(alternative, 0) == 0 is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:93-93
        In source order: Evaluate once alternative; assign in source target order to name.
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:95-95
        In source order: Evaluate once _dominant_symbol_name(inputs.nodes, members, community_id); assign in source target order to dominant.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:96-111
        if (the source predicate dominant != name and used_labels.get(dominant, 0) == 0 and (dominant != source_template_99_36) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:101-101
          In source order: Evaluate once dominant; assign in source target order to name.
        }
        else {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:103-111
          for each suffix in range(2, 100) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:104-104
            In source order: Evaluate once source_template_104_36; assign in source target order to candidate.
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:105-107
            if (the source predicate used_labels.get(candidate, 0) == 0 is truthy) {
              // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:106-106
              In source order: Evaluate once candidate; assign in source target order to name.
              // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:107-107
              Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
            }
          }
          Only on normal iterator exhaustion, with no break from this loop {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:111-111
            In source order: Evaluate once source_template_111_31; assign in source target order to name.
          }
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:112-121
    In source order: Evaluate once used_labels.get(name, 0) + 1; assign in source target order to used_labels[name]. Then Evaluate records.append(CommunityRecord(source_template_115_16, name, round(overall_modularity * 1000) / 1000, len(members), tuple(members))); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:122-122
  End this invocation with records.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:125-126
// Source signature: _is_generic(name: str) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _is_generic(name) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:126-126
  End this invocation with name.lower() in _GENERIC_PACKAGE_NAMES.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:129-137
// Source signature: _directory_counts(nodes: dict[str, AnalysisNode], member_ids: list[str]) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _directory_counts(nodes, member_ids) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:130-130
  In source order: For counts, assign {}; source annotation dict[str, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:131-136
  for each member_id in member_ids {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:132-132
    In source order: Evaluate once nodes.get(member_id); assign in source target order to symbol.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:133-134
    if (the source predicate symbol is None or not symbol.file_path is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:134-134
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:135-136
    In source order: Evaluate once posixpath.dirname(symbol.file_path).lstrip('./') or 'root'; assign in source target order to directory. Then Evaluate once counts.get(directory, 0) + 1; assign in source target order to counts[directory].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:137-137
  End this invocation with counts.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:140-237
// Source signature: _derive_name(nodes: dict[str, AnalysisNode], member_ids: list[str], community_id: int, exclude: str='') -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _derive_name(nodes, member_ids, community_id, exclude) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:146-146
  In source order: Evaluate once _directory_counts(nodes, member_ids); assign in source target order to directory_counts.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:147-148
  if (the source predicate not directory_counts is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:148-148
    End this invocation with source_template_148_15.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:150-152
  In source order: Evaluate once sorted(directory_counts); assign in source target order to directories. Then Evaluate once ''; assign in source target order to best_dir. Then Evaluate once 0; assign in source target order to best_count.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:153-158
  for each directory in directories {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:154-155
    if (the source predicate _is_generic(posixpath.basename(directory)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:155-155
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:156-158
    if (the source predicate directory_counts[directory] > best_count is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:157-158
      In source order: Evaluate once directory_counts[directory]; assign in source target order to best_count. Then Evaluate once directory; assign in source target order to best_dir.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:159-163
  if (the source predicate not best_dir is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:160-163
    for each directory in directories {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:161-163
      if (the source predicate directory_counts[directory] > best_count is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:162-163
        In source order: Evaluate once directory_counts[directory]; assign in source target order to best_count. Then Evaluate once directory; assign in source target order to best_dir.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:165-166
  In source order: Evaluate once posixpath.basename(best_dir); assign in source target order to base. Then Evaluate once '/' not in best_dir and best_dir != 'root'; assign in source target order to is_shallow_root.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:168-209
  if (the source predicate is_shallow_root is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:169-169
    In source order: For sub_counts, assign {}; source annotation dict[str, int].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:170-174
    for each (directory, count) in directory_counts.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:171-174
      if (the source predicate directory.startswith(best_dir + '/') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:172-172
        In source order: Evaluate once directory.removeprefix(best_dir + '/').split('/', 1)[0]; assign in source target order to sub.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:173-174
        if (the source predicate not _is_generic(sub) is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:174-174
          In source order: Evaluate once sub_counts.get(sub, 0) + count; assign in source target order to sub_counts[sub].
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:175-179
    if (the source predicate not sub_counts is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:176-179
      for each (directory, count) in directory_counts.items() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:177-179
        if (the source predicate directory.startswith(best_dir + '/') is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:178-179
          In source order: Evaluate once directory.removeprefix(best_dir + '/').split('/', 1)[0]; assign in source target order to sub. Then Evaluate once sub_counts.get(sub, 0) + count; assign in source target order to sub_counts[sub].
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:180-205
    if (the source predicate sub_counts is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:181-182
      In source order: Evaluate once sorted(sub_counts); assign in source target order to subs. Then Evaluate once ('', 0); assign in source target order to (best_sub, best_sub_count).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:183-188
      for each sub in subs {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:184-185
        if (the source predicate sub == exclude is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:185-185
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:186-188
        if (the source predicate sub_counts[sub] > best_sub_count is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:187-188
          In source order: Evaluate once sub_counts[sub]; assign in source target order to best_sub_count. Then Evaluate once sub; assign in source target order to best_sub.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:189-193
      if (the source predicate not best_sub is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:190-193
        for each sub in subs {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:191-193
          if (the source predicate sub_counts[sub] > best_sub_count is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:192-193
            In source order: Evaluate once sub_counts[sub]; assign in source target order to best_sub_count. Then Evaluate once sub; assign in source target order to best_sub.
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:194-194
      In source order: Evaluate once ('', 0); assign in source target order to (second_sub, second_count).
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:195-200
      for each sub in subs {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:196-197
        if (the source predicate sub == best_sub is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:197-197
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:198-200
        if (the source predicate sub_counts[sub] > second_count is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:199-200
          In source order: Evaluate once sub_counts[sub]; assign in source target order to second_count. Then Evaluate once sub; assign in source target order to second_sub.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:201-201
      In source order: Evaluate once best_sub; assign in source target order to candidate.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:202-203
      if (the source predicate second_sub and second_count * 2 >= best_sub_count is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:203-203
        In source order: Evaluate once best_sub + '+' + second_sub; assign in source target order to candidate.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:204-205
      if (the source predicate candidate != exclude is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:205-205
        End this invocation with candidate.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:206-206
    In source order: Evaluate once _dominant_symbol_name(nodes, member_ids, community_id); assign in source target order to name.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:207-208
    if (the source predicate name != exclude is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:208-208
      End this invocation with name.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:209-209
    End this invocation with source_template_209_15.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:211-214
  if (the source predicate _is_generic(base) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:212-212
    In source order: Evaluate once posixpath.dirname(best_dir); assign in source target order to parent.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:213-214
    if (the source predicate parent not in ('.', '/', '') is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:214-214
      In source order: Evaluate once posixpath.basename(parent) + '/' + base; assign in source target order to base.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:216-217
  if (the source predicate best_count * 2 >= len(member_ids) and base != exclude is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:217-217
    End this invocation with base.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:219-219
  In source order: Evaluate once ('', 0); assign in source target order to (second_dir, second_count).
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:220-225
  for each directory in directories {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:221-222
    if (the source predicate directory == best_dir is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:222-222
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:223-225
    if (the source predicate directory_counts[directory] > second_count is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:224-225
      In source order: Evaluate once directory_counts[directory]; assign in source target order to second_count. Then Evaluate once directory; assign in source target order to second_dir.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:226-234
  if (the source predicate second_dir is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:227-227
    In source order: Evaluate once posixpath.basename(second_dir); assign in source target order to second_base.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:228-231
    if (the source predicate _is_generic(second_base) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:229-229
      In source order: Evaluate once posixpath.dirname(second_dir); assign in source target order to parent.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:230-231
      if (the source predicate parent not in ('.', '/', '') is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:231-231
        In source order: Evaluate once posixpath.basename(parent) + '/' + second_base; assign in source target order to second_base.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:232-232
    In source order: Evaluate once base + '+' + second_base; assign in source target order to candidate.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:233-234
    if (the source predicate candidate != exclude is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:234-234
      End this invocation with candidate.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:235-236
  if (the source predicate base != exclude is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:236-236
    End this invocation with base.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:237-237
  End this invocation with _dominant_symbol_name(nodes, member_ids, community_id).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:240-266
// Source signature: _dominant_symbol_name(nodes: dict[str, AnalysisNode], member_ids: list[str], community_id: int) -> str
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _dominant_symbol_name(nodes, member_ids, community_id) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:243-243
  In source order: For name_counts, assign {}; source annotation dict[str, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:244-248
  for each member_id in member_ids {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:245-245
    In source order: Evaluate once nodes.get(member_id); assign in source target order to symbol.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:246-247
    if (the source predicate symbol is None or not symbol.name or (not symbol.is_exported) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:247-247
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:248-248
    In source order: Evaluate once name_counts.get(symbol.name, 0) + 1; assign in source target order to name_counts[symbol.name].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:249-250
  if (the source predicate not name_counts is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:250-250
    End this invocation with source_template_250_15.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:251-252
  In source order: Evaluate once sorted(name_counts); assign in source target order to names. Then Evaluate once ('', 0); assign in source target order to (best_name, best_count).
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:253-256
  for each name in names {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:254-256
    if (the source predicate name_counts[name] > best_count is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:255-256
      In source order: Evaluate once name_counts[name]; assign in source target order to best_count. Then Evaluate once name; assign in source target order to best_name.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:257-257
  In source order: Evaluate once ('', 0); assign in source target order to (second_name, second_count).
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:258-263
  for each name in names {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:259-260
    if (the source predicate name == best_name is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:260-260
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:261-263
    if (the source predicate name_counts[name] > second_count is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:262-263
      In source order: Evaluate once name_counts[name]; assign in source target order to second_count. Then Evaluate once name; assign in source target order to second_name.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:264-265
  if (the source predicate second_name and second_count * 2 >= best_count is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:265-265
    End this invocation with best_name + '+' + second_name.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:266-266
  End this invocation with best_name or source_template_266_24.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:269-282
// Source signature: is_connected(adjacency: Adjacency, members: list[str]) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn is_connected(adjacency, members) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:270-270
  In source order: Retain source documentation literal source_literal_270_4; it is not a model call.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:271-272
  if (the source predicate not members is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:272-272
    End this invocation with True.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:273-275
  In source order: Evaluate once set(members); assign in source target order to member_set. Then Evaluate once [members[0]]; assign in source target order to stack. Then Evaluate once {members[0]}; assign in source target order to seen.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:276-281
  while (the source predicate stack is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:277-277
    In source order: Evaluate once stack.pop(); assign in source target order to node.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:278-281
    for each neighbor in adjacency.get(node, {}) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:279-281
      if (the source predicate neighbor in member_set and neighbor not in seen is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:280-281
        In source order: Evaluate seen.add(neighbor); retain side effects and discard the expression result. Then Evaluate stack.append(neighbor); retain side effects and discard the expression result.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:282-282
  End this invocation with len(seen) == len(member_set).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:285-316
// Source signature: split_disconnected_communities(adjacency: Adjacency, membership: dict[str, int]) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn split_disconnected_communities(adjacency, membership) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:288-290
  In source order: Retain source documentation literal source_literal_288_4; it is not a model call. Then For groups, assign {}; source annotation dict[int, list[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:291-292
  for each (node, community) in membership.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:292-292
    In source order: Evaluate groups.setdefault(community, []).append(node); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:293-294
  In source order: Evaluate once max(groups, default=-1) + 1; assign in source target order to next_id. Then Evaluate once dict(membership); assign in source target order to result.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:295-315
  for each community in sorted(groups) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:296-298
    In source order: Evaluate once sorted(groups[community]); assign in source target order to members. Then Evaluate once set(members); assign in source target order to remaining. Then Evaluate once True; assign in source target order to first_component.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:299-315
    while (the source predicate remaining is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:300-302
      In source order: Evaluate once min(remaining); assign in source target order to start. Then Evaluate once {start}; assign in source target order to component. Then Evaluate once [start]; assign in source target order to stack.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:303-308
      while (the source predicate stack is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:304-304
        In source order: Evaluate once stack.pop(); assign in source target order to node.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:305-308
        for each neighbor in adjacency.get(node, {}) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:306-308
          if (the source predicate neighbor in remaining and neighbor not in component is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:307-308
            In source order: Evaluate component.add(neighbor); retain side effects and discard the expression result. Then Evaluate stack.append(neighbor); retain side effects and discard the expression result.
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:309-309
      In source order: Apply source augmented assignment remaining -= component with source evaluation/in-place semantics.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:310-312
      if (the source predicate first_component is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:311-311
        In source order: Evaluate once False; assign in source target order to first_component.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:312-312
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:313-314
      for each node in sorted(component) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:314-314
        In source order: Evaluate once next_id; assign in source target order to result[node].
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:315-315
      In source order: Apply source augmented assignment next_id += 1 with source evaluation/in-place semantics.
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:316-316
  End this invocation with result.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:319-320
// Source signature: community_quality_is_finite(value: float) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn community_quality_is_finite(value) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/communities.py:320-320
  End this invocation with not math.isnan(value) and (not math.isinf(value)).
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from context_graph_sdk.analysis.inputs import AnalysisInputs, AnalysisNode` at source line 23: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/inputs.py.sudo.md`.
- `from context_graph_sdk.analysis.leiden import Adjacency, LeidenOptions, leiden, modularity` at source line 24: `source_detail/vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py.sudo.md`.
