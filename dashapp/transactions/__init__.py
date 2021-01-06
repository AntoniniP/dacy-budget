def create_table(df):
    import dash_bootstrap_components as dbc

    return dbc.Table.from_dataframe(df.sort_values("added_date"), id="transaction_table", striped=True, bordered=True, hover=True)
