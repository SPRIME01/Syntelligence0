# docs/source/conf.py

# Add type annotations
extensions: list[str] = []
exclude_patterns: list[str] = ["_build", "Thumbs.db", ".DS_Store"]

# Define the author
author: str = "Samuel Prime"  # Replace with your name

# Define the master_doc
master_doc: str = "index"  # Replace with the name of your master document

# Other configurations...

# The name of the Pygments (syntax highlighting) style to use.
pygments_style: str = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos: bool = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme: str = "furo"

# A list of paths that contain custom static files (such as style sheets)
html_static_path: list[str] = ["_static"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename: str = "SphinxDoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements: dict[str, str] = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents: list[tuple[str, str, str, str, str]] = [
    (master_doc, "Sphinx.tex", "Sphinx Documentation", author, "manual"),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages: list[tuple[str, str, str, list[str], int]] = [
    (master_doc, "sphinx", "Sphinx Documentation", [author], 1),
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents: list[tuple[str, str, str, str, str, str, str]] = [
    (
        master_doc,
        "Sphinx",
        "Sphinx Documentation",
        author,
        "Sphinx",
        "One line description of project.",
        "Miscellaneous",
    ),
]
