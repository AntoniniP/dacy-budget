from app import db


class Wallet(db.Model):
    __tablename__ = 'wallets'

    id = db.Column(db.BigInteger, primary_key=True)
    description = db.Column(db.String(255))

    # details = db.relationship("TransactionDetail", back_populates="transaction_headers")