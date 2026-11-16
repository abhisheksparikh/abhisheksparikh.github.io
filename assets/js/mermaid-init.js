// Renders ```mermaid fenced blocks with the site palette. Mermaid is only
// downloaded on pages that actually contain a diagram.
const blocks = document.querySelectorAll("div.language-mermaid, pre > code.language-mermaid");
if (blocks.length) {
  const { default: mermaid } = await import("https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs");
  blocks.forEach((el) => {
    const target = el.tagName === "CODE" ? el.parentElement : el;
    const pre = document.createElement("pre");
    pre.className = "mermaid";
    pre.textContent = el.textContent.trim();
    target.replaceWith(pre);
  });
  mermaid.initialize({
    startOnLoad: false,
    theme: "base",
    fontFamily: "Arial, Helvetica, sans-serif",
    themeVariables: {
      background: "#FDFCFA",
      primaryColor: "#7FA8D1",
      primaryTextColor: "#2E2E2E",
      primaryBorderColor: "#4F7FB5",
      secondaryColor: "#9CC5A1",
      secondaryTextColor: "#2E2E2E",
      secondaryBorderColor: "#9CC5A1",
      tertiaryColor: "#F2B28C",
      tertiaryTextColor: "#2E2E2E",
      tertiaryBorderColor: "#F2B28C",
      lineColor: "#7A7A7A",
      textColor: "#2E2E2E",
      noteBkgColor: "#EAD27A",
      noteTextColor: "#2E2E2E",
      noteBorderColor: "#EAD27A",
      edgeLabelBackground: "#FDFCFA"
    }
  });
  await mermaid.run({ querySelector: "pre.mermaid" });
}
