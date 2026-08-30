/* ==========================================================================
   Sidebar nav structure — edit THIS file to add/reorder pages.
   Every page's sidebar renders from this one array, so adding a new doc
   page never means touching HTML in more than one place.

   `page` must match the data-page attribute on that page's <body> tag,
   which is how nav.js knows which link to highlight as active.
   ========================================================================== */

const PYSOUP_NAV = [
  {
    label: "Get started",
    links: [
      { page: "index", title: "Overview", href: "index.html" },
    ],
  },
  {
    label: "Scripting",
    links: [
      { page: "events", title: "Events", href: "events.html" },
      { page: "async-events", title: "Async events", href: "async-events.html" },
      { page: "items", title: "Items & inventory", href: "items.html" },
      { page: "scheduler", title: "Scheduler", href: "scheduler.html" },
    ],
  },
  {
    label: "Reference",
    links: [
      { page: "errors", title: "Reading errors", href: "errors.html" },
      { page: "limitations", title: "Known limitations", href: "limitations.html" },
    ],
  },
];
