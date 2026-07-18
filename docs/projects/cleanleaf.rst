
CleanLeaf — from pitch prototype to documented open source
==========================================================

*A community wellness platform: the prototype behind our Whitman Dean's
Sustainability Challenge pitch, refined into an open-source project and
documented end to end with Diátaxis.*

CleanLeaf is a B2B2C concept my team pitched at Syracuse University's Whitman
School Dean's Sustainability Challenge in 2026, where it won **2nd Place
Judge's Favorite and a $5,000 award**. Institutions — universities,
corporations — run healthy-eating challenges that reach people through the
group chats they already use (WhatsApp, Teams, Slack): you photograph a meal,
an AI engine scores it against the NOVA food-classification system, and your
progress is gamified within your community through leaderboards and streaks.
Every logged meal also becomes a data point in the institution's ESG and SDG
reporting. I owned the business model and pricing and built the interactive
prototype — a simulated WhatsApp challenge with a live camera-and-scoring
loop, plus the institution-side dashboard.

Like most things built for a pitch, the prototype was written for one demo
day. This project is what came after: taking that hackathon-grade codebase
and making it something a stranger could clone, run, read, and extend.

The refinement pass
-------------------

The code work was a hardening pass, not a redesign — the product and its look
stayed exactly as pitched. What changed is everything around it: dead code
and an entire unused scoring table went; repeated UI became components;
scattered magic values became a single seed-data module, so staging the demo
for a different institution means editing one file; and the pitch deck's
palette was made accessible at the source — its muted gold fell below the
WCAG AA contrast ratio as text on light backgrounds, so the palette gained a
darker shade for exactly that use. The
most important change was the **zero-key demo mode**: the meal scorer now
degrades from a live vision model to a clearly labelled stub whenever no API
key is configured, so ``npm install && npm run dev`` on a fresh clone
completes the full loop — nudge, photo, score, leaderboard — with no accounts
and no backend. A working first run is the difference between a repository
and a screenshot.

The documentation
-----------------

The docs are structured with `Diátaxis <https://diataxis.fr>`_, and the
project is small enough to show the framework working at honest scale — a
prototype does not need a documentation empire, it needs each mode doing its
one job:

- a **tutorial** that walks a newcomer through the complete demo loop, from
  install to watching their points move the leaderboard;
- **how-to guides** for the three tasks a motivated cloner actually has:
  deploying to Vercel, swapping the stub scorer for a real model (the scorer
  contract is documented, so any vision backend that honors it drops in), and
  reconfiguring the institution and challenge;
- **reference** pages for the routes, components, data shapes, and
  environment variables;
- and two **explanation** pieces, which carry the part I care about most: one
  on the three-party design — how a single meal photo pays the individual (a
  habit rep), the community (leaderboard points), and the institution (an SDG
  data point) at once — and one adapting my *integration over destination*
  essay (:doc:`the blog post </integration-over-destination>`) into an
  architectural explanation of why CleanLeaf lives in group chats instead of
  being an app.

That last piece closes a loop that runs through my whole practice: the
principle that shaped the product — meet people where their attention already
is, rather than building a destination and hoping they come — is the same
user-pull instinct that drives good documentation. Documenting CleanLeaf
properly was a way of applying the product's own philosophy to the product.

Project links
-------------

- `cleanleaf repository on GitHub
  <https://github.com/c-kapsalis/cleanleaf>`_ — source code, full
  documentation, and release notes.
- `Whitman newsroom coverage of the 2026 Dean's Sustainability Challenge
  <https://whitman.syracuse.edu/about/newsroom/whitman-news/news-detail/2026/05/07/2026-whitman-dean-s-sustainability-challenge-showcase-highlights-student-innovation-inspired-by-u.n.-sustainable-development-goals>`_.

The repository ships the project's complete Diátaxis documentation set
(``docs/`` plus release notes); this page is the showcase, not the docs.
