# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Demo"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = "0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",
    "atsphinx.audioplayer",
    "atsphinx.feed",
    "atsphinx.og_article",
    "rst_package_refs.sphinx",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_baseurl = "http://localhost:8002"
