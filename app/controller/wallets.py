from sqlalchemy.exc import IntegrityError
import flask_login

def new_wallet(description, initial_balance, default_currency):
    from app import db
    from app.models.wallets import Wallet

    try:
        current_user = flask_login.current_user.id
        wallet = Wallet(
            description = description,
            initial_balance = initial_balance,
            default_currency = default_currency,
            user = current_user
        )
        db.session.add(wallet)
    except IntegrityError as e:
        print(e)
        db.session.rollback()
    else:
        db.session.commit()
