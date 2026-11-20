# vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py.evidence.json`. SHA-256: `5cae3bff3aaed8d76e0604635ff800eafa0328667a6d339effe9cadb3eed98ca`.

```sudo
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:15-25
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import math; preserve alias and import-time effects. Then Resolve source import import random; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass, field; preserve alias and import-time effects.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:26-31
In source order: Resolve source import from enum import Enum; preserve alias and import-time effects. Then Evaluate once dict[str, dict[str, float]]; assign in source target order to Adjacency. Then Evaluate once 20; assign in source target order to _MAX_LEVELS. Then Evaluate once 100; assign in source target order to _CONVERGENCE_CAP.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:34-37
interface Objective {
  Describe the source Python type, preserving its base/metaclass expression order: Enum.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:35-37
  In source order: Evaluate once 'modularity'; assign in source target order to MODULARITY. Then Evaluate once 'cpm'; assign in source target order to CPM. Then Evaluate once 'erdos-renyi'; assign in source target order to ERDOS_RENYI.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:41-58
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:40-40
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:41-58
interface LeidenOptions {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:42-54
  In source order: Retain source documentation literal source_literal_42_4; it is not a model call. Then For objective, assign Objective.MODULARITY; source annotation Objective. Then For resolution, assign None; source annotation float | None. Then For beta, assign None; source annotation float | None. Then For seed, assign 42; source annotation int.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:57-58
  In source order: For max_iterations, assign 2; source annotation int. Then For start_partition, assign None; source annotation dict[str, int] | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:62-65
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:61-61
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:62-65
interface LeidenResult {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:63-65
  In source order: For membership, assign field(default_factory=dict[str, int]); source annotation dict[str, int]. Then For cluster_count, assign 0; source annotation int. Then For quality, assign math.nan; source annotation float.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:68-77
// Source signature: validate_adjacency(adjacency: Adjacency, objective: Objective) -> str | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn validate_adjacency(adjacency, objective) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:69-76
  for each (source, neighbors) in adjacency.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:70-76
    for each (target, weight) in neighbors.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:71-72
      if (the source predicate math.isnan(weight) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:72-72
        End this invocation with source_template_72_23.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:73-74
      if (the source predicate math.isinf(weight) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:74-74
        End this invocation with source_template_74_23.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:75-76
      if (the source predicate weight < 0 and objective is not Objective.CPM is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:76-76
        End this invocation with source_template_76_23.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:77-77
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:80-90
// Source signature: _effective_resolution(options: LeidenOptions, total_weight: float, node_count: int) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _effective_resolution(options, total_weight, node_count) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:81-81
  In source order: Evaluate once options.resolution; assign in source target order to resolution.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:82-83
  if (the source predicate options.objective is Objective.CPM is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:83-83
    End this invocation with 1.0 if resolution is None else resolution.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:84-89
  if (the source predicate options.objective is Objective.ERDOS_RENYI is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:85-85
    In source order: Evaluate once 1.0 if resolution is None else resolution; assign in source target order to resolution.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:86-88
    if (the source predicate node_count > 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:87-88
      In source order: Evaluate once node_count * (node_count + 1) / 2.0; assign in source target order to pairs. Then Apply source augmented assignment resolution *= total_weight / pairs with source evaluation/in-place semantics.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:89-89
    End this invocation with resolution.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:90-90
  End this invocation with 1.0 / (2 * total_weight) if resolution is None else resolution.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:93-98
// Source signature: _node_weights(adjacency: Adjacency, nodes: list[str], options: LeidenOptions) -> dict[str, float]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _node_weights(adjacency, nodes, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:96-97
  if (the source predicate options.objective in (Objective.CPM, Objective.ERDOS_RENYI) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:97-97
    End this invocation with dict.fromkeys(nodes, 1.0).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:98-98
  End this invocation with {node: sum(adjacency[node].values()) for node in nodes}.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:101-187
// Source signature: leiden(adjacency: Adjacency, options: LeidenOptions | None=None) -> LeidenResult
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn leiden(adjacency, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:102-102
  In source order: Evaluate once options or LeidenOptions(); assign in source target order to options.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:103-104
  if (the source predicate not adjacency is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:104-104
    End this invocation with LeidenResult().
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:106-108
  if (the source predicate validate_adjacency(adjacency, options.objective) is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:107-107
    In source order: Evaluate once sorted(adjacency); assign in source target order to nodes.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:108-108
    End this invocation with LeidenResult({node: i for i, node in enumerate(nodes)}, len(nodes), math.nan).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:110-111
  In source order: Evaluate once sorted(adjacency); assign in source target order to nodes. Then Evaluate once sum((sum(neighbors.values()) for neighbors in adjacency.values())) / 2; assign in source target order to total_weight.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:112-113
  if (the source predicate total_weight == 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:113-113
    End this invocation with LeidenResult({node: i for i, node in enumerate(nodes)}, len(nodes), math.nan).
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:115-119
  In source order: Evaluate once _effective_resolution(options, total_weight, len(nodes)); assign in source target order to resolution. Then Evaluate once 0.01 if options.beta is None else options.beta; assign in source target order to beta. Then Evaluate once _node_weights(adjacency, nodes, options); assign in source target order to node_weight. Then For membership, declare without assigning a value; source annotation dict[str, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:120-130
  if (the source predicate options.start_partition is not None is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:121-122
    In source order: Evaluate once max(options.start_partition.values(), default=-1) + 1; assign in source target order to next_id. Then Evaluate once {}; assign in source target order to membership.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:123-128
    for each node in nodes {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:124-128
      if (the source predicate node in options.start_partition is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:125-125
        In source order: Evaluate once options.start_partition[node]; assign in source target order to membership[node].
      }
      else {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:127-128
        In source order: Evaluate once next_id; assign in source target order to membership[node]. Then Apply source augmented assignment next_id += 1 with source evaluation/in-place semantics.
      }
    }
  }
  else {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:130-130
    In source order: Evaluate once {node: i for i, node in enumerate(nodes)}; assign in source target order to membership.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:132-137
  In source order: Evaluate once random.Random(options.seed); assign in source target order to rng. Then Evaluate once options.max_iterations; assign in source target order to iterations. Then Evaluate once iterations < 0; assign in source target order to run_until_convergence.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:138-139
  if (the source predicate run_until_convergence is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:139-139
    In source order: Evaluate once _CONVERGENCE_CAP; assign in source target order to iterations.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:141-141
  In source order: Evaluate once membership; assign in source target order to current_membership.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:142-176
  for each _ in range(iterations) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:143-147
    In source order: Evaluate once adjacency; assign in source target order to level_adj. Then Evaluate once nodes; assign in source target order to level_nodes. Then Evaluate once node_weight; assign in source target order to level_weight. Then Evaluate once current_membership; assign in source target order to level_membership. Then For node_to_original, assign {node: [node] for node in nodes}; source annotation dict[str, list[str]].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:148-148
    In source order: Evaluate once False; assign in source target order to any_changed.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:150-168
    for each _ in range(_MAX_LEVELS) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:151-153
      In source order: Evaluate once _fast_move(level_adj, level_nodes, level_weight, level_membership, resolution, rng); assign in source target order to changed.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:154-155
      if (the source predicate not changed is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:155-155
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:156-160
      In source order: Evaluate once True; assign in source target order to any_changed. Then Evaluate _reindex(level_nodes, level_membership); retain side effects and discard the expression result. Then Evaluate once _refine(level_adj, level_nodes, level_weight, level_membership, resolution, beta, rng); assign in source target order to refined.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:161-162
      if (the source predicate len({refined[node] for node in level_nodes}) >= len(level_nodes) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:162-162
        In source order: Evaluate once {node: level_membership[node] for node in level_nodes}; assign in source target order to refined.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:163-165
      In source order: Evaluate once _aggregate(level_adj, level_nodes, level_weight, level_membership, refined, node_to_original); assign in source target order to aggregated.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:166-167
      if (the source predicate len(aggregated[1]) >= len(level_nodes) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:167-167
        Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:168-168
      In source order: Evaluate once aggregated; assign in source target order to (level_adj, level_nodes, level_weight, level_membership, node_to_original).
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:170-171
    if (the source predicate run_until_convergence and (not any_changed) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:171-171
      Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:173-173
    In source order: Evaluate once {}; assign in source target order to current_membership.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:174-176
    for each (super_node, community) in level_membership.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:175-176
      for each original in node_to_original[super_node] {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:176-176
        In source order: Evaluate once community; assign in source target order to current_membership[original].
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:178-178
  In source order: For remap, assign {}; source annotation dict[int, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:179-183
  for each node in nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:180-180
    In source order: Evaluate once current_membership[node]; assign in source target order to community.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:181-182
    if (the source predicate community not in remap is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:182-182
      In source order: Evaluate once len(remap); assign in source target order to remap[community].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:183-183
    In source order: Evaluate once remap[community]; assign in source target order to current_membership[node].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:185-187
  End this invocation with LeidenResult(current_membership, len(remap), quality(adjacency, current_membership, options)).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:190-279
// Source signature: _fast_move(adjacency: Adjacency, nodes: list[str], node_weight: dict[str, float], membership: dict[str, int], resolution: float, rng: random.Random) -> bool
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _fast_move(adjacency, nodes, node_weight, membership, resolution, rng) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:198-199
  In source order: For sigma_tot, assign {}; source annotation dict[int, float]. Then For community_size, assign {}; source annotation dict[int, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:200-203
  for each node in nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:201-203
    In source order: Evaluate once membership[node]; assign in source target order to community. Then Evaluate once sigma_tot.get(community, 0.0) + node_weight[node]; assign in source target order to sigma_tot[community]. Then Evaluate once community_size.get(community, 0) + 1; assign in source target order to community_size[community].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:205-210
  In source order: Evaluate once max((membership[node] for node in nodes), default=-1) + 1; assign in source target order to next_cluster. Then Evaluate once [c for c in range(next_cluster) if community_size.get(c, 0) == 0]; assign in source target order to empty_stack. Then Evaluate once list(nodes); assign in source target order to shuffled. Then Evaluate rng.shuffle(shuffled); retain side effects and discard the expression result. Then Evaluate once list(shuffled); assign in source target order to queue.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:211-213
  In source order: Evaluate once dict.fromkeys(shuffled, True); assign in source target order to in_queue. Then Evaluate once 0; assign in source target order to head. Then Evaluate once False; assign in source target order to any_moved.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:215-277
  while (the source predicate head < len(queue) is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:216-221
    In source order: Evaluate once queue[head]; assign in source target order to node. Then Apply source augmented assignment head += 1 with source evaluation/in-place semantics. Then Evaluate once False; assign in source target order to in_queue[node]. Then Evaluate once membership[node]; assign in source target order to old_community. Then Evaluate once node_weight[node]; assign in source target order to degree.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:223-223
    In source order: For neighbor_weight, assign {}; source annotation dict[int, float].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:224-228
    for each (neighbor, weight) in adjacency[node].items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:225-226
      if (the source predicate neighbor == node is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:226-226
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:227-228
      In source order: Evaluate once membership[neighbor]; assign in source target order to community. Then Evaluate once neighbor_weight.get(community, 0.0) + weight; assign in source target order to neighbor_weight[community].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:230-231
    In source order: Apply source augmented assignment sigma_tot[old_community] -= degree with source evaluation/in-place semantics. Then Apply source augmented assignment community_size[old_community] -= 1 with source evaluation/in-place semantics.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:232-233
    if (the source predicate community_size[old_community] == 0 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:233-233
      In source order: Evaluate empty_stack.append(old_community); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:235-240
    In source order: Evaluate once empty_stack[-1] if empty_stack else -1; assign in source target order to empty_community. Then Evaluate once old_community; assign in source target order to best_community. Then Evaluate once neighbor_weight.get(old_community, 0.0) - degree * sigma_tot[old_community] * resolution; assign in source target order to best_diff.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:241-243
    if (the source predicate empty_community >= 0 and empty_community != old_community and (best_diff < 0.0) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:242-243
      In source order: Evaluate once 0.0; assign in source target order to best_diff. Then Evaluate once empty_community; assign in source target order to best_community.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:245-249
    for each community in sorted((c for c in neighbor_weight if c != old_community)) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:246-246
      In source order: Evaluate once neighbor_weight[community] - degree * sigma_tot.get(community, 0.0) * resolution; assign in source target order to diff.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:247-249
      if (the source predicate diff > best_diff is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:248-249
        In source order: Evaluate once diff; assign in source target order to best_diff. Then Evaluate once community; assign in source target order to best_community.
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:251-253
    In source order: Evaluate once best_community; assign in source target order to membership[node]. Then Evaluate once sigma_tot.get(best_community, 0.0) + degree; assign in source target order to sigma_tot[best_community]. Then Evaluate once community_size.get(best_community, 0) + 1; assign in source target order to community_size[best_community].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:255-266
    if (the source predicate best_community == old_community and community_size[old_community] == 1 and empty_stack and (empty_stack[-1] == old_community) or (best_community == empty_community and best_community != old_community and empty_stack and (empty_stack[-1] == empty_community)) is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:266-266
      In source order: Evaluate empty_stack.pop(); retain side effects and discard the expression result.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:268-277
    if (the source predicate best_community != old_community is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:269-274
      In source order: Evaluate once True; assign in source target order to any_moved. Then Evaluate once sorted((neighbor for neighbor in adjacency[node] if membership.get(neighbor) != best_community and (not in_queue.get(neighbor, False)))); assign in source target order to to_enqueue.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:275-277
      for each neighbor in to_enqueue {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:276-277
        In source order: Evaluate queue.append(neighbor); retain side effects and discard the expression result. Then Evaluate once True; assign in source target order to in_queue[neighbor].
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:279-279
  End this invocation with any_moved.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:282-377
// Source signature: _refine(adjacency: Adjacency, nodes: list[str], node_weight: dict[str, float], membership: dict[str, int], resolution: float, beta: float, rng: random.Random) -> dict[str, int]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _refine(adjacency, nodes, node_weight, membership, resolution, beta, rng) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:291-292
  In source order: Evaluate once {node: index for index, node in enumerate(nodes)}; assign in source target order to refined. Then For clusters, assign {}; source annotation dict[int, list[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:293-294
  for each node in nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:294-294
    In source order: Evaluate clusters.setdefault(membership[node], []).append(node); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:296-298
  In source order: Evaluate once {refined[node]: node_weight[node] for node in nodes}; assign in source target order to refined_sigma. Then Evaluate once {c: sum((node_weight[n] for n in members)) for c, members in clusters.items()}; assign in source target order to cluster_total. Then For non_singleton, assign set(); source annotation set[int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:300-375
  for each cluster_id in sorted(clusters) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:301-301
    In source order: Evaluate once clusters[cluster_id]; assign in source target order to members.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:302-303
    if (the source predicate len(members) <= 1 is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:303-303
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:304-306
    In source order: Evaluate once cluster_total[cluster_id]; assign in source target order to total_cluster_weight. Then For ext_edge_weight, assign {}; source annotation dict[int, float].
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:307-316
    for each vertex in members {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:308-308
      In source order: Evaluate once refined[vertex]; assign in source target order to refined_community.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:309-316
      for each (neighbor, weight) in adjacency[vertex].items() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:310-316
        if (the source predicate membership.get(neighbor) == cluster_id and refined[neighbor] != refined_community is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:314-316
          In source order: Evaluate once ext_edge_weight.get(refined_community, 0.0) + weight; assign in source target order to ext_edge_weight[refined_community].
        }
      }
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:318-319
    In source order: Evaluate once list(members); assign in source target order to shuffled. Then Evaluate rng.shuffle(shuffled); retain side effects and discard the expression result.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:321-375
    for each vertex in shuffled {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:322-323
      In source order: Evaluate once refined[vertex]; assign in source target order to current. Then Evaluate once node_weight[vertex]; assign in source target order to degree.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:324-325
      if (the source predicate current in non_singleton is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:325-325
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:326-329
      if (the source predicate ext_edge_weight.get(current, 0.0) < resolution * degree * (total_cluster_weight - degree) is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:329-329
        Continue the immediately enclosing source loop at its next iteration.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:331-333
      In source order: Apply source augmented assignment refined_sigma[current] -= degree with source evaluation/in-place semantics. Then For neighbor_refined, assign {}; source annotation dict[int, float].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:334-337
      for each (neighbor, weight) in adjacency[vertex].items() {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:335-337
        if (the source predicate membership.get(neighbor) == cluster_id is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:336-337
          In source order: Evaluate once refined[neighbor]; assign in source target order to community. Then Evaluate once neighbor_refined.get(community, 0.0) + weight; assign in source target order to neighbor_refined[community].
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:339-339
      In source order: For candidates, assign [(current, 0.0)]; source annotation list[tuple[int, float]].
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:340-349
      for each community in sorted(neighbor_refined) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:341-342
        if (the source predicate community == current is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:342-342
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:343-344
        In source order: Evaluate once refined_sigma.get(community, 0.0); assign in source target order to target_weight. Then Evaluate once target_weight * (total_cluster_weight - target_weight); assign in source target order to well_connected.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:345-346
        if (the source predicate ext_edge_weight.get(community, 0.0) < well_connected * resolution is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:346-346
          Continue the immediately enclosing source loop at its next iteration.
        }
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:347-347
        In source order: Evaluate once neighbor_refined[community] - degree * target_weight * resolution; assign in source target order to diff.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:348-349
        if (the source predicate diff >= 0 is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:349-349
          In source order: Evaluate candidates.append((community, diff)); retain side effects and discard the expression result.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:351-353
      In source order: Evaluate once max((diff for _, diff in candidates)); assign in source target order to max_diff. Then For cumulative, assign []; source annotation list[float]. Then Evaluate once 0.0; assign in source target order to running.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:354-356
      for each (_, diff) in candidates {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:355-356
        In source order: Apply source augmented assignment running += math.exp((diff - max_diff) / beta) with source evaluation/in-place semantics. Then Evaluate cumulative.append(running); retain side effects and discard the expression result.
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:357-358
      In source order: Evaluate once rng.random() * running; assign in source target order to draw. Then Evaluate once 0; assign in source target order to chosen_index.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:359-362
      for each (index, bound) in enumerate(cumulative) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:360-362
        if (the source predicate draw <= bound is truthy) {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:361-361
          In source order: Evaluate once index; assign in source target order to chosen_index.
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:362-362
          Leave the immediately enclosing source loop, skipping its normal-exhaustion body.
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:363-363
      In source order: Evaluate once candidates[chosen_index][0]; assign in source target order to chosen.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:365-374
      if (the source predicate chosen != current is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:366-367
        In source order: Evaluate once chosen; assign in source target order to refined[vertex]. Then Evaluate non_singleton.add(chosen); retain side effects and discard the expression result.
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:368-374
        for each (neighbor, weight) in adjacency[vertex].items() {
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:369-370
          if (the source predicate membership.get(neighbor) != cluster_id is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:370-370
            Continue the immediately enclosing source loop at its next iteration.
          }
          // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:371-374
          if (the source predicate refined[neighbor] == chosen is truthy) {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:372-372
            In source order: Evaluate once ext_edge_weight.get(chosen, 0.0) - weight; assign in source target order to ext_edge_weight[chosen].
          }
          else {
            // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:374-374
            In source order: Evaluate once ext_edge_weight.get(chosen, 0.0) + weight; assign in source target order to ext_edge_weight[chosen].
          }
        }
      }
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:375-375
      In source order: Evaluate once refined_sigma.get(chosen, 0.0) + degree; assign in source target order to refined_sigma[chosen].
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:377-377
  End this invocation with refined.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:380-422
// Source signature: _aggregate(adjacency: Adjacency, nodes: list[str], node_weight: dict[str, float], membership: dict[str, int], refined: dict[str, int], node_to_original: dict[str, list[str]]) -> tuple[Adjacency, list[str], dict[str, float], dict[str, int], dict[str, list[str]]]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _aggregate(adjacency, nodes, node_weight, membership, refined, node_to_original) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:388-388
  In source order: For members_by_refined, assign {}; source annotation dict[int, list[str]].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:389-390
  for each node in nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:390-390
    In source order: Evaluate members_by_refined.setdefault(refined[node], []).append(node); retain side effects and discard the expression result.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:391-394
  In source order: Evaluate once sorted(members_by_refined); assign in source target order to refined_ids. Then Evaluate once {c: source_template_392_21 for c in refined_ids}; assign in source target order to super_name. Then For new_adjacency, assign {super_name[c]: {} for c in refined_ids}; source annotation Adjacency.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:395-400
  for each node in nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:396-396
    In source order: Evaluate once super_name[refined[node]]; assign in source target order to source.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:397-400
    for each (neighbor, weight) in adjacency[node].items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:398-398
      In source order: Evaluate once super_name[refined[neighbor]]; assign in source target order to target.
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:399-400
      if (the source predicate source <= target is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:400-400
        In source order: Evaluate once new_adjacency[source].get(target, 0.0) + weight; assign in source target order to new_adjacency[source][target].
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:401-404
  for each (source, neighbors) in list(new_adjacency.items()) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:402-404
    for each (target, weight) in list(neighbors.items()) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:403-404
      if (the source predicate source != target is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:404-404
        In source order: Evaluate once weight; assign in source target order to new_adjacency[target][source].
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:406-415
  In source order: Evaluate once {super_name[c]: sum((node_weight[m] for m in members_by_refined[c])) for c in refined_ids}; assign in source target order to new_weight. Then Evaluate once {super_name[c]: membership[members_by_refined[c][0]] for c in refined_ids}; assign in source target order to new_membership. Then Evaluate once {super_name[c]: [original for member in members_by_refined[c] for original in node_to_original[member]] for c in refined_ids}; assign in source target order to new_node_to_original.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:416-422
  End this invocation with (new_adjacency, [super_name[c] for c in refined_ids], new_weight, new_membership, new_node_to_original).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:425-431
// Source signature: _reindex(nodes: list[str], membership: dict[str, int]) -> None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _reindex(nodes, membership) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:426-426
  In source order: For remap, assign {}; source annotation dict[int, int].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:427-431
  for each node in nodes {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:428-428
    In source order: Evaluate once membership[node]; assign in source target order to community.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:429-430
    if (the source predicate community not in remap is truthy) {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:430-430
      In source order: Evaluate once len(remap); assign in source target order to remap[community].
    }
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:431-431
    In source order: Evaluate once remap[community]; assign in source target order to membership[node].
  }
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:434-458
// Source signature: quality(adjacency: Adjacency, communities: dict[str, int], options: LeidenOptions | None=None) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn quality(adjacency, communities, options) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:437-437
  In source order: Evaluate once options or LeidenOptions(); assign in source target order to options.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:438-439
  if (the source predicate not adjacency is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:439-439
    End this invocation with 0.0.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:440-440
  In source order: Evaluate once sum((sum(neighbors.values()) for neighbors in adjacency.values())) / 2; assign in source target order to total_weight.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:441-442
  if (the source predicate total_weight == 0 is truthy) {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:442-442
    End this invocation with math.nan.
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:443-446
  In source order: Evaluate once _effective_resolution(options, total_weight, len(adjacency)); assign in source target order to resolution. Then Evaluate once _node_weights(adjacency, sorted(adjacency), options); assign in source target order to node_weight. Then Evaluate once 0.0; assign in source target order to internal.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:447-451
  for each (source, neighbors) in adjacency.items() {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:448-448
    In source order: Evaluate once communities[source]; assign in source target order to source_community.
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:449-451
    for each (target, weight) in neighbors.items() {
      // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:450-451
      if (the source predicate communities[target] == source_community is truthy) {
        // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:451-451
        In source order: Apply source augmented assignment internal += weight with source evaluation/in-place semantics.
      }
    }
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:453-453
  In source order: For cluster_weight, assign {}; source annotation dict[int, float].
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:454-456
  for each node in adjacency {
    // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:455-456
    In source order: Evaluate once communities[node]; assign in source target order to community. Then Evaluate once cluster_weight.get(community, 0.0) + node_weight[node]; assign in source target order to cluster_weight[community].
  }
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:457-457
  In source order: Evaluate once sum((weight * weight for weight in cluster_weight.values())); assign in source target order to squared.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:458-458
  End this invocation with (internal - resolution * squared) / (2.0 * total_weight).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:461-463
// Source signature: modularity(adjacency: Adjacency, communities: dict[str, int]) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn modularity(adjacency, communities) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:462-462
  In source order: Evaluate once quality(adjacency, communities, LeidenOptions(objective=Objective.MODULARITY)); assign in source target order to value.
  // Source: vendor/context_graph_sdk/src/context_graph_sdk/analysis/leiden.py:463-463
  End this invocation with 0.0 if math.isnan(value) else value.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

No statically resolved in-checkout import; external calls remain explicit dependency boundaries.
