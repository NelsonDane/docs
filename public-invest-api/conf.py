import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath(".."))
from conf import *

# -- Project information -----------------------------------------------------
html_title = "Public Invest API Docs"
html_short_title = "Public API Docs"

# -- General configuration ---------------------------------------------------
extensions = extensions + [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
]
print(extensions)
napoleon_google_docstring = True

# Custom function to hide non-private members
# def hide_non_private(app, what, name, obj, skip, options):
#     # if private-members is set, show only private members
#     if name == "Public":
#         return None
#     if (
#         "private-members" in options
#         and not name.startswith("_")
#         and not name.endswith("__")
#     ):
#         # skip public methods
#         print(f"Skipping public method: {name}")
#         return True
#     else:
#         # do not modify skip - private methods will be shown
#         print(f"Showing method: {name}")
#         return None

# # -- Use custom function to hide non-private members -----------------------------
# def setup(app):
#     try:
#         from conf import setup as base_setup
#         base_setup(app)
#     except ImportError:
#         pass
#     app.connect("autodoc-skip-member", hide_non_private)
