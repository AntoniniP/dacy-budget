import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_table.FormatTemplate as FormatTemplate
import pandas as pd
import dash_bootstrap_components as dbc


def layout(app):
    layout = html.Div([
        dbc.Row([
            dbc.Col(dcc.Input(id='input-1-description', type='text', value='Description'), md=4),
            dbc.Col(dcc.Input(id='input-3-default_currency', type='text', value='default_currency'), md=4),
            dbc.Col(dcc.Input(id='input-4-initial_balance', type='number', value='Amount'), md=4)
        ]),
        dbc.Row([
            dbc.Col(html.Button(id='submit-button-state', children='Submit')),
            dbc.Col(html.Div(id='output-state'))
        ]),
    ])
    return layout
