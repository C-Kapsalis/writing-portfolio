
report-template-site
====================

**A working demo of my documentation approach for BI-shy marketers — where the
tutorial is not about the product; the tutorial is the product.**
report-template-site is a small open-source web app (React + TypeScript,
deployable to Vercel as a static site) that demonstrates a single-page
reporting template for email marketers who have no data team: one combo chart
and one matrix, driven entirely by three field-parameter selectors — *plot
axis*, *legend*, *measures* — with a hamburger menu of views and four built-in
**bookmarks**, each a saved pre-selection that answers one recurring marketing
question ("is deliverability slipping?", "which sends earned their keep?").
The interaction model replicates, in web form, the field-parameter-and-bookmark
pattern professional BI teams build in Power BI; the demo runs on twelve months
of fictional data for an unnamed specialty tea-and-homeware shop — the demo
deliberately names no business — seeded with deliberately weak sends and a
quietly eroding list segment so that every bookmark has a story to tell.

I built the app, but I treat the project as a writing artifact. It is the
worked, end-to-end demonstration of the approach I lay out in
:doc:`documenting-bi-reports-for-marketers`, and every principle on that page
is embodied somewhere concrete here:

- **The tutorial teaches by doing, starting from blank.** The second page of
  the app *is* the tutorial: empty selectors, an empty canvas, and six
  numbered, coach-marked steps in which the reader picks an axis, a legend and
  their first measures, watches the chart and matrix assemble themselves, saves the
  result as a named bookmark, switches to a built-in view, and returns to
  their own. The closing lesson lands in the hands, not in prose: *a bookmark
  is just a saved pre-selection of dimensions and measures that answers one
  recurring question.* Each step gates its "Next" on the reader actually
  having done the thing — instructional design as UI state.
- **The missing theory ships alongside the product.** Four short explanation
  guides — the deliverability funnel, CTR versus CTOR, list health and
  erosion, campaigns over time and revenue — live both in the repo's docs and
  inside the app itself, one behind each bookmark, so the discipline
  knowledge arrives at the moment the view raises the question.
- **The glossary governs.** Every metric has exactly one canonical definition
  in the reference layer; the in-app glossary and selector hints restate it,
  and the semantics are enforced, not merely described — the report declines
  to plot meaningless dimension–metric combinations, saying why in a notice,
  and politely objects when a per-send benchmark (CTR against its 2–5% band)
  is asked of a monthly aggregate.
- **How-to guides branch on what the data shows.** The reading-order guide is
  written as a decision tree — check the deliverability gate first; branch on
  what you find — rather than a linear checklist that abandons readers at the
  first fork.

The documentation set is Diátaxis-shaped end to end: two tutorials (using the
demo, and rebuilding the same template natively in Power BI Desktop with field
parameters, bookmarks and the selection-pane menu), three how-to guides
(reading the report, swapping in your own data, deploying), a four-page
reference layer (glossary, data model, bookmark shape, code map), and five
explanation pieces — including one arguing the template's own thesis, with its
trade-offs stated honestly: one canvas plus bookmarks replaces a stack of
static report pages, but only if the metric catalog stays governed.

Project links
-------------

- `Live demo <https://bi-report-template-site.vercel.app/>`_ — the report and
  the blank-start tutorial, running in the browser.
- `report-template-site repository on GitHub
  <https://github.com/c-kapsalis/report-template-site>`_ — source code, full
  documentation, and release notes.

The repository ships the project's complete Diátaxis documentation set
(``docs/`` plus release notes); this page is the showcase, not the docs.
