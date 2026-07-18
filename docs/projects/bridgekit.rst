
bridgekit
=========

*An agentic framework for prototyping three-party tools — or, what happens
when an essay becomes a system prompt.*

For people building not to make money, but to build bridges.

Most of my projects have gone the usual direction: build the thing, then
write about it. bridgekit ran the other way. It started as a piece of
writing — :doc:`Integration over destination <../integration-over-destination>`,
the essay I wrote after CleanLeaf, arguing that tools fail when they are
built as destinations instead of meeting people where their attention
already lives. bridgekit is that essay made executable: the text, adapted
but kept in its own voice, is the literal system prompt that governs every
agent in the framework. If you disagree with what the framework designs,
the place to argue with it is the essay.

What it does
------------

CleanLeaf's design move was that one action — photographing a meal — paid
three parties at once: the student built a habit, the dorm got a
leaderboard, and the institution got a line in the ESG report it already
had to produce. Same data point, three payoffs, no new app. bridgekit
generalizes that move into a pipeline you can point at any domain:
employee wellness, community composting, team knowledge sharing.

Three agents (built on Hugging Face's smolagents, over a free-by-default
OpenRouter model) run in sequence, each inheriting the philosophy prompt:

- **uncover** interviews the domain: who are the individual, the community,
  and the institution here; what does each want; where do their incentives
  collide; and — the essay's question — where does their attention already
  live?
- **reconcile** searches for the *bridge action*: one lightweight recurring
  action that closes the incentive loop for all three parties, on a surface
  they already inhabit, whose data exhaust becomes the institution's
  reporting. It must publish the gives/gets table and name the weak link
  honestly.
- **prototype** emits a runnable single-file HTML demo of the loop plus a
  ``SPEC.md`` — deliberately framed as a starting point for handing to a
  coding agent, not a product. The framework refuses, on principle, to
  pretend it can generate the real thing: a real bridge tool lives inside
  chat platforms and existing rituals, and a generator can only fabricate
  destinations.

There is a CLI for the terminal crowd and a small browser GUI for everyone
else — paste a free OpenRouter key, name a domain, watch the three stages
stream, download your prototype. The CLI follows the Heroku CLI style
guide's conventions — data on stdout, status on stderr, flags over
positional arguments — with its two deliberate deviations named in the
reference; the GUI keeps its controls keyboard-reachable, ARIA-labelled and
visibly focused.

The technical-writing thread
----------------------------

This is the project where the writing did not document the software — it
*became* the software. The essay is the system prompt; the pipeline's
output contract is itself a documentation set (a research report, a design
brief, a spec); and the whole thing ships with full Diátaxis docs, because
a framework whose thesis is "meet people where they are" had better apply
that to its own readers. The other thread is honesty of scope, which I
think of as a writer's virtue before an engineer's: every prototype carries
a footer saying what it is not, and the spec's final section lists exactly
what was left out and why.

MIT-licensed, Python + smolagents, 36 tests, with the GUI deployable to
Vercel as a static page. CleanLeaf remains the worked example throughout
the docs — the bridge the framework keeps pointing back to.

Project links
-------------

- `Live GUI <https://bridgekit-puce.vercel.app/>`_ — the browser front end;
  paste your own OpenRouter key (it stays in your browser) and run the pipeline.
- `bridgekit repository on GitHub
  <https://github.com/c-kapsalis/bridgekit>`_ — source code, full
  documentation, and release notes.

The repository ships the project's complete Diátaxis documentation set
(``docs/`` plus release notes); this page is the showcase, not the docs.
