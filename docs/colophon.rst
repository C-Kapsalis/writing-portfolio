Colophon — how this site was built
==================================

Per the Write the Docs portfolio guidance, *how* a portfolio is built is
itself a writing sample. So here is this site's own documentation.

The stack
---------

This site is written in **reStructuredText**, built with **Sphinx** using the
**Furo** theme, kept in **Git**, and deployed to **GitHub Pages** by a
**GitHub Actions** workflow that rebuilds and republishes on every push to
``main``. There is no paid hosting anywhere in the pipeline.

Why this stack
--------------

It is the same docs-as-code toolchain used by the teams I want to write for,
so the site is not just a container for samples — it is itself evidence that I
can author in reStructuredText, structure with Sphinx, and publish from CI.

How to reproduce it
-------------------

.. code-block:: console

   $ pip install sphinx furo
   $ sphinx-build -b html docs docs/_build/html   # build locally
   $ python -m http.server -d docs/_build/html     # preview at :8000

Pushing to GitHub, with Pages set to build from GitHub Actions, publishes the
site automatically. The workflow lives in ``.github/workflows/docs.yml``.

Problems solved along the way
-----------------------------

*(Keep a note here of anything you had to figure out — a build warning, a
theme tweak, a Pages configuration step. This section is itself part of the
sample, and reviewers value seeing how you work through friction.)*
