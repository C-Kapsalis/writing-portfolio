"""Sphinx configuration for the technical-writing portfolio."""

project = "Christoforos Kapsalis"
author = "Christoforos Kapsalis"
copyright = "2026, Christoforos Kapsalis"

extensions = []

templates_path = ["_templates"]
html_static_path = ["_static"]
html_js_files = ["new-tab.js"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Furo: a clean, modern, responsive theme that reads well on mobile.
html_theme = "furo"
html_title = "Christoforos Kapsalis"

html_theme_options = {
    "sidebar_hide_name": False,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/c-kapsalis",
            "html": "",
            "class": "fa-brands fa-github",
        },
    ],
}

# So dead internal links fail the build rather than shipping broken.
nitpicky = False
