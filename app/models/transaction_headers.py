from app import db


class TransactionHeader(db.Model):
    __tablename__ = 'transaction_headers'

    id = db.Column(db.BigInteger, primary_key=True)

    details = db.relationship("TransactionDetail", back_populates="transaction_headers")