"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

-- Project information -----------------------------------------------------
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""

# Basic project configuration
project = "dynamic-library"
copyright = "2025, Filipe Laíns"  # noqa: A001
author = "Filipe Laíns"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",  # Auto-generate API documentation
    "sphinx.ext.viewcode",  # Add links to source code
    "sphinx.ext.intersphinx",  # Link to other Sphinx documentation
    "sphinx.ext.coverage",  # Check documentation coverage
    "sphinx.ext.autosummary",  # Generate summary tables
    "sphinx.ext.napoleon",  # Support for math equations
    "numpydoc",  # Enhanced NumPy documentation support
    "myst_parser",  # For parsing Markdown files
]
html_theme = "furo"
templates_path = ["_templates"]

# autodoc
autodoc_typehints = "description"  # Put type hints in the description
autodoc_member_order = "bysource"  # Order members by source order
autodoc_default_options = {
    "members": True,
}
autoclass_content = "class"  # Include both class and module docstrings

# autosummary
autosummary_generate = True  # Generate stub pages for API

# intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
}

# numpydoc
numpydoc_class_members_toctree = False

# Myst
myst_heading_anchors = 4
