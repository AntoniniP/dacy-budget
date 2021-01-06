from app import db
from datetime import datetime


class Wallet(db.Model):
    __tablename__ = 'wallets'

    id = db.Column(db.BigInteger, primary_key=True)
    added_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    
    description = db.Column(db.String(255))
    initial_balance = db.Column(db.Numeric(18,4))
    default_currency = db.Column(db.String(3))
    # user
    
    transactions = db.relationship("TransactionDetail", back_populates="wallet")
