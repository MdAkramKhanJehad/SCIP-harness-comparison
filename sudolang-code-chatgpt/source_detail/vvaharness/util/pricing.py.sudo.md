# vvaharness/util/pricing.py

Structural SudoLang detail. Every source statement is represented; straight-line plumbing is grouped.
Source expressions retain Python evaluation semantics as documented in `representation_specification.md`.
Calls supply arguments or expose tools; they do not imply model compliance or an unshown tool invocation.
Long strings/templates resolve through this module's exact evidence asset; no literal content is inferred.

Evidence: `assets/vvaharness/util/pricing.py.evidence.json`. SHA-256: `2e443fca6eba526f309a6247439ba6a1d8348291bdfee51790ed45e1c67ac1c0`.

```sudo
// Source: vvaharness/util/pricing.py:15-21
In source order: Retain source documentation literal source_literal_15_0; it is not a model call. Then Resolve source import from __future__ import annotations; preserve alias and import-time effects. Then Resolve source import import hashlib; preserve alias and import-time effects. Then Resolve source import import os; preserve alias and import-time effects. Then Resolve source import import threading; preserve alias and import-time effects.
// Source: vvaharness/util/pricing.py:22-27
In source order: Resolve source import from collections.abc import Mapping; preserve alias and import-time effects. Then Resolve source import from dataclasses import dataclass; preserve alias and import-time effects. Then Resolve source import from pathlib import Path; preserve alias and import-time effects. Then Resolve source import from typing import TypedDict; preserve alias and import-time effects. Then Resolve source import import yaml; preserve alias and import-time effects.
// Source: vvaharness/util/pricing.py:29-36
In source order: Resolve source import from vvaharness.util import console; preserve alias and import-time effects. Then Evaluate once 'VVAHARNESS_PRICING_FILE'; assign in source target order to PRICING_FILE_ENV. Then Evaluate once 1000000.0; assign in source target order to _PER_MTOK. Then Evaluate once 0.1; assign in source target order to FALLBACK_CACHE_READ_FRACTION. Then Evaluate once 1.25; assign in source target order to FALLBACK_CACHE_WRITE_MULTIPLIER.
// Source: vvaharness/util/pricing.py:40-46
// Source: vvaharness/util/pricing.py:39-39
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/util/pricing.py:40-46
interface CacheRateDefaults {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/pricing.py:41-46
  In source order: Retain source documentation literal source_literal_41_4; it is not a model call. Then For read_fraction, assign FALLBACK_CACHE_READ_FRACTION; source annotation float. Then For write_multiplier, assign FALLBACK_CACHE_WRITE_MULTIPLIER; source annotation float. Then For is_fallback, assign True; source annotation bool.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/util/pricing.py:49-56
interface TokenBucket {
  Describe the source Python type, preserving its base/metaclass expression order: TypedDict, total=False.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/pricing.py:50-55
  In source order: Retain source documentation literal source_literal_50_4; it is not a model call. Then For prompt, declare without assigning a value; source annotation int. Then For completion, declare without assigning a value; source annotation int. Then For cache_read, declare without assigning a value; source annotation int. Then For cache_write, declare without assigning a value; source annotation int.
  // Source: vvaharness/util/pricing.py:56-56
  In source order: For calls, declare without assigning a value; source annotation int.
}
// Source: vvaharness/util/pricing.py:60-66
// Source: vvaharness/util/pricing.py:59-59
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/util/pricing.py:60-66
interface ModelPricing {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/pricing.py:61-66
  In source order: Retain source documentation literal source_literal_61_4; it is not a model call. Then For input_per_mtok, declare without assigning a value; source annotation float. Then For output_per_mtok, declare without assigning a value; source annotation float. Then For cache_read_per_mtok, assign None; source annotation float | None. Then For cache_creation_per_mtok, assign None; source annotation float | None.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/util/pricing.py:70-77
// Source: vvaharness/util/pricing.py:69-69
Before evaluating bases/metaclass and executing the type body, evaluate and retain decorators top-to-bottom: dataclass(frozen=True).
// Source: vvaharness/util/pricing.py:70-77
interface PricingTable {
  Describe the source Python type, preserving its base/metaclass expression order: implicit object.
  Execute field/nested-definition operations in source type-body order; type instantiation/descriptor semantics remain those of the cited source and dependencies.
  // Source: vvaharness/util/pricing.py:71-76
  In source order: Retain source documentation literal source_literal_71_4; it is not a model call. Then For models, declare without assigning a value; source annotation dict[str, ModelPricing]. Then For path, declare without assigning a value; source annotation str. Then For sha256, declare without assigning a value; source annotation str. Then For source, declare without assigning a value; source annotation str.
  // Source: vvaharness/util/pricing.py:77-77
  In source order: For cache_defaults, assign CacheRateDefaults(); source annotation CacheRateDefaults.
}
Apply the retained type decorators bottom-to-top after creating the source type; bind the resulting object to the source name.
// Source: vvaharness/util/pricing.py:80-84
// Source signature: _rate(raw: Mapping[str, object], key: str) -> float | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _rate(raw, key) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:81-81
  In source order: Evaluate once raw.get(key); assign in source target order to value.
  // Source: vvaharness/util/pricing.py:82-83
  if (the source predicate isinstance(value, bool) or not isinstance(value, int | float) is truthy) {
    // Source: vvaharness/util/pricing.py:83-83
    End this invocation with None.
  }
  // Source: vvaharness/util/pricing.py:84-84
  End this invocation with float(value).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:87-99
// Source signature: _model_pricing(raw: object) -> ModelPricing | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _model_pricing(raw) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:88-89
  if (the source predicate not isinstance(raw, Mapping) is truthy) {
    // Source: vvaharness/util/pricing.py:89-89
    End this invocation with None.
  }
  // Source: vvaharness/util/pricing.py:90-91
  In source order: Evaluate once _rate(raw, 'input_per_mtok'); assign in source target order to inp. Then Evaluate once _rate(raw, 'output_per_mtok'); assign in source target order to out.
  // Source: vvaharness/util/pricing.py:92-93
  if (the source predicate inp is None or out is None is truthy) {
    // Source: vvaharness/util/pricing.py:93-93
    End this invocation with None.
  }
  // Source: vvaharness/util/pricing.py:94-99
  End this invocation with ModelPricing(input_per_mtok=inp, output_per_mtok=out, cache_read_per_mtok=_rate(raw, 'cache_read_per_mtok'), cache_creation_per_mtok=_rate(raw, 'cache_creation_per_mtok')).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:102-118
// Source signature: _parse_cache_defaults(data: object) -> CacheRateDefaults
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_cache_defaults(data) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:103-103
  In source order: Retain source documentation literal source_literal_103_4; it is not a model call.
  // Source: vvaharness/util/pricing.py:104-105
  if (the source predicate not isinstance(data, Mapping) is truthy) {
    // Source: vvaharness/util/pricing.py:105-105
    End this invocation with CacheRateDefaults().
  }
  // Source: vvaharness/util/pricing.py:106-106
  In source order: Evaluate once data.get('cache_rate_defaults'); assign in source target order to raw.
  // Source: vvaharness/util/pricing.py:107-108
  if (the source predicate not isinstance(raw, Mapping) is truthy) {
    // Source: vvaharness/util/pricing.py:108-108
    End this invocation with CacheRateDefaults().
  }
  // Source: vvaharness/util/pricing.py:109-110
  In source order: Evaluate once _rate(raw, 'read_fraction'); assign in source target order to read. Then Evaluate once _rate(raw, 'write_multiplier'); assign in source target order to write.
  // Source: vvaharness/util/pricing.py:111-112
  if (the source predicate read is None and write is None is truthy) {
    // Source: vvaharness/util/pricing.py:112-112
    End this invocation with CacheRateDefaults().
  }
  // Source: vvaharness/util/pricing.py:113-118
  End this invocation with CacheRateDefaults(read_fraction=FALLBACK_CACHE_READ_FRACTION if read is None else read, write_multiplier=FALLBACK_CACHE_WRITE_MULTIPLIER if write is None else write, is_fallback=False).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:121-132
// Source signature: _parse_models(data: object) -> dict[str, ModelPricing]
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _parse_models(data) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:122-123
  if (the source predicate not isinstance(data, Mapping) is truthy) {
    // Source: vvaharness/util/pricing.py:123-123
    End this invocation with {}.
  }
  // Source: vvaharness/util/pricing.py:124-124
  In source order: Evaluate once data.get('models'); assign in source target order to raw_models.
  // Source: vvaharness/util/pricing.py:125-126
  if (the source predicate not isinstance(raw_models, Mapping) is truthy) {
    // Source: vvaharness/util/pricing.py:126-126
    End this invocation with {}.
  }
  // Source: vvaharness/util/pricing.py:127-127
  In source order: For out, assign {}; source annotation dict[str, ModelPricing].
  // Source: vvaharness/util/pricing.py:128-131
  for each (name, spec) in raw_models.items() {
    // Source: vvaharness/util/pricing.py:129-129
    In source order: Evaluate once _model_pricing(spec); assign in source target order to priced.
    // Source: vvaharness/util/pricing.py:130-131
    if (the source predicate isinstance(name, str) and priced is not None is truthy) {
      // Source: vvaharness/util/pricing.py:131-131
      In source order: Evaluate once priced; assign in source target order to out[name].
    }
  }
  // Source: vvaharness/util/pricing.py:132-132
  End this invocation with out.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:135-164
// Source signature: _table_from_file(path: Path, source: str) -> PricingTable | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _table_from_file(path, source) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:136-141
  Perform the following protected operations {
    // Source: vvaharness/util/pricing.py:137-138
    In source order: Evaluate once path.read_bytes(); assign in source target order to blob. Then For data, assign yaml.safe_load(blob.decode('utf-8')); source annotation object.
  }
  // Source: vvaharness/util/pricing.py:139-141
  On the first matching source exception (OSError, UnicodeDecodeError, yaml.YAMLError) as e, in handler order {
    // Source: vvaharness/util/pricing.py:140-140
    In source order: Evaluate console.write(source_template_140_22); retain side effects and discard the expression result.
    // Source: vvaharness/util/pricing.py:141-141
    End this invocation with None.
  }
  // Source: vvaharness/util/pricing.py:142-142
  In source order: Evaluate once _parse_models(data); assign in source target order to models.
  // Source: vvaharness/util/pricing.py:143-146
  if (the source predicate not models is truthy) {
    // Source: vvaharness/util/pricing.py:144-145
    In source order: Evaluate console.write(source_template_144_22); retain side effects and discard the expression result.
    // Source: vvaharness/util/pricing.py:146-146
    End this invocation with None.
  }
  // Source: vvaharness/util/pricing.py:147-147
  In source order: Evaluate once _parse_cache_defaults(data); assign in source target order to defaults.
  // Source: vvaharness/util/pricing.py:149-161
  for each (name, priced) in models.items() {
    // Source: vvaharness/util/pricing.py:150-153
    In source order: Evaluate once [field for field, rate in (('cache_read_per_mtok', priced.cache_read_per_mtok), ('cache_creation_per_mtok', priced.cache_creation_per_mtok)) if rate is None]; assign in source target order to omitted.
    // Source: vvaharness/util/pricing.py:154-155
    if (the source predicate not omitted is truthy) {
      // Source: vvaharness/util/pricing.py:155-155
      Continue the immediately enclosing source loop at its next iteration.
    }
    // Source: vvaharness/util/pricing.py:156-161
    In source order: Evaluate once "built-in fallback — Anthropic-shaped, verify it suits this model's provider" if defaults.is_fallback else 'from cache_rate_defaults'; assign in source target order to origin. Then Evaluate console.write(source_template_159_22); retain side effects and discard the expression result.
  }
  // Source: vvaharness/util/pricing.py:162-164
  End this invocation with PricingTable(models=models, path=str(path), sha256=hashlib.sha256(blob).hexdigest(), source=source, cache_defaults=defaults).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:167-173
// Source signature: _selected_source(cfg_pricing_file: str | None) -> tuple[str, str] | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn _selected_source(cfg_pricing_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:168-168
  In source order: Evaluate once os.environ.get(PRICING_FILE_ENV, '').strip(); assign in source target order to env_path.
  // Source: vvaharness/util/pricing.py:169-170
  if (the source predicate env_path is truthy) {
    // Source: vvaharness/util/pricing.py:170-170
    End this invocation with (env_path, 'env').
  }
  // Source: vvaharness/util/pricing.py:171-172
  if (the source predicate cfg_pricing_file is truthy) {
    // Source: vvaharness/util/pricing.py:172-172
    End this invocation with (str(cfg_pricing_file), 'config').
  }
  // Source: vvaharness/util/pricing.py:173-173
  End this invocation with None.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:176-183
// Source signature: load_pricing(cfg_pricing_file: str | None) -> PricingTable | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_pricing(cfg_pricing_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:177-179
  In source order: Retain source documentation literal source_literal_177_4; it is not a model call. Then Evaluate once _selected_source(cfg_pricing_file); assign in source target order to selected.
  // Source: vvaharness/util/pricing.py:180-181
  if (the source predicate selected is None is truthy) {
    // Source: vvaharness/util/pricing.py:181-181
    End this invocation with None.
  }
  // Source: vvaharness/util/pricing.py:182-182
  In source order: Evaluate once selected; assign in source target order to (raw_path, source).
  // Source: vvaharness/util/pricing.py:183-183
  End this invocation with _table_from_file(Path(raw_path).expanduser(), source).
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:187-188
In source order: For _PRICING_CACHE, assign {}; source annotation dict[tuple[str, str] | None, PricingTable | None]. Then Evaluate once threading.Lock(); assign in source target order to _PRICING_CACHE_LOCK.
// Source: vvaharness/util/pricing.py:191-200
// Source signature: load_pricing_cached(cfg_pricing_file: str | None) -> PricingTable | None
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn load_pricing_cached(cfg_pricing_file) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:192-193
  In source order: Retain source documentation literal source_literal_192_4; it is not a model call. Then Evaluate once _selected_source(cfg_pricing_file); assign in source target order to selected.
  // Source: vvaharness/util/pricing.py:194-200
  Enter source context managers left-to-right: _PRICING_CACHE_LOCK {
    // Source: vvaharness/util/pricing.py:195-199
    if (the source predicate selected not in _PRICING_CACHE is truthy) {
      // Source: vvaharness/util/pricing.py:196-199
      In source order: Evaluate once _table_from_file(Path(selected[0]).expanduser(), selected[1]) if selected is not None else None; assign in source target order to _PRICING_CACHE[selected].
    }
    // Source: vvaharness/util/pricing.py:200-200
    End this invocation with _PRICING_CACHE[selected].
  }
  Exit acquired managers in reverse order on all exits; preserve their exception-suppression semantics.
  If execution reaches this end, finish with the source implicit None result.
}
// Source: vvaharness/util/pricing.py:203-219
// Source signature: bucket_cost_usd(bucket: TokenBucket, pricing: ModelPricing, cache_defaults: CacheRateDefaults | None=None) -> float
Define the following callable; defaults and non-deferred annotations evaluate at definition time. Its nested body describes invocation, not definition-time execution.
fn bucket_cost_usd(bucket, pricing, cache_defaults) {
  Bind arguments/defaults/annotations exactly as the source signature specifies.
  // Source: vvaharness/util/pricing.py:205-211
  In source order: Retain source documentation literal source_literal_205_4; it is not a model call. Then Evaluate once cache_defaults or CacheRateDefaults(); assign in source target order to d. Then Evaluate once bucket.get('cache_write', 0); assign in source target order to cache_write. Then Evaluate once max(bucket.get('prompt', 0) - cache_write, 0); assign in source target order to fresh. Then Evaluate once pricing.input_per_mtok * d.write_multiplier if pricing.cache_creation_per_mtok is None else pricing.cache_creation_per_mtok; assign in source target order to write_rate.
  // Source: vvaharness/util/pricing.py:212-218
  In source order: Evaluate once pricing.input_per_mtok * d.read_fraction if pricing.cache_read_per_mtok is None else pricing.cache_read_per_mtok; assign in source target order to read_rate. Then Evaluate once fresh * pricing.input_per_mtok + cache_write * write_rate + bucket.get('cache_read', 0) * read_rate + bucket.get('completion', 0) * pricing.output_per_mtok; assign in source target order to total.
  // Source: vvaharness/util/pricing.py:219-219
  End this invocation with total / _PER_MTOK.
  If execution reaches this end, finish with the source implicit None result.
}
```

## Local import links

- `from vvaharness.util import console` at source line 29: `source_detail/vvaharness/util/__init__.py.sudo.md`.
- `from vvaharness.util import console` at source line 29: `source_detail/vvaharness/util/console.py.sudo.md`.
