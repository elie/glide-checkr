from os import path

version = "1.5.0"


def setup(app):
    app.add_html_theme(
        'revealjs-checkr',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "revealjs-checkr")))
    app.add_html_theme(
        'handouts-checkr',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "handouts-checkr")))
