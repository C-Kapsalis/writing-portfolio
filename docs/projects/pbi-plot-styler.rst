
pbi-plot-styler
===============

**A Power BI reporting template you can argue for, with a formatter that
enforces it, documented end to end.** pbi-plot-styler is a small open-source
Python CLI that makes Power BI combo charts presentation-ready: it reads the
measures a semantic model declares in its *field-parameter* tables and
deterministically rebuilds every chart's line color, data labels and
data-label backgrounds, so that any metric anyone adds to the model comes out
styled for a deck with one command. I built the tool and its documentation
together. Its central claim, that per-measure formatting in Power BI is a
derived artifact that should be regenerated from the model and never
maintained by hand, is argued in prose as deliberately as it is enforced in
code.

The documentation is deliberately lean and deliberately Diátaxis-shaped, one
document per reader need rather than one per feature:

- **A README that evangelizes rather than lists.** Most CLI READMEs open
  with installation; this one opens with a failure mode, the twenty-page
  report where every page is the same chart with a different measure, and
  argues for a pattern: declare your dimensions and measures in three field
  parameters, drive one combo-chart page from slicers and bookmarks, and let
  a tool own the formatting. The CLI is positioned as the last mile of a
  template, not as the product.
- **One tutorial** (*Getting started*) that walks a fictional
  specialty-coffee roastery from an empty model to styled charts: the three
  field-parameter tables as ready-to-paste TMDL, the combo-chart page, a
  dry-run diff, the apply, and the idempotent re-run that proves the tool
  safe to habituate.
- **One reference page** for the CLI: every argument, option, and config key
  with its default; the exact JSON properties the tool rewrites, plus the
  guarantee that everything else in the file is preserved byte for byte down
  to line endings and the end-of-file convention; the exit codes, including
  the dry-run drift code that turns the style guide into a CI check; and why
  formatting must be enforced by regeneration rather than discipline, folded
  in as reference sections (CI usage, brand palettes, the one Power BI quirk
  that makes a shared measure catalog worth naming) rather than spun into
  standalone pages a three-flag tool does not need.

The project doubles as a demonstration of a documentation belief of mine:
that a tool with a strong opinion deserves documentation sized to its
surface, not to a template. Two documents and a README cover the whole
tool; nothing is written twice, and nothing is split into its own page
just because a bigger project would have split it.

Project links
-------------

- `pbi-plot-styler repository on GitHub
  <https://github.com/c-kapsalis/pbi-plot-styler>`_: source code, full
  documentation, and release notes.
- `Documentation site
  <https://app.readthedocs.org/projects/pbi-plot-styler-documentation/>`_:
  the published docs, on Read the Docs.

The repository ships the project's full documentation set (``docs/`` plus
release notes), organized with Diátaxis; this page introduces the
project, not the docs themselves.

*Python ≥ 3.10; 30 passing tests; MIT license.*
