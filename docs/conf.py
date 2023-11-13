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
from os.path import abspath, dirname, join
import sys
sys.path.append(abspath(join(dirname(__file__), "_ext")))
# import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = "Lilith's Throne Mod Documentation"
copyright = '2020, Innoxia and contributors'
author = 'Innoxia'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ltxml",
    "sphinx.ext.graphviz",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    # "sphinx_rtd_theme",
]

primary_domain = None

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# sphinx internationalization
locale_dirs = ['locale/']   # path is example but recommended.
language = "en"
gettext_compact = True     # optional.


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
html_theme = "alabaster"
html_context = {
    'display_github': True,
    'github_user': 'CKRainbow',
    'github_repo': 'lilith-throne-documentation',
    'github_version': 'master',
    'conf_py_path': '/docs/',
}
html_theme_options = {
    'github_user': 'CKRainbow',
    'github_repo': 'lilith-throne-documentation',
    'github_banner': False,
    'github_button': True,
    'github_type': 'star',
    'show_related': True,
    'show_relbars': True,
}
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_baseurl = "https://bicobus.github.io/lilith-throne-documentation/"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

extlinks = {
    'wiki': (
        'https://www.lilithsthrone.com/wiki/doku.php?id=modding_wiki:modding:%s',
        '%s'
    ),
    'ltgithub': (
        'https://github.com/Innoxia/liliths-throne-public/tree/dev/%s',
        '%s'
    )
}
