Documenting BI reports for marketers
====================================

Most of my documentation work has served one reader: a marketer who has been
given a Power BI report and no data team to stand behind it. This page lays out
the approach I have developed for that reader — what order to teach things in,
where the documentation should live, and what it must never assume. A worked,
end-to-end demonstration of the whole approach is the
:doc:`report template demo <report-template-site>`, an open-source project
whose documentation set follows every principle below.

Assume the tool is scary and the theory is missing
--------------------------------------------------

Two assumptions shape everything else, and both came from being proven wrong
the polite way — by real readers.

The first: a marketing manager once asked me a question that revealed they were
not struggling with my reports at all. They were missing the fundamentals of
their own discipline that my documentation silently took for granted.
Documentation answers the questions its audience is most likely to ask, but
there can be no questions where there is no underlying knowledge to spark them.
So the documentation has to supply that knowledge itself: discipline-level
explanatory pieces — what the email send funnel is, why the list beneath it
matters — sit *alongside* the product documentation, and the reader is routed
through them *before* they ever meet a metric definition.

The second: the first time I documented a semantic model, I published the
documentation in the format I knew best — a Power BI report. The BI-phobic
marketing readers it was written for bounced off the Power BI service
environment before reading a word. The reading surface is part of the writing.
For this audience the documentation (and ideally the product walkthrough
itself) lives on a plain, friendly web page, never inside the BI tool it
explains.

Structure by the reader's question, not the tool's features
-----------------------------------------------------------

I structure this material with a *user-pull* approach: a landing page routes
each reader by discipline — email, paid search, organic social — and within
each discipline every page opens with the marketing question it answers, never
with the feature it happens to describe. An email marketer arriving at the
docs is first shown the funnel view their discipline is read through, and only
then the definitions of the metrics that measure it.

The reference layer is a governed glossary: every metric and dimension gets
exactly one canonical definition, in exactly one place, and every
audience-facing page links back to it rather than restating it. Click-through
rate and click-to-open rate are each defined once — which is the only reliable
way to stop two teams arriving at the same meeting with different numbers
bearing the same name. The glossary also carries a kind of negative knowledge
that BI documentation usually omits: which dimension–metric combinations are
semantically valid, and which produce a number that means nothing. Mapping the
meaningless pairs, and keeping them out of every presentation, prevents the
wrong conclusions before they are drawn.

Teach by doing, starting from blank
-----------------------------------

For this reader, the tutorial cannot be a tour of a finished dashboard —
a finished dashboard is precisely the thing they do not yet understand. The
tutorial starts from a *blank* report template: empty selectors, an empty
canvas. The reader picks a date axis, a legend, a first set of email metrics,
and watches the plot and the table assemble themselves. Then they save what
they built as a bookmark, switch to a different one, and come back — and in
that round trip they learn, in their hands rather than in prose, what a
metric, a dimension, and a bookmark actually *are*: a bookmark is nothing more
than a saved pre-selection that answers one recurring marketing question.

The how-to guides then cover the recurring tasks of the role, and they are
allowed to branch on what the data shows: check deliverability against the
benchmarks first; if it is healthy, go read the click; if the list is eroding,
fix that before anything else. A guide that pretends every reader's data looks
the same is a guide that abandons half of them at the first fork.

The shape underneath
--------------------

Readers of :doc:`my approach page <../approach>` will recognise the Diátaxis
frame underneath all of this — explanation supplying the missing theory,
reference as the governed glossary, tutorials that teach by doing, how-to
guides for the tasks of the role. What this page adds is the calibration for
one specific, underserved reader: the non-technical marketer. For them the
order of arrival matters (explanation first), the surface matters (never the
BI service), and the glossary must govern, not merely describe.

The :doc:`report template demo <report-template-site>` puts all of it in one
place: a two-page web app whose first page is the report template itself and
whose second page *is* the tutorial — blank selectors, guided steps, a saved
bookmark — with the four topic guides and the glossary built into the same
friendly surface.

Project links
-------------

- `report-template-site repository on GitHub
  <https://github.com/c-kapsalis/report-template-site>`_ — the demo's source
  code, full documentation, and release notes.

The demo project ships its complete Diátaxis documentation set (``docs/``
plus release notes) in its repository; this page describes the approach, and
the :doc:`showcase page <report-template-site>` describes the project — the
docs live with the project.
