from dash import Dash
from .dash_func import apply_layout_with_auth, _protect_dashviews
from dashapp.new_wallet.callbacks import register_callbacks
from dashapp.new_wallet.layout import layout
import dash_bootstrap_components as dbc


url_base = "/dash/new_wallet/"


def add_dash(server):
    meta_viewport = {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
    }
    external_stylesheets = [dbc.themes.BOOTSTRAP]  # ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
    app = Dash(
        server=server,
        url_base_pathname=url_base,
        # meta_tags=[meta_viewport],
        external_stylesheets=external_stylesheets,
    )
    app.url_base_pathname = url_base
    apply_layout_with_auth(app, layout(app))
    register_callbacks(app)
    _protect_dashviews(app)

    return app.server
