from app import db
from datetime import datetime


class TransactionHeader(db.Model):
    __tablename__ = 'transaction_headers'

    id = db.Column(db.BigInteger, primary_key=True)
    added_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    user = db.Column(db.Integer)

    details = db.relationship("TransactionDetail", back_populates="header")
