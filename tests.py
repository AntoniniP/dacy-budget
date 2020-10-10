#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models.users import User
from app.models.transaction_headers import TransactionHeader
from app.models.transaction_details import TransactionDetail
from config import Config


class TestConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        # db.drop_all()
        self.app_context.pop()

    def test_transaction_creation(self):
        TH = TransactionHeader()
        db.session.add(TH)

        TD1 = TransactionDetail(header=TH, date='2020-12-31', amount=123.45)
        TD2 = TransactionDetail(header=TH, date='2020-12-31', amount=-123.45)
        db.session.add(TD1)
        db.session.add(TD2)

        db.session.commit()



    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
        db.session.add(u)
        db.session.commit()

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
