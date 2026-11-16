# Abhi's Notes

Source for https://abhisheksparikh.github.io, built by GitHub Pages with Jekyll.

## Write a post

Create `_posts/YYYY-MM-DD-slug.md`:

~~~markdown
---
title: "My post"
---
Text in Markdown.

![A caption line](/assets/img/posts/slug/figure.svg)

```mermaid
flowchart LR
  idea --> experiment --> plot --> post
```
~~~

Photos and illustrations go in `assets/img/posts/<slug>/` and are referenced the same way.

## Make a plot with the palette

```bash
pip install -r tools/requirements.txt
```

In a script inside `tools/`:

```python
import palette
palette.apply()               # Arial, pastel colour cycle, light grid
...
plt.savefig(palette.img_dir("slug") / "figure.svg")
```

`python tools/make_demo_plot.py` writes a demo to `assets/img/demo/demo-plot.svg`.

## Palette ("Sorbet")

Defined in `assets/css/style.css`, `tools/palette.py` and `assets/js/mermaid-init.js`. Change all three together.

| role | hex | | accent | hex |
|---|---|---|---|---|
| background | `#FDFCFA` | | blue | `#7FA8D1` |
| text | `#2E2E2E` | | sage | `#9CC5A1` |
| muted | `#7A7A7A` | | peach | `#F2B28C` |
| rule | `#E6E2DC` | | lavender | `#B59FD1` |
| link | `#4F7FB5` | | rose | `#E8A0A8` |
| | | | butter | `#EAD27A` |

## Preview locally

```bash
jekyll serve --port 4000 --force_polling
```

Then open http://127.0.0.1:4000.

## Publish

```bash
git add -A
git commit -m "New post"
git push
```

GitHub Pages rebuilds the site in a minute or two.

## Analytics

Set `google_analytics: G-XXXXXXXXXX` in `_config.yml`. The tag is only emitted in production builds (GitHub Pages), never in local previews.
