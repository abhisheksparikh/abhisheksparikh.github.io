"""Abhi's Notes palette ("Sorbet") for matplotlib.

Usage in a plot script:

    import palette
    palette.apply()
    ...
    plt.savefig(palette.img_dir("my-post") / "figure.svg")

Keep the hex values in sync with assets/css/style.css and assets/js/mermaid-init.js.
"""
from pathlib import Path

import matplotlib as mpl
from cycler import cycler

BACKGROUND = "#FDFCFA"
TEXT = "#2E2E2E"
MUTED = "#7A7A7A"
RULE = "#E6E2DC"
LINK = "#4F7FB5"

ACCENTS = {
    "blue": "#7FA8D1",
    "sage": "#9CC5A1",
    "peach": "#F2B28C",
    "lavender": "#B59FD1",
    "rose": "#E8A0A8",
    "butter": "#EAD27A",
}
COLORS = list(ACCENTS.values())

REPO_ROOT = Path(__file__).resolve().parents[1]


def img_dir(post_slug: str) -> Path:
    """Return (and create) assets/img/posts/<post_slug>/ for a post's figures."""
    d = REPO_ROOT / "assets" / "img" / "posts" / post_slug
    d.mkdir(parents=True, exist_ok=True)
    return d


def apply() -> None:
    """Apply the blog style to matplotlib's global rcParams."""
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.prop_cycle": cycler(color=COLORS),
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": BACKGROUND,
        "savefig.facecolor": BACKGROUND,
        "text.color": TEXT,
        "axes.labelcolor": TEXT,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "axes.edgecolor": RULE,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": RULE,
        "grid.linewidth": 0.8,
        "lines.linewidth": 2.2,
        "legend.frameon": False,
        "figure.figsize": (7, 4),
        "figure.dpi": 110,
        "savefig.bbox": "tight",
        "svg.fonttype": "none",  # keep text as real text so the browser renders Arial
    })
