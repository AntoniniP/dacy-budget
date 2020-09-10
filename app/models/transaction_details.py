from app import db


class TransactionDetail(db.Model):
    __tablename__ = 'transaction_details'

    id = db.Column(db.BigInteger, primary_key=True)

    id_header = db.Column(db.BigInteger, db.ForeignKey('transaction_headers.id'))
    header = db.relationship("TransactionHeader", back_populates="transaction_details")

    date = db.Column(db.DateTime)
    amount = db.Column(db.Numeric(10, 2))


