"""Abhi's Notes palette ("Sorbet") for matplotlib and Plotly.

matplotlib:

    import palette
    palette.apply()                      # Arial, pastel colour cycle, "sorbet" colormaps
    ...
    plt.savefig(palette.img_dir("my-post") / "figure.svg")

Plotly:

    import palette
    palette.apply_plotly()               # registers and activates the "sorbet" template
    fig = px.imshow(z)                   # heatmaps / continuous colour use the sorbet scales
    palette.plotly_html(fig, "my-post", "heatmap")
    # then in the post:  {% include plots/my-post/heatmap.html %}

Keep the hex values in sync with assets/css/style.css and assets/js/mermaid-init.js.
"""
from pathlib import Path

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

# Continuous scales, light to dark so low values sit close to the page background.
SEQUENTIAL = ["#F1F5FA", "#C9DAEC", "#7FA8D1", "#4F7FB5", "#2E5C8C"]          # blues
SEQUENTIAL_WARM = ["#FBF5E4", "#EAD27A", "#F2B28C", "#E8A0A8", "#C4707B"]     # butter -> peach -> rose
DIVERGING = ["#C4707B", "#E8A0A8", "#F7F3EE", "#7FA8D1", "#2E5C8C"]            # rose <- neutral -> blue

REPO_ROOT = Path(__file__).resolve().parents[1]
FONT = "Arial, Helvetica, sans-serif"


def img_dir(post_slug: str) -> Path:
    """Return (and create) assets/img/posts/<post_slug>/ for a post's figures."""
    d = REPO_ROOT / "assets" / "img" / "posts" / post_slug
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------- matplotlib

def apply() -> None:
    """Apply the blog style to matplotlib's global rcParams and register colormaps."""
    import matplotlib as mpl
    from cycler import cycler
    from matplotlib.colors import LinearSegmentedColormap

    for name, colors in (("sorbet", SEQUENTIAL), ("sorbet_warm", SEQUENTIAL_WARM), ("sorbet_div", DIVERGING)):
        if name not in mpl.colormaps:
            cmap = LinearSegmentedColormap.from_list(name, colors)
            mpl.colormaps.register(cmap)
            mpl.colormaps.register(cmap.reversed(), name=name + "_r")

    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.prop_cycle": cycler(color=COLORS),
        "image.cmap": "sorbet",
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


# -------------------------------------------------------------------- plotly

def plotly_template():
    """Build the "sorbet" Plotly template (without registering it)."""
    import plotly.graph_objects as go

    axis = dict(
        gridcolor=RULE,
        zerolinecolor=RULE,
        linecolor=RULE,
        tickcolor=RULE,
        tickfont=dict(color=MUTED),
        title=dict(font=dict(color=TEXT)),
        showline=False,
    )
    colorbar = dict(outlinewidth=0, ticks="", tickfont=dict(color=MUTED), thickness=14)

    return go.layout.Template(
        layout=dict(
            font=dict(family=FONT, color=TEXT, size=13),
            title=dict(font=dict(size=16, color=TEXT), x=0, xanchor="left"),
            paper_bgcolor=BACKGROUND,
            plot_bgcolor=BACKGROUND,
            colorway=COLORS,
            colorscale=dict(
                sequential=SEQUENTIAL,
                sequentialminus=SEQUENTIAL_WARM,
                diverging=DIVERGING,
            ),
            xaxis=axis,
            yaxis=axis,
            legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=MUTED)),
            hoverlabel=dict(font=dict(family=FONT), bordercolor=RULE),
            hovermode="closest",
            margin=dict(l=50, r=20, t=50, b=50),
            coloraxis=dict(colorbar=colorbar),
        ),
        data=dict(
            heatmap=[go.Heatmap(colorscale=SEQUENTIAL, colorbar=colorbar)],
            contour=[go.Contour(colorscale=SEQUENTIAL, colorbar=colorbar)],
            histogram2d=[go.Histogram2d(colorscale=SEQUENTIAL, colorbar=colorbar)],
            surface=[go.Surface(colorscale=SEQUENTIAL, colorbar=colorbar)],
            scatter=[go.Scatter(marker=dict(colorbar=colorbar))],
            bar=[go.Bar(marker=dict(line=dict(width=0)))],
        ),
    )


def apply_plotly(name: str = "sorbet") -> None:
    """Register the template with plotly.io and make it the default."""
    import plotly.io as pio

    pio.templates[name] = plotly_template()
    pio.templates.default = name


def plotly_html(fig, post_slug: str, name: str) -> str:
    """Write `fig` as an HTML fragment to _includes/plots/<post_slug>/<name>.html.

    Returns the Liquid tag to paste into the post. plotly.js is loaded from the CDN
    once per page, so include several figures freely.
    """
    d = REPO_ROOT / "_includes" / "plots" / post_slug
    d.mkdir(parents=True, exist_ok=True)
    out = d / f"{name}.html"
    fig.write_html(
        out,
        full_html=False,
        include_plotlyjs="cdn",
        default_width="100%",
        default_height="420px",
        config={"responsive": True, "displaylogo": False},
    )
    return f"{{% include plots/{post_slug}/{name}.html %}}"
