Projects
========

This is where I gather the technical-writing work I can point to. It comes in
two kinds. The larger body is professional and internal: the documentation I
have written around the Power BI semantic models and the reports built on them
at Maya Insights. Because that work is client-confidential, it is *described*
here rather than shown. The second kind is my public open-source contributions,
which are still few — a single documentation fix so far, with more on the way
through the Canonical Open Documentation Academy and projects in my own domain
such as PyMC-Marketing.

Power BI semantic model & report documentation — Maya Insights
--------------------------------------------------------------

.. note::

   This documentation is internal and client-confidential, so it is described
   here rather than reproduced.

At Maya Insights I document a marketing-analytics product built on a BigQuery
warehouse, a Power BI semantic model that pins one governed definition to every
metric, and a conversational MCP layer on top. Most of my writing sits around
the semantic model and the reports built on it, and it spans all four Diátaxis
modes, each aimed at a specific reader:

- **Reference** — interactive glossaries of the model's metrics and dimensions:
  how each is defined, how they interrelate, and which combinations are
  meaningful, tailored to each reader's marketing discipline.
- **Tutorials** — hands-on introductions that get non-technical marketers, many
  of whom had never opened Power BI, comfortable running a basic analysis in our
  report templates.
- **How-to guides** — concise, task-focused guides for the recurring analyses
  each marketing role needs to perform.
- **Explanation** — discipline-level pieces (for example, on the email-marketing
  funnel) that supply the underlying fundamentals the product quietly assumes,
  so the rest of the documentation can land.

Alongside the client-facing material I maintain internal engineering
documentation — our DAX, report-styling and data-modeling conventions, and the
development docs for the MCP server that keep a distributed team's practice
uniform. I also introduced source control to our Power BI practice through the
TMDL text format, which let us track model definitions centrally and retire
stale documentation.

*A sanitized version of one explanatory piece, stripped of sensitive
information, is available on request.*

Open-source contributions
--------------------------

**Diátaxis — documentation typo fix**

A small fix to the documentation of the Diátaxis framework itself — the very
framework I use to structure my own documentation. Modest in size, but it took
me through the project's contribution workflow end to end and, more usefully,
made me read the source material closely.

- Contribution: *(add the link to your pull request)*

.. Add new projects and contributions above as they go live. A useful note for
   each: what it was, who it was for, and what you did.
