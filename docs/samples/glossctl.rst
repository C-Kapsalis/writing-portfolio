glossctl — documenting a tool end to end
========================================

A self-authored command-line tool and its complete documentation set,
written to show how I approach a product's docs from scratch.

**Live docs:** *(add your GitHub Pages URL once published)*
**Source:** *(add your GitHub repo URL)*

The reader
----------

Two audiences, deliberately separated. A newcomer who has never used the tool
and needs to be taught it (the tutorial), and a competent user who arrives
with a specific job to do (the how-to guides). The reference and explanation
serve a third mode of need: looking things up, and understanding *why* the
tool works the way it does.

What the docs had to do
-----------------------

``glossctl`` keeps a documentation set's terminology anchored to a single
source of truth and flags drift. The documentation had to teach the concept,
enable real use, describe the machinery exactly, and argue the philosophy —
without any one page trying to do more than one of those jobs.

Tools
-----

reStructuredText, Sphinx (with autodoc generating the API reference straight
from source docstrings, so it can't drift from the code), the Furo theme, a
Sphinx ``glossary`` directive for canonical terms, Git, and a containerised
Docker build. Published from CI.

How I worked
------------

I structured the set with Diátaxis before writing a word, so every page had a
defined job. On a real team I would pair this with the engineers who own the
tool to get the reference details exactly right, ask a QA reviewer to run the
tutorial start to finish on a clean machine (the only real test of a
tutorial), and have a peer editor check that no page had drifted across modes.

A detail I am proud of: I wired the tool into its own CI, and the check
initially failed because it read a *documented example* of bad input inside a
tutorial code block as if it were real. Fixing that taught me something worth
keeping — a documentation linter has to understand the difference between
prose and code, exactly as a writer does.

What I would improve
--------------------

The explanation page carries a lot of weight; on a larger site I would split
the governance argument from the design rationale so each is discoverable on
its own terms.
