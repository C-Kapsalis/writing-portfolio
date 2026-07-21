Presentations
=============

**Source Control in Power BI: a BI developer's journey to CI/CD**,
Athens Fabric & Power BI Meetup, March 2025.

A talk arguing that Power BI development deserves to be treated as software
engineering, and that Microsoft's new project format finally makes it possible,
opening a traditionally closed, proprietary Fabric environment up to version
control, review, security, and even AI agents. I built and delivered it the way
I build documentation: a structured, sourced case aimed at moving a community of
practitioners toward a more open and accountable way of working.

What it covered:

- **The problem.** BI developers are "software developers supercharged with
  business knowledge", yet were stuck editing binary ``.pbix`` files, versioning
  by saving copies, and exporting to Excel, with no diffing, no review, no safe
  collaboration.
- **The grounding.** I set the argument on the business-intelligence-systems
  literature (Davenport and Arnott; the finding that roughly 70% of BI projects
  fail to meet expectations without proper foundations) and closed by mapping the
  approach to the DeLone and McLean information-systems success model.
- **Microsoft's "revolutionary trinity".** The PBIP structure with the **TMDL**
  text format (turning binary models into transparent, version-controllable,
  human- and agent-readable folders), Git integration with Power BI Service
  workspaces, and Copilot integration.
- **A metadata-only security model.** Models reference data sources by name
  only, so no production data ever travels inside a file, which satisfies strict
  compliance requirements.
- **The real implementation** at Maya: a shared "universal" core model,
  automated workspace and customer-folder creation via the Power BI API and
  GitHub Actions, a branch → test on a dummy workspace → pull request → merge
  loop, a standardized ``.gitignore``, and Python automations (for example,
  rebinding report visuals straight from ``tmdl`` metadata).
- **An agent-experience outlook.** Because source-controlled Power BI artifacts
  are granular, structured text (JSON plus ``tmdl``), agents can parse and even
  generate reports without proprietary connectors.

`Slides <https://drive.google.com/file/d/1qXqzyBncQq6WssjkwV_XBwAVQ1SbUHTO/view>`_
· `meetup page <https://www.meetup.com/athens-power-bi-meetup-group/events/306218331/>`_
