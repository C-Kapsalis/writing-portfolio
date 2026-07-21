
tmdl-preflight
==============

**An open-source testing and auto-fix suite for Power BI semantic models
saved as text (TMDL/PBIP).** I built the tool in Python — 21 rules, five
safe auto-fixers, a CLI and a pytest plugin — and gave it a documentation
set built just as deliberately: fourteen explanation guides, a tutorial,
four how-to guides and a two-part reference, written as one coherent body
rather than an afterthought.

The problem it documents
------------------------

When Power BI projects are saved in their text-based format, the semantic
model becomes a folder of plain files — which means merges, scripts and
hand edits can now produce models that *look* fine and fail on deployment,
or refuse to open at all. A table that lost its ``ref table`` line is not
attached to the model, so Power BI will not open the project; a table with
no partition, an inline ``#table`` entity source that silently forces a
composite model, or a reserved table name like ``Measures`` fails the same
way. A duplicated identity tag rejects the import. One orphan comma in a
field parameter takes down every visual that parameter drives. A bookmark
field that says ``"2"`` instead of ``2`` is refused with a one-line error
that names neither the file nor the path.

These defects share a shape: mechanical to detect, expensive to discover
late, and — for a careful subset — mechanical to *repair*. tmdl-preflight
checks for all of them and auto-fixes that subset, always re-checking from
disk afterwards so a fixer never gets to vouch for itself (the project
calls this the *imposition pattern*: check → fix → re-check).

How the documentation is structured
-----------------------------------

The docs follow `Diátaxis <https://diataxis.fr>`_ strictly, and the split
did real design work:

- **Tutorial** — install, check a fictional bike-shop model that ships in
  the repository, break it on purpose, watch the fixer repair it. The
  reader leaves having seen a full check → fix → re-check cycle.
- **How-to guides** — run in CI (read-only, ``--strict``), run inside
  pytest, run only the auto-fixable rules, add a custom rule. Each starts
  from a task, not a feature.
- **Reference** — the CLI contract (commands, path resolution, exit
  codes, JSON schema) and a rule catalog: one entry per rule with id,
  severity, fixability, scope, and a link to its explanation.
- **Explanation** — the part I care about most: **one guide per
  precaution**. Each explains the data-modeling pitfall itself — why it
  arises in text-based workflows, what it costs, and why the automatic
  repair is safe (or, just as deliberately, why no repair is offered).

That last constraint — every rule must justify itself in prose — turned
out to be a quality gate on the *tool*. Writing "why is this fix safe?"
for each fixer forced a written safety contract (a fixer only repairs what
its rule's failure mode describes, is idempotent, never overwrites
human-authored semantics), and two candidate fixers failed the essay and
stayed check-only.

Excerpts
--------

From the explanation of duplicate lineage tags, on why regeneration is a
safe repair:

    Regenerating a lineage tag is safe precisely because of what a
    duplicate means: **a duplicated tag carries no usable identity
    anyway.** The deployment target cannot use it to track either object,
    so replacing the *second* occurrence with a fresh ``uuid4`` loses
    nothing — it simply gives the copied object the new identity it should
    have had from the start.

From the explanation of bookmark visual references, on why that rule
deliberately has *no* fixer:

    A dangling reference has three legitimate resolutions, and they point
    in different directions: the visual was deleted **on purpose** →
    delete or re-author the bookmark; the visual was rebuilt → retarget
    the reference to the new name; the deletion was the mistake → restore
    the visual. Choosing requires knowing why the visual disappeared —
    intent the files do not record.

From the design guide on the imposition pattern, the sentence the whole
tool hangs on:

    The run is clean only if the **re-check** is clean. … Auto-repair can
    therefore never *mask* a defect — the worst it can do is fail to
    remove one, exactly as if it did not exist.

What I'd point a reviewer at
----------------------------

The 21 explanation-linked rule entries in the reference are the
best sample of my reference writing (tight, tabular, no narrative), and
the twelve precaution guides are the best sample of the opposite mode —
each one argues a position about a pitfall rather than describing a
feature. The worked example throughout is a fictional bike-shop model, so
every code block in the docs is runnable against the repository's own test
fixtures. And the release notes record the pass that mattered most: before
release, the suite was run end to end against several multi-megabyte
production semantic models — hundreds of tables, thousands of measures —
and the rules it sharpened there are named in the notes.

Project links
-------------

- `tmdl-preflight repository on GitHub
  <https://github.com/c-kapsalis/tmdl-preflight>`_ — source code, full
  documentation, release notes, and runnable bike-shop example models
  (one clean, one deliberately broken) under ``examples/``.
- `Documentation site
  <https://tmdl-preflight-documentation.readthedocs.io/en/latest/index.html>`_
  — the published Diátaxis docs, on Read the Docs.

The repository ships the project's complete Diátaxis documentation set
(``docs/`` plus release notes); this page is the showcase, not the docs.

*Python ≥ 3.10, standard library only; 125 passing tests; MIT license.*
