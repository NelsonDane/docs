# -- Project information ------------------------------------------------------
project = "NelsonDane Docs"
copyright = "2025, Nelson Dane"
author = "Nelson Dane"
html_title = "Nelson Dane Docs"
html_short_title = "Docs"

# -- General configuration ----------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx_new_tab_link",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv", "**/.venv/**", "**/site-packages/**",]

language = "en"

# -- Options for HTML output --------------------------------------------------
html_theme = "furo"  # or another theme you like
html_static_path = ["_static"]
html_theme_options = {
    "navigation_with_keys": True,
}

# Custom function to hide non-private members
def hide_non_private(app, what, name, obj, skip, options):
    # if private-members is set, show only private members
    if name == "Public":
        return None
    if (
        "private-members" in options
        and not name.startswith("_")
        and not name.endswith("__")
    ):
        # skip public methods
        return True
    else:
        # do not modify skip - private methods will be shown
        return None

def setup(app):
    try:
        from conf import setup as base_setup
        base_setup(app)
    except ImportError:
        pass
    app.connect("autodoc-skip-member", hide_non_private)
