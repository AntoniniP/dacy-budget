from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_table
from flask_login import current_user
import pandas as pd
from collections import OrderedDict
from sqlalchemy.exc import IntegrityError
import dashapp.transactions.layout
from dash.exceptions import PreventUpdate
from datetime import date
from datetime import datetime
import dash_bootstrap_components as dbc
import app.controller.wallets as controller #import new_transaction


def register_callbacks(app):
    @app.callback(Output("output-state", "children"), 
                  [Input('submit-button-state', 'n_clicks')],
                  [State('input-1-description', 'value'), State('input-4-initial_balance', 'value'), State('input-3-default_currency', 'value')]
                  )
    def add_db(n_clicks, description, initial_balance, default_currency):
        if n_clicks is None or n_clicks==0:
            raise PreventUpdate
        else:
            controller.new_wallet(description, initial_balance, default_currency)
        
        return u'The Button has been pressed {} times.'.format(n_clicks)
