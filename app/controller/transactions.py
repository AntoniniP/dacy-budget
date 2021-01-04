from sqlalchemy.exc import IntegrityError
import flask_login

def new_transaction():
    from app import db
    from ..models.transaction_details import TransactionDetail
    from ..models.transaction_headers import TransactionHeader  

    try:
        current_user = flask_login.current_user.id
        th = TransactionHeader(user=current_user)
        db.session.add(th)

        # transaction = Transaction(id=(datetime.now()), account=account, date=date, narration=narration, amount=amount)
        td = TransactionDetail(header=th)
        db.session.add(td)

    except IntegrityError as e:
        print(e)
        db.session.rollback()
    else:
        db.session.commit()