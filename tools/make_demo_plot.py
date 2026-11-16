"""Demo plot showing the palette. Writes assets/img/demo/demo-plot.svg.

Run from anywhere:  python tools/make_demo_plot.py
"""
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

import palette

palette.apply()

x = np.linspace(0, 2 * np.pi, 200)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.6))

for i, name in enumerate(palette.ACCENTS):
    ax1.plot(x, np.sin(x - i * 0.5) + i * 0.3, label=name)
ax1.set_title("Lines")
ax1.set_xlabel("x")
ax1.legend(ncol=2, fontsize=9)

ax2.bar(list(palette.ACCENTS), [5, 7, 4, 8, 6, 3], color=palette.COLORS)
ax2.set_title("Bars")
ax2.tick_params(axis="x", labelrotation=30)

out = palette.REPO_ROOT / "assets" / "img" / "demo" / "demo-plot.svg"
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out)
print(f"wrote {out}")
