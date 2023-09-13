# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'ML4STS Lab'
copyright = '2022, Sarah M Brown'
author = 'Sarah M Brown'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "ablog",
    'sphinx.ext.intersphinx',
    "sphinx_design",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
]

# "sphinxext.rediraffe",

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*",
        "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md", '_bibliography',
        '_data','_pages','_people','_projects']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
  "github_url": "https://github.com/ml4sts/",
  "twitter_url": "https://twitter.com/ml4sts",
  "search_bar_text": "Search",
  "navbar_end": ["search-field.html", "navbar-icon-links"],
  "footer_items":["copyright",  "sphinx-version",],
  "use_edit_page_button": True,
}


html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "ml4sts",
    "github_repo": "ml4sts.github.io",
    "github_version": "main",
    "doc_path": ".",
}

# html_favicon = "_static/favicon.ico"
html_title = project
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
# html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "publications": ["hello.html"],
    "projects": ["hello.html"],
    "people": ["hello.html"],
    "outreach": ["hello.html"],
    "news": ["hello.html", 'archives.html'],
    "news/**": ['postcard.html', 'recentposts.html', 'archives.html'],
    "blog": ['tagcloud.html', 'archives.html'],
    "blog/**": ['postcard.html', 'recentposts.html', 'archives.html']
}
blog_baseurl = "https://ml4sts.com"
blog_title = "  The Machine Learning for Socio-Technical Systems Lab at University of Rhode Island"
blog_path = "news"
blog_feed_length = 5
fontawesome_included = True
blog_post_pattern = "news/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False

# MyST config
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
#     "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Bibliography and citations
bibtex_bibfiles = ["_static/papers.bib"]

# OpenGraph config
ogp_site_url = "https://ml4sts.com"
# ogp_image = "https://predictablynoisy.com/_static/profile-bw.png"

# Temporarily stored as off until we fix it
# jupyter_execute_notebooks = "off"

# rediraffe_redirects = {
# }

def setup(app):
    app.add_css_file("custom.css")
