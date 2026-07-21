
tmdl-drift-doctor
=================

**A drift-detection and remediation suite for fleets of Power BI semantic
models — and a full Diátaxis documentation set written alongside the code.**

The problem it solves is one I know from the inside. When a company delivers
analytics as one semantic model per client, all derived from a shared
template, entropy is the default: the template improves, and a dozen client
models each drift a little — an edited measure here, a missing column there,
a table retired months ago still haunting three tenants. tmdl-drift-doctor
turns "are the clients up to date?" from an afternoon of eyeballing diffs
into three commands: ``capture`` a baseline of the template, ``detect``
typed drift findings per model, ``remediate`` by cascading template truth
back out — allowlist-gated, dry-runnable, and recorded in an append-only
audit ledger.

I built it as an open-source Python package (CLI, parser, safe text-surgery
engine, 60 tests over a fictional gym-chain fleet), and its documentation is
not an appendix to the tool — it is half the deliverable, and in places it
led the design. Before
release the suite was also exercised against a production-scale fleet — a
108-table, 614-measure template with three derived client models, ~780
findings — so the claims below are validated, not merely tested.

The documentation
-----------------

The docs follow `Diátaxis <https://diataxis.fr>`_ end to end: a tutorial
that walks a sandbox fleet from first capture to first cascade; how-to
guides for the situations operators actually face (onboarding a model,
cascading a column retirement, recovering from an unwanted remediation,
wiring the detector into CI); and reference pages for the CLI, the
configuration schema, the drift-kind catalog and the ledger format.

The part I am proudest of is the explanation section, built on a simple
editorial rule: **one topic guide per thing the suite looks for.** Every
drift kind — missing objects, expression drift, property drift, extra
objects, and the four retirement kinds down to the surgical
"one row removed from a lookup table that survives" — gets the same
five-part treatment: what it is, how it arises in real fleets, how
detection reasons about it, what remediation does, and — the section most
docs never write — *when not to auto-fix*. Alongside them sit four
operating-principles essays that explain the tool's temperament rather than
its features: why baselines are recaptured the moment the template changes,
why nothing cascades unless an allowlist names it, why deletions require
provenance and how the revival model keeps corrections from erasing
history, and why TMDL is edited as raw text blocks behind write guards —
including the hard-won invariant that a property line must never be
injected into a multi-line DAX expression body.

Writing those guides was not decoration; it was verification. Explaining
*when not to auto-fix* forced design decisions the code then had to honor —
extras on shared tables became advisory-only findings with no remediation
path at all, and the "stale baseline" failure mode described in the
recapture essay became a guard that refuses to run rather than a warning.
That is the working style I keep coming back to: if the explanation cannot
be written cleanly, the behavior is usually wrong.

- **Stack:** Python, Click, pytest; Markdown docs organised with Diátaxis
- **Docs:** 1 tutorial · 4 how-to guides · 4 reference pages · 11
  explanation guides

Project links
-------------

- `tmdl-drift-doctor repository on GitHub
  <https://github.com/c-kapsalis/tmdl-drift-doctor>`_ — source code, full
  documentation, release notes, and a runnable example fleet (a fictional
  gym chain) under ``examples/``.
- `Documentation site
  <https://tmdl-drift-doctor-documentation.readthedocs.io/en/latest/>`_ —
  the published Diátaxis docs, on Read the Docs.

The repository ships the project's complete Diátaxis documentation set
(``docs/`` plus release notes); this page is the showcase, not the docs.
