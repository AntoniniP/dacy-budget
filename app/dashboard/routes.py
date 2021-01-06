from . import bp
from flask import render_template
from flask_login import login_required
from dashapp import dash_transactions, dash_charts, dash_new_wallet


@bp.route("/transactions")
@login_required
def transactions_template():
    return render_template("transactions.html", dash_url=dash_transactions.url_base)


@bp.route("/charts")
@login_required
def charts_template():
    return render_template("charts.html", dash_url=dash_charts.url_base)


@bp.route("/new_wallet")
@login_required
def new_wallet_template():
    return render_template("new_wallet.html", dash_url=dash_new_wallet.url_base)
