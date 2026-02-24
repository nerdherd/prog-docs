# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'prog-docs'
copyright = '2026, NerdHerd'
author = 'NerdHerd'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_favicon = '_static/Nerd.svg'

html_theme_options = {
    "font_family": "'Poppins'",
    "body_text": "#ffffffff",
    "sidebar_text": "#ffffffff",
    "sidebar_header": "#ffffffff",
    "sidebar_link": "#ffffffff",
    "link": "#ffffffff",
    "narrow_sidebar_bg": "var(--darker-navy)",
    "narrow_sidebar_fg": "#ffffffff",
    "narrow_sidebar_link": "#ffffffff",
    "link_hover": "var(--light-blue)",
    "description": "The NerdHerd Programming Documentation",
    "logo": "Nerd.svg",
}