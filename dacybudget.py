from flask_migrate import Migrate
from app import create_app, db

from app.models.users import User
from app.models.transactions import Transaction
from app.models.categories import Category
from app.models.transaction_details import TransactionDetail
from app.models.transaction_headers import TransactionHeader
from app.models.wallets import Wallet


app = create_app()


@app.shell_context_processor
def make_shell_context():
    """
    Required by Flask: register all database odbjects.
    """
    return dict(
        db=db,
        User=User,
        Transaction=Transaction,
        Category=Category,
        TransactionDetail=TransactionDetail,
        TransactionHeader=TransactionHeader,
        Wallet=Wallet
    )


if __name__ == "__main__":
    app.run(debug=True)
