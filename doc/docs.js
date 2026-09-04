/* ==========================================================================
   Shared page methods, driven off the same PYSOUP_NAV data used by the
   sidebar. Call docsInit() once, after nav-data.js and hljs have loaded.
   ========================================================================== */

function addCopyButtons() {
  document.querySelectorAll("pre").forEach((pre) => {
    if (pre.querySelector(".copy-btn")) return; // already added

    const btn = document.createElement("button");
    btn.className = "copy-btn";
    btn.type = "button";
    btn.textContent = "Copy";
    btn.setAttribute("aria-label", "Copy code to clipboard");

    btn.addEventListener("click", () => {
      const code = pre.querySelector("code");
      if (!code) return;
      navigator.clipboard.writeText(code.innerText).then(() => {
        btn.textContent = "Copied";
        btn.classList.add("copied");
        setTimeout(() => {
          btn.textContent = "Copy";
          btn.classList.remove("copied");
        }, 1600);
      });
    });

    pre.style.position = "relative";
    pre.appendChild(btn);
  });
}

/* Flattens PYSOUP_NAV into a single ordered list, then renders a
   prev/next footer for whichever page is current. Reorder pages by
   reordering nav-data.js — this footer follows automatically. */
function renderPageFooter() {
  const container = document.getElementById("page-footer-root");
  if (!container || typeof PYSOUP_NAV === "undefined") return;

  const flat = PYSOUP_NAV.flatMap((group) => group.links);
  const currentPage = document.body.getAttribute("data-page");
  const index = flat.findIndex((link) => link.page === currentPage);
  if (index === -1) return;

  const prev = flat[index - 1];
  const next = flat[index + 1];

  container.innerHTML = `
    <div class="page-footer">
      ${prev ? `<a class="page-footer-link prev" href="${prev.href}">
                  <span class="page-footer-dir">Previous</span>
                  <span class="page-footer-title">${prev.title}</span>
                </a>` : "<span></span>"}
      ${next ? `<a class="page-footer-link next" href="${next.href}">
                  <span class="page-footer-dir">Next</span>
                  <span class="page-footer-title">${next.title}</span>
                </a>` : "<span></span>"}
    </div>
  `;
}

function docsInit() {
  addCopyButtons();
  renderPageFooter();
}
