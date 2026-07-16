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

1. Push this repo to GitHub (public).
2. Repo **Settings -> Pages -> Build and deployment -> Source: GitHub Actions**.
3. Every push to `main` rebuilds and republishes automatically.

To serve it at `https://<username>.github.io/`, name the repo
`<username>.github.io`. Any other repo name serves it at
`https://<username>.github.io/<repo>/`.
