/* ==========================================================================
   Renders the sidebar into <div id="sidebar-root"></div> using PYSOUP_NAV
   (from nav-data.js) and highlights whichever link matches the current
   page's data-page attribute.

   To add a new page:
     1. Copy template.html, rename it, set <body data-page="your-id">
     2. Add { page: "your-id", title: "...", href: "your-file.html" }
        to nav-data.js
   That's it — sidebar, active-state, and styling all come from this file
   and styles.css. Nothing else needs to change.
   ========================================================================== */

(function renderSidebar() {
  const currentPage = document.body.getAttribute("data-page");
  const root = document.getElementById("sidebar-root");
  if (!root) return;

  const brand = `
    <a class="brand" href="index.html">
      <span class="brand-mark">PySoup</span>
    </a>
    <p class="brand-tag">Python scripting for Paper</p>
  `;

  const groups = PYSOUP_NAV.map((group) => {
    const links = group.links
      .map((link) => {
        const active = link.page === currentPage ? " active" : "";
        return `<a class="nav-link${active}" href="${link.href}">${link.title}</a>`;
      })
      .join("");
    return `
      <div class="nav-group">
        <p class="nav-group-label">${group.label}</p>
        ${links}
      </div>
    `;
  }).join("");

  root.innerHTML = brand + groups;
})();
