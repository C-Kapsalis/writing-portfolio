Projects
========

The technical-writing work I can point to, grouped by kind. My open-source
contributions are still few — a single documentation fix so far, with more on
the way. My most substantial public piece is a conference talk on bringing
source control and CI/CD to Power BI. And a personal teaching project is in
progress. A larger body of professional documentation, written around the
Power BI semantic models and reports at Maya Insights, is client-confidential,
so it is described here rather than shown.

Open-source contributions
--------------------------

**Diátaxis — documentation typo fix.** A small fix to the documentation of the
Diátaxis framework itself — the very framework I use to structure my own
documentation. Modest in size, but it took me through the project's
contribution workflow end to end and, more usefully, made me read the source
material closely.
`Pull request #164 <https://github.com/evildmp/diataxis-documentation-framework/pull/164>`_.

*Next: contributions through the Canonical Open Documentation Academy and to
open-source projects in my own domain, such as PyMC-Marketing.*

Presentations
-------------

**Source Control in Power BI: a BI developer's journey to CI/CD**
— Athens Fabric & Power BI Meetup, March 2025.

A talk arguing that Power BI development deserves to be treated as software
engineering, and that Microsoft's new project format finally makes it possible —
opening a traditionally closed, proprietary Fabric environment up to version
control, review, security, and even AI agents. I built and delivered it the way
I build documentation: a structured, sourced case aimed at moving a community of
practitioners toward a more open and accountable way of working.

What it covered:

- **The problem.** BI developers are "software developers supercharged with
  business knowledge", yet were stuck editing binary ``.pbix`` files, versioning
  by saving copies, and exporting to Excel — with no diffing, no review, no safe
  collaboration.
- **The grounding.** I set the argument on the business-intelligence-systems
  literature (Davenport and Arnott; the finding that roughly 70% of BI projects
  fail to meet expectations without proper foundations) and closed by mapping the
  approach to the DeLone and McLean information-systems success model.
- **Microsoft's "revolutionary trinity".** The PBIP structure with the **TMDL**
  text format (turning binary models into transparent, version-controllable,
  human- and agent-readable folders), Git integration with Power BI Service
  workspaces, and Copilot integration.
- **A metadata-only security model.** Models reference data sources by name
  only, so no production data ever travels inside a file — which satisfies strict
  compliance requirements.
- **The real implementation** at Maya: a shared "universal" core model,
  automated workspace and customer-folder creation via the Power BI API and
  GitHub Actions, a branch → test on a dummy workspace → pull request → merge
  loop, a standardised ``.gitignore``, and Python automations (for example,
  rebinding report visuals straight from ``tmdl`` metadata).
- **An agent-experience outlook.** Because source-controlled Power BI artifacts
  are granular, structured text (JSON plus ``tmdl``), agents can parse and even
  generate reports without proprietary connectors.

`Slides <https://drive.google.com/file/d/1qXqzyBncQq6WssjkwV_XBwAVQ1SbUHTO/view>`_
· `meetup page <https://www.meetup.com/athens-power-bi-meetup-group/events/306218331/>`_

Personal projects
-----------------

**Cohortica — a marketing diagnostic engine** *(live).* At heart this is a
documentation project: a body of how-to guidance for readers who already have
the data picture of their marketing but lack the expertise to act on it. Two
free diagnostics drive it — a **funnel diagnostic** (say whether acquisition,
activation, retention or order value is up, flat or down, and it returns the
likely underlying problem and the actions to take) and a **brand strategy
diagnostic** (a 3C-based read on relevance, defensibility and strategic fit).
You feed in the signal; it returns a diagnosis and a prescribed set of steps —
in effect, situation-triggered how-to guides — backed by a knowledge base of
explanatory articles. It is the technical writer's core task turned into a
product: take expert knowledge, structure it around the reader's need, and make
it something a non-expert can act on. I designed the diagnostic logic, wrote the
guidance, and built the site.
`cohortica.studio <https://www.cohortica.studio/>`_

**CleanLeaf — a community wellness platform** *(Whitman Dean's Sustainability
Challenge, 2026).* A B2B2C concept my team pitched at Syracuse University's
Whitman School: institutions run healthy-eating challenges that reach people
through the group chats they already use (WhatsApp, Teams, Slack) — you
photograph a meal, an AI engine scores it, and progress is gamified within your
community. It won **2nd Place Judge's Favorite and a $5,000 award**. I owned the
business model and pricing and built the dashboard prototype. The
technical-writing thread runs through it twice: the *integration over
destination* principle behind it is the same user-pull instinct that drives good
documentation — meet the reader where their attention already is rather than
building a destination and hoping they come (I wrote about it in
:doc:`this post <integration-over-destination>`); and the piece I owned that I
care about most was information design — turning thousands of individually
logged meals into automated ESG and SDG reports an institution can actually
read, instead of compiling them by hand.
`Whitman newsroom <https://whitman.syracuse.edu/about/newsroom/whitman-news/news-detail/2026/05/07/2026-whitman-dean-s-sustainability-challenge-showcase-highlights-student-innovation-inspired-by-u.n.-sustainable-development-goals>`_
· `our presentation <https://drive.google.com/file/d/1S4yfOQNPecb3L74qiQq3l061scfQ5MdF/view?usp=sharing>`_.

**Marketing Analytics Starter Kit** *(in progress).* A free, self-serve template
that helps junior marketers adopt a data-driven perspective rooted in marketing
fundamentals. Users paste campaign exports into a Google Sheet, connect it to a
Looker Studio report, and the documentation ties every metric back to the idea
it serves — the funnel, unit economics, brand versus generic demand. It is
documented end to end with Diátaxis, using a fictional specialty-coffee brand as
the worked example; the first module covers paid search.

*Link to follow once the report and docs are published.*

Copywriting
-----------

.. Add published copywriting and editorial work here — for example PR pieces
   published in FreshPlaza, the company blog you launched, LinkedIn thought
   leadership, and email campaigns.

Blog posts
----------

**Integration over destination.** Why wellness programs — and most tools — fail
when they build new destinations and expect people to come, instead of meeting
people where their attention already lives; the thinking behind CleanLeaf,
generalised to marketing and product design.
:doc:`Read the post <integration-over-destination>`.

Fiction
-------

.. Add fiction here — short stories or other creative writing that shows voice
   and range. Keep it clearly secondary to the domain-focused work above.

Professional documentation — Maya Insights
-------------------------------------------

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
  of whom had never opened Power BI, comfortable running a basic analysis.
- **How-to guides** — concise, task-focused guides for the recurring analyses
  each marketing role needs to perform.
- **Explanation** — discipline-level pieces (for example, on the email-marketing
  funnel) that supply the underlying fundamentals the product quietly assumes.

Alongside the client-facing material I maintain internal engineering
documentation — our DAX, report-styling and data-modeling conventions, and the
development docs for the MCP server that keep a distributed team's practice
uniform.

*A sanitized version of one explanatory piece, stripped of sensitive
information, is available on request.*

.. toctree::
   :hidden:

   integration-over-destination
