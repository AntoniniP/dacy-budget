import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_table.FormatTemplate as FormatTemplate
import pandas as pd
import dash_bootstrap_components as dbc
from .. import create_table


def layout(app):
    from app import db
    from app.models.transactions import Transaction

    with app.server.app_context():
        transactions = db.session.query(Transaction)
        df = pd.read_sql(transactions.statement, transactions.session.bind)

    row_input = [
        dbc.Col(dcc.Input(id='input-1-account', type='text', value='Account')),
        dbc.Col(dcc.DatePickerSingle(id='input-2-date')),
        dbc.Col(dcc.Input(id='input-3-narration', type='text', value='Narration')),
        dbc.Col(dcc.Input(id='input-4-amount', type='number', value='Amount')),
        dbc.Col(html.Div(html.Button(id='submit-button-state', children='Submit'))),
        dbc.Col(html.Div(id='output-state'))
    ]

    # row_submit = [
    #     dbc.Col(html.Button(id='submit-button-state', children='Submit'), width="auto"),
    #     dbc.Col(html.Div(id='output-state'), width="auto")
    # ]

    # layout = html.Div(
    #     # dbc.Row(row_input),
    #     # dbc.Row(row_submit),
    #     dbc.Row([dbc.Col(dbc.Card(
    #         dbc.CardBody([
    #             row_input,
    #             row_submit
    #         ])
    #     ))]),
    #     # dbc.Row([
    #     #     dbc.Col(html.Div(id='transactions-table', children=create_table(df)), width="auto")
    #     # ])
    # )

    layout = html.Div([
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        dbc.Row(row_input)#,
                        #row_submit
                    )
                )
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(id='transactions-table', children=create_table(df))
            )
        ])
    ])

    return layout
