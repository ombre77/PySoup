/* ==========================================================================
   Foldable tree, built from plain data.

   renderTree("container-id", [
     { label: "scripts/", open: true, children: [
       { label: "greeting.py" },
       { label: "items/", children: [
         { label: "wands.py", note: "loaded second" },
       ]},
     ]},
   ]);

   Node shape:
     label:    string, required
     children: array of nodes — presence of this key makes it foldable
     open:     boolean, starts expanded (default: false)
     note:     optional string shown right-aligned, dimmed

   Folding itself is native <details>/<summary> — works with zero JS,
   keyboard accessible by default. This function only builds the markup.
   ========================================================================== */

function renderTreeNode(node) {
  const note = node.note ? `<span class="tree-note">${node.note}</span>` : "";

  if (node.children && node.children.length) {
    const childrenHtml = node.children.map(renderTreeNode).join("");
    const openAttr = node.open ? " open" : "";
    return `
      <details class="tree-node"${openAttr}>
        <summary>${node.label}${note}</summary>
        <div class="tree-children">${childrenHtml}</div>
      </details>
    `;
  }

  return `<div class="tree-leaf">${node.label}${note}</div>`;
}

function renderTree(containerId, data) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.className = (container.className + " tree").trim();
  container.innerHTML = data.map(renderTreeNode).join("");
}
