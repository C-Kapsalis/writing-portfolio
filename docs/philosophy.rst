How I think about documentation
===============================

One question sits under everything I write: *what is the reader trying to do
right now?* Not "what does this feature do," but what need the reader has at
the moment they arrive. Four different needs produce four different kinds of
document, and the discipline is to let each page serve exactly one.

Diátaxis
--------

I structure documentation with `Diátaxis <https://diataxis.fr>`_: tutorials
(learning-oriented), how-to guides (task-oriented), reference
(information-oriented), and explanation (understanding-oriented). The value is
not the four boxes; it is that knowing which one a page is tells you what to
leave out. The most common documentation failure is not being wrong — it is
being correct but *mixed*, so the reader drowns in material meant for a
different need.

Single source of truth
-----------------------

A definition should live in exactly one place, and everything else should link
to it. When the same term is restated in many places, it drifts, and two
readers end up meaning different things by the same word. I treat that as a
governance problem to be enforced in the pipeline, not a discipline problem to
be remembered — an idea I built into a small tool, :doc:`glossctl
<samples/glossctl>`.

Documentation has a second reader now
-------------------------------------

Having built LLM tooling over a data platform, I have watched reference
material become something machines consume too. A muddled reference used to
just frustrate a person; now it degrades every agent built on top of it. The
same discipline that keeps a human from getting lost between modes is what
makes the reference layer clean enough for a machine — which makes good
structure more load-bearing than ever.
