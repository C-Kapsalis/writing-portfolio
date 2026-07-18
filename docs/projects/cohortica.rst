Cohortica: restructuring a blog into an interview-prep product
==============================================================

Cohortica began as my marketing-diagnostic web app — two deterministic engines
that read signals and return a diagnosis. This page is about its second life:
turning several dozen discipline articles I had written into a free,
open-source interview-prep tool for marketing roles. No prose was harvested
into a "blog archive" page; the corpus was *restructured* — new unit of
content, new information architecture, new reader. It is the most explicit
content-strategy exercise in this portfolio, and I treat it as technical
writing end to end: the source material was expert knowledge, the deliverable
is a structure a stranger can act on.

One reader, one recurring situation
-----------------------------------

The original articles served a marketer trying to read their own account. The
restructure serves a sharper situation: a candidate with an interview next
week. That reader does not want 4,000-word explanatory pieces; they want the
discipline's reasoning, compressed, in the order a practitioner would apply
it, with the questions they will actually face. Naming that situation decided
everything downstream — what to cut, what to keep, and what shape the surviving
knowledge should take.

The unit of content: the playbook
---------------------------------

Every article was condensed into a *playbook* of 300–600 words with a fixed
anatomy: the single marketing question the topic answers, the framework a
practitioner uses to read it, the metrics that matter paired with the naive
misreading of each, and three to five realistic interview questions — each
answered not with a script but with how a strong candidate reasons through it.
The fixed anatomy is the point. Fifty-nine playbooks written to one template
read as one system, can be reviewed against one checklist, and teach the
reader where to look before they have read a word.

The compression was also an editing discipline. The source articles carried
product framing — sections on how a particular analytics tool streamlines each
analysis — and worked examples built on named fictional brands. All of it was
stripped: the tool becomes generic knowledge, the personas become anonymous
worked examples, and the piece keeps only what survives a change of employer,
platform, or decade. What remains is the part of the original writing that was
always the real value: benchmarks, reading orders, and traps.

Information architecture as the product
---------------------------------------

The architecture is three levels deep and deliberately boring: a discipline
index, a hub per discipline that lists its playbooks *in reading order*, and a
page per playbook. The reading order does quiet work — each discipline opens
with its overview and its "read your account in order" roadmap, so the hub
itself teaches the sequence an audit follows. The two original diagnostics
survived intact as practice apparatus: case questions in marketing interviews
are diagnosis questions, and a deterministic engine that maps signals to
states to actions is a rehearsal machine for exactly that move. The dead ends
are honest too: an unknown route, discipline or playbook slug lands on a
not-found page that says what happened, why it likely happened, and where to
go next — never a bare 404 — and the whole surface is built to be accessible
(semantic landmarks, labelled controls, visible keyboard focus, a skip link,
WCAG AA contrast).

The contribution story is structural too. Playbooks are markdown files with a
three-line frontmatter block; a build-time loader picks up anything dropped
into a discipline folder. Adding content requires no code, which let me write
the contributor documentation the way I prefer: a how-to guide that is
genuinely one file long.

Docs as part of the artifact
----------------------------

The repository ships with its own documentation set — two tutorials (prep for
an interview with the tool; run it locally), three how-to guides (add a
playbook, add a discipline, deploy), and reference pages for the content
schema, routes, and component map — all stemming from a README that doubles as
a live content map of disciplines and playbook counts. A knowledge product
that asks strangers to contribute has to document itself to the same standard
it documents its subject; the CONTRIBUTING guide carries the tone rules and
the review checklist that keep fifty-nine voices reading as one.

Project links
-------------

- `Live site <https://cohortica-studio.vercel.app/>`_ — the playbooks and the
  two diagnostics, running in the browser.
- `cohortica repository on GitHub
  <https://github.com/c-kapsalis/cohortica>`_ — source code, the playbook
  corpus, full documentation, and release notes.

The repository ships the project's full documentation set (``docs/`` plus
release notes), organised with Diátaxis; this page is the showcase, not the
docs.
