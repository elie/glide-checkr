from os import path

version = "1.5.0"


def setup(app):
    app.add_html_theme(
        'revealjs-walmart',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "revealjs-walmart")))
    app.add_html_theme(
        'handouts-walmart',
        path.abspath(
            path.join(path.dirname(__file__), "themes", "handouts-walmart")))
