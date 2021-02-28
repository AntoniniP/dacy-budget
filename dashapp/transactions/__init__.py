def create_table(df):
    import dash_bootstrap_components as dbc

    return dbc.Table.from_dataframe(df.sort_values(by="added_date", ascending=False), id="transaction_table", striped=True, bordered=True, hover=True)
