import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    USERNAME = "sa"
    PASSWORD = "Paolino_93"
    DATABASE = "money_monitor_3"

    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "mssql+pyodbc://{user}:{pw}@localhost/{db}?driver={driver}".format(
        user=USERNAME,
        pw=PASSWORD,
        db=DATABASE,
        driver="ODBC Driver 17 for SQL Server".replace(" ", "+"))
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(
        user = 'postgres',
        password = 'postgres',
        host = 'localhost',
        port = '5432',
        dbname = 'money_monitor_3'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get("LOG_TO_STDOUT")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["danielcopelin@gmail.com"]
