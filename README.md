# Technical-writing portfolio

Source for my technical-writing portfolio, written in reStructuredText, built
with [Sphinx](https://www.sphinx-doc.org/) + [Furo](https://pradyunsg.me/furo/),
and deployed free to GitHub Pages via GitHub Actions.

## Build locally

```console
pip install -r requirements.txt
make serve   # builds and serves at http://localhost:8000
```

## Publish (free)

1. Create a **new** public repo named `writing-portfolio` (any name works;
   it becomes part of the URL).
2. Push this project to it.
3. Repo **Settings -> Pages -> Build and deployment -> Source: GitHub Actions**.
4. Every push to `main` rebuilds and republishes automatically.

The site is served at `https://c-kapsalis.github.io/writing-portfolio/`,
sitting alongside the existing `c-kapsalis.github.io` user site without
conflict. (Sphinx uses relative links, so the subpath works with no config
change.)
