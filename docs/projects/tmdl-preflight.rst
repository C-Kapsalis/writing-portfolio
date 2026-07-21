
tmdl-preflight
==============

**An open-source testing and auto-fix suite for Power BI semantic models
saved as text (TMDL/PBIP).** I built the tool in Python (21 rules, five
safe auto-fixers, a CLI, and a pytest plugin) and gave it a documentation
set built just as deliberately: a tutorial, two how-to guides, and a
two-part reference, sized to what a three-command tool actually needs
rather than padded out to a template.

The problem it documents
------------------------

When Power BI projects are saved in their text-based format, the semantic
model becomes a folder of plain files. That means merges, scripts, and
hand edits can produce models that *look* fine and fail on deployment, or
refuse to open at all. A table that lost its ``ref table`` line is not
attached to the model, so Power BI will not open the project; a table
with no partition, an inline ``#table`` entity source that silently
forces a composite model, or a reserved table name like ``Measures``
fails the same way. A duplicated identity tag rejects the import. One
orphan comma in a field parameter takes down every visual that parameter
drives. A bookmark field that says ``"2"`` instead of ``2`` is refused
with a one-line error that names neither the file nor the path.

These defects share a shape: mechanical to detect, expensive to discover
late, and, for a careful subset, mechanical to *repair*. tmdl-preflight
checks for all of them and auto-fixes that subset, always re-checking
from disk afterward so a fixer never gets to vouch for itself. The
project calls this the *imposition pattern*: check, fix, re-check.

How the documentation is structured
-----------------------------------

The docs follow `Diátaxis <https://diataxis.fr>`_, trimmed to what a
single-purpose CLI needs rather than a full four-quadrant traversal:

- **Tutorial**: install, check a fictional bike-shop model that ships in
  the repository, break it on purpose, watch the fixer repair it. The
  reader leaves having seen a full check-fix-re-check cycle.
- **How-to guides**: add a rule of your own, and add or change an
  auto-fix. Each assumes the reader already knows Python and TMDL, and
  starts from the task rather than re-teaching the fundamentals.
- **Reference**: the CLI contract (commands, path resolution, exit codes,
  JSON schema, the full rule catalog, and CI/scoping usage patterns) in
  one page, and the pytest fixture, the Python API, and the design behind
  the check-fix-re-check loop in a second.

That second reference page carries the argument most CLI docs leave out
entirely: not just what each rule checks, but why only five of the
twenty-one rules earn an auto-fixer, and why the other sixteen are
correctly left to a human. A repair earns a fixer only if the failure
mode fully determines the correct repair, it never overwrites
human-authored semantics, it is idempotent, and it is a minimal,
line-level edit. An unbalanced DAX expression, for instance, has
infinitely many valid completions, so no fixer can guess which one the
author meant.

What I'd point a reviewer at
----------------------------

The rule catalog in the reference is the best sample of my reference
writing: tight, tabular, no narrative. The design section that closes
the same page is the best sample of the opposite mode: an argument for
why the tool draws its automation boundary exactly where it does. The
worked example throughout is a fictional bike-shop model, so every code
block in the docs is runnable against the repository's own test
fixtures. The release notes record the pass that mattered most: before
release, the suite ran end to end against several multi-megabyte
production semantic models, hundreds of tables and thousands of
measures, and the rules it sharpened there are named in the notes.

Project links
-------------

- `tmdl-preflight repository on GitHub
  <https://github.com/c-kapsalis/tmdl-preflight>`_: source code, full
  documentation, release notes, and runnable bike-shop example models
  (one clean, one deliberately broken) under ``examples/``.
- `Documentation site
  <https://tmdl-preflight-documentation.readthedocs.io/en/latest/index.html>`_:
  the published docs, on Read the Docs.

The repository ships the project's complete documentation set (``docs/``
plus release notes); this page introduces the project, not the docs
themselves.

*Python 3.10 or later, standard library only; 125 passing tests; MIT
license.*
