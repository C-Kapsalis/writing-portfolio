
pbip-model-forge
================

*Prototype a Power BI data model in chat — with real data loaded — then hand
the diagram to your data engineers as a spec.*

For the domain experts who are given the fewest data resources of anyone.

The mission comes first
-----------------------

Most of my tools start from a defect and work outward. This one starts from a
conviction about the moment we are in. In the AI age, the asset that keeps its
value is **domain expertise** — the person who actually understands the
business, its customers, and what moves the numbers. And yet the teams that
hold that expertise — marketing, finance, operations, sales — are routinely
handed the *fewest* data resources and the least data-engineering support.
Their sharpest questions sit in a backlog; their insight never reaches a model.

pbip-model-forge is built to close that gap. It lets a domain expert spec and
stand up a *real* data model themselves, in plain conversation — capturing the
tables, relationships and measures their questions actually need — so they can
extract insight, justify their priorities, and express their value to
stakeholders in concrete terms, no longer blocked on scarce data resources to
prove the point. I lead the documentation with that framing because it is the
reason the project exists; the engineering underneath is in service of it.

What it does
------------

You say *"create a sample data model for a hospital"* — or for subscription
analytics, or a delivery fleet. Claude invents plausible tables, columns and
sample data, and the repo turns that into a **real, openable PBIP**: a Power BI
semantic model with the sample data *physically loaded*, plus a blank report,
validated so that Power BI Desktop will actually open it. Because the data is
really there, relationships resolve, measures compute, and the diagram view is
populated — so the model is not a drawing of a model, it is one.

The skill workflow
------------------

This is a **Claude Code skill-based product**, and the skill instructions are
where much of the writing lives — the same move as an earlier project of mine,
where the prose *is* the software rather than describing it. Two skills split
the work along a clean seam:

- **create-sample-model** drives the first pass: domain description in, a spec
  dict assembled, a full PBIP written to disk (``build_pbip(spec, out_dir)``
  produces the ``.pbip`` plus its ``.SemanticModel`` and a blank ``.Report``).
- **validate-and-expand** owns the iteration loop. "Add a promotions
  dimension", "add a margin measure", "make it monthly" — the model
  regenerates from the single spec and re-validates, so it stays openable as it
  grows rather than drifting into a state Desktop rejects.

The will-it-open engineering
----------------------------

A hand-authored PBIP is unforgiving: get one of about nine structural details
wrong and Power BI Desktop simply **refuses to open the project**, often with
an opaque error like *"Sequence contains no elements"* or *"A composite model
cannot be used with entity based query sources"*. Each of those was hit for
real and is now encoded into the builder, and written up in a *will-it-open
playbook* — an artifact checklist that walks every file and every check in
turn, so the knowledge is documented, not buried in code.

The single trickiest part is loading real data with no external source: Power
BI stores manually entered data as a compressed **raw-DEFLATE + base64 blob**
that must be byte-identical to what Desktop writes. The repo's encoder is
verified byte-for-byte against a model proven to open, with a worked example in
its own encoding guide and a test that locks it to Power BI's golden byte
layout. Validation is not self-attested: every generated model is gated by
:doc:`tmdl-preflight <tmdl-preflight>`, and nothing is called "openable" until
``tmdl-preflight check`` reports **0 errors**.

The deliverable is a spec, not a report
----------------------------------------

The generated report is intentionally **blank** — ``.platform`` plus
``definition.pbir``, no pages, no visuals — because the value is the model:
tables, types, keys, relationships and measures, the thing a data engineer
actually needs. Presented as a star-schema diagram alongside the PBIP, it
becomes the hand-off artifact. Give it to your data engineers to build the
warehouse to exactly that shape, or hand it to a data-engineering skill and
have the pipeline generated the same way. The domain expert defines *what the
business needs to measure*; the plumbing follows.

Project links
-------------

- `pbip-model-forge repository on GitHub
  <https://github.com/c-kapsalis/pbip-model-forge>`_ — the two Claude Code
  skills, the byte-exact entered-data encoder, the builder, and the docs (the
  vision, the will-it-open artifact checklist, and the entered-data encoding
  guide).

*Python ≥ 3.9, standard library only to build a model; requires the
tmdl-preflight validator, installed separately; MIT license.*
