"""Demo Plotly figures in the palette: a heatmap, a continuous-colour scatter and a
diverging heatmap. Writes a standalone page to assets/img/demo/demo-plotly.html.

Run from anywhere:  python tools/make_demo_plotly.py
"""
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import palette

palette.apply_plotly()

rng = np.random.default_rng(0)
z = rng.random((8, 12)).cumsum(axis=1)

fig = make_subplots(
    rows=1, cols=3,
    subplot_titles=("Heatmap (sequential)", "Scatter (continuous colour)", "Heatmap (diverging)"),
    horizontal_spacing=0.08,
)
fig.add_trace(go.Heatmap(z=z, colorbar=dict(x=0.27)), row=1, col=1)
x = rng.normal(size=120)
fig.add_trace(
    go.Scatter(x=x, y=x + rng.normal(scale=0.6, size=120), mode="markers",
               marker=dict(color=x, colorscale=palette.SEQUENTIAL_WARM, size=9, showscale=True,
                           colorbar=dict(x=0.63))),
    row=1, col=2,
)
fig.add_trace(go.Heatmap(z=z - z.mean(), colorscale=palette.DIVERGING, zmid=0), row=1, col=3)
fig.update_layout(title="Sorbet palette, Plotly", height=380, showlegend=False)

out = palette.REPO_ROOT / "assets" / "img" / "demo" / "demo-plotly.html"
fig.write_html(out, include_plotlyjs="cdn", config={"responsive": True, "displaylogo": False})
print(f"wrote {out}")

# Also exercise the discrete colourway through plotly.express.
fig2 = px.bar(x=list(palette.ACCENTS), y=[5, 7, 4, 8, 6, 3], color=list(palette.ACCENTS), title="Colourway")
print("express colourway:", [t.marker.color for t in fig2.data])
