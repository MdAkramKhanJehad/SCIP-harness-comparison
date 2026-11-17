"""Draw knob counts by category for both harnesses.

Reads the two registries and writes, into ../graphs/:
  knob_counts_by_category.{png,svg}   grouped bars, one pair per category
  knob_origin_by_category.{png,svg}   per harness, each category split by origin
  knob_counts_by_category.csv         the numbers behind both charts

Run from comparison-results/:  python3 tools/plot_knob_counts.py
"""
import collections
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "graphs"
OUT.mkdir(exist_ok=True)

HARNESSES = [("VulnHunter", "vulnhunter.knobs.yaml"), ("VVAH", "vvah.knobs.yaml")]
CATEGORIES = [
    "model_routing", "budget_and_termination", "decomposition_and_parallelism",
    "scope_and_coverage", "context_supply", "tool_access", "detection_method",
    "gating_and_thresholds", "verification_depth", "dedup_and_merge",
    "ranking_and_reporting", "remediation", "runtime_and_infra", "evaluation",
]
REAL_CONFIG = {"config_file", "builtin_default", "cli_flag", "env_var"}
ORIGIN_BUCKETS = ["Real config", "Prompt text", "Code constant / not set"]


def bucket(origin):
    if origin in REAL_CONFIG:
        return "Real config"
    if origin == "prompt_text":
        return "Prompt text"
    return "Code constant / not set"


# Reference palette (dataviz skill, light mode)
SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
GRID = "#e4e3df"
HARNESS_COLOR = {"VulnHunter": "#2a78d6", "VVAH": "#eb6834"}   # slots 1, 2
ORIGIN_COLOR = {"Real config": "#1baf7a",                       # slot 3 aqua
                "Prompt text": "#6250d6",                       # slot 7 violet
                "Code constant / not set": "#a8a7a2"}           # neutral

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10,
    "text.color": TEXT, "axes.labelcolor": TEXT2,
    "xtick.color": TEXT2, "ytick.color": TEXT,
    "axes.edgecolor": GRID, "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
})

counts = {}           # (harness, category) -> total
origin = {}           # (harness, category, bucket) -> count
for name, fname in HARNESSES:
    data = yaml.safe_load(open(ROOT / fname))
    for cat, groups in data["categories"].items():
        for knobs in groups.values():
            for k in knobs:
                counts[(name, cat)] = counts.get((name, cat), 0) + 1
                key = (name, cat, bucket(k["origin"]))
                origin[key] = origin.get(key, 0) + 1

# Sort categories by combined total, largest at top.
order = sorted(CATEGORIES, key=lambda c: sum(counts.get((h, c), 0) for h, _ in HARNESSES))
labels = [c.replace("_", " ") for c in order]

with open(OUT / "knob_counts_by_category.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["category", "harness", "total"] + ORIGIN_BUCKETS)
    for c in reversed(order):
        for h, _ in HARNESSES:
            w.writerow([c, h, counts.get((h, c), 0)] + [origin.get((h, c, b), 0) for b in ORIGIN_BUCKETS])


def style(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.tick_params(axis="y", length=0)


def save(fig, stem):
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=170, bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)


# ---- Chart 1: grouped bars ----
fig, ax = plt.subplots(figsize=(10, 8))
bar_h = 0.38
gap = 0.02
for i, (h, _) in enumerate(HARNESSES):
    ys = [y + (bar_h / 2 + gap / 2) * (1 if i == 0 else -1) for y in range(len(order))]
    vals = [counts.get((h, c), 0) for c in order]
    ax.barh(ys, vals, height=bar_h, color=HARNESS_COLOR[h], label=h, edgecolor=SURFACE, linewidth=1)
    for y, v in zip(ys, vals):
        ax.text(v + 6, y, str(v) if v else "0 (none)", va="center", fontsize=8.5, color=TEXT2)
ax.set_yticks(range(len(order)))
ax.set_yticklabels(labels)
ax.set_xlabel("Number of knobs")
style(ax)
totals = {h: sum(counts.get((h, c), 0) for c in CATEGORIES) for h, _ in HARNESSES}
ax.set_title("Knobs by category", loc="left", fontsize=14, fontweight="bold", pad=26)
ax.text(0, 1.015, f"VulnHunter {totals['VulnHunter']:,} knobs  ·  VVAH {totals['VVAH']:,} knobs  ·  "
        "all origins (config, prompt, code)", transform=ax.transAxes, color=TEXT2, fontsize=9.5)
ax.legend(loc="lower right", frameon=False)
ax.set_xlim(0, max(counts.values()) * 1.12)
save(fig, "knob_counts_by_category")

# ---- Chart 2: origin split, one panel per harness, shared x ----
fig, axes = plt.subplots(1, 2, figsize=(13, 8), sharey=True, sharex=True)
xmax = max(counts.values()) * 1.15
for ax, (h, _) in zip(axes, HARNESSES):
    left = [0] * len(order)
    for b in ORIGIN_BUCKETS:
        vals = [origin.get((h, c, b), 0) for c in order]
        ax.barh(range(len(order)), vals, left=left, height=0.7, color=ORIGIN_COLOR[b],
                label=b, edgecolor=SURFACE, linewidth=1.5)
        left = [l + v for l, v in zip(left, vals)]
    for y, c in enumerate(order):
        real = origin.get((h, c, "Real config"), 0)
        tot = counts.get((h, c), 0)
        txt = f"{tot}" + (f"  ({real} config)" if real else "")
        ax.text(tot + 6, y, txt, va="center", fontsize=8.5, color=TEXT2)
    real_total = sum(origin.get((h, c, "Real config"), 0) for c in CATEGORIES)
    ax.set_title(f"{h}: {real_total} real-config of {totals[h]:,} knobs", loc="left",
                 fontsize=11.5, fontweight="bold")
    ax.set_xlim(0, xmax)
    ax.set_xlabel("Number of knobs")
    style(ax)
axes[0].set_yticks(range(len(order)))
axes[0].set_yticklabels(labels)
handles, lbls = axes[0].get_legend_handles_labels()
fig.legend(handles, lbls, loc="upper left", ncol=3, frameon=False, bbox_to_anchor=(0.0, 0.985))
fig.suptitle("Where each category's knobs come from", x=0.0, ha="left", y=1.035,
             fontsize=14, fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.95))
save(fig, "knob_origin_by_category")

print("wrote", sorted(p.name for p in OUT.iterdir()))
