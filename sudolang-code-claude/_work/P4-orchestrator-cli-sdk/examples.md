# Examples: P4-orchestrator-cli-sdk

## 1. Gate and cap: sdk/handoff.py inject_findings

Source `vvaharness/sdk/handoff.py:57-73`:
```
    if not findings:
        raise HandoffError("no findings to inject")
    if len(findings) > MAX_INJECTED_FINDINGS:
        raise HandoffError(
            f"{len(findings)} findings exceeds MAX_INJECTED_FINDINGS={MAX_INJECTED_FINDINGS}")
    bad = [f for f in findings if not isinstance(f, Finding)]
    if bad:
        raise HandoffError(f"every item must be a Finding; got {type(bad[0]).__name__}")
    repo_path = Path(repo).expanduser().resolve()
    if not repo_path.is_dir():
        raise HandoffError(f"repo is not a directory: {repo}")
    run_id = run_id_for(repo_path)
    ckpt_dir = _store.state_root() / "checkpoints" / run_id
    _store.register_run(run_id, repo_root=str(repo_path), repo_name=repo_path.name, app_id=None)
    save_ckpt(ckpt_dir, run_id, "s4",
              {"findings": list(findings), "outcomes": _outcomes(findings),
               "input_kind": "external"})
```
SudoLang `vvah/vvaharness/sdk/handoff.sudo`:
```
  require findings is not empty => throw HandoffError("no findings to inject")
  require length(findings) <= MAX_INJECTED_FINDINGS => throw HandoffError("<n> findings exceeds MAX_INJECTED_FINDINGS=2000")
  require every item is a Finding => throw HandoffError("every item must be a Finding; got <type>")
  repo_path = repo with "~" expanded, resolved
  require repo_path is a directory => throw HandoffError("repo is not a directory: <repo>")
  run_id = checkpoints.run_id_for(repo_path)
  ckpt_dir = store.state_root() + "/checkpoints/$run_id"
  store.register_run(run_id, repo_root=repo_path, repo_name=name of repo_path, app_id=null)
  checkpoints.save_ckpt(ckpt_dir, run_id, "s4", { findings, outcomes: _outcomes(findings), input_kind: "external" })
```

## 2. Threshold gate: orchestrator/preflight.py _warn_deepagents_tuned_max_turns

Source `vvaharness/orchestrator/preflight.py:205-215`:
```
def _warn_deepagents_tuned_max_turns(cfg) -> None:
    for stage_key, role in _TURN_CAPPED_STAGES:
        block = getattr(cfg, stage_key, None)
        model = getattr(getattr(cfg, "models", None), role, None)
        turns = getattr(block, "max_turns", None)
        if block is None or model is None or not isinstance(turns, int) or turns <= 0:
            continue
        via = resolve_model(model).via
        if via not in _HARD_TURN_CAP_VIAS or turns > _STARVED_TURN_CEILING:
            continue
        log.warning(Event.PREFLIGHT_MAX_TURNS_HARD_CAPPED, ...)
```
SudoLang `vvah/vvaharness/orchestrator/preflight.sudo` (constants `_HARD_TURN_CAP_VIAS = ["sdk", "cli", "openai"]`, `_STARVED_TURN_CEILING = 20`, preflight.py:196-202):
```
// src: vvaharness/orchestrator/preflight.py:205-224
fn _warn_deepagents_tuned_max_turns(cfg):executor=code {
  for each [stage_key, role] in _TURN_CAPPED_STAGES {
    turns = knob("$stage_key.max_turns", default=null); model = cfg.models[role]
    if (stage block or model missing || turns is not a positive integer) continue
    via = resolve_model(model).via
    if (via in _HARD_TURN_CAP_VIAS && turns <= _STARVED_TURN_CEILING) {
      warn PREFLIGHT_MAX_TURNS_HARD_CAPPED
    }
  }
}
```

## 3. Bounds: sdk/plugins.py PluginSet

Source `vvaharness/sdk/plugins.py:94-95, 112-120`:
```
    if len(plugins) > MAX_PLUGINS:
        raise ValueError(f"at most {MAX_PLUGINS} plugins")
...
    def __init__(self, plugins: Iterable[object] = ()) -> None:
        self._plugins = _validated(tuple(plugins))
        merged = Contribution()
        for plugin in self._plugins:
            merged = merged.merge(plugin.contribute())
        if len(merged.graph_tools) > MAX_PLUGIN_GRAPH_TOOLS:
            raise ValueError(f"at most {MAX_PLUGIN_GRAPH_TOOLS} plugin graph tools")
        self._contribution = merged
```
SudoLang `vvah/vvaharness/sdk/plugins.sudo`:
```
  require length(plugins) <= MAX_PLUGINS => throw ValueError("at most 16 plugins")
...
    _plugins = _validated(plugins)
    merged = Contribution()
    for each plugin in _plugins { merged = merged.merge(plugin.contribute()) }
    require length(merged.graph_tools) <= MAX_PLUGIN_GRAPH_TOOLS => throw ValueError("at most 8 plugin graph tools")
```
