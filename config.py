"""Flask configuration variables."""
from os import environ, path
from dotenv import load_dotenv
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""
    SECRET_KEY = environ.get("SECRET_KEY")
    # Database
    db_credentials = f'{environ.get("DB_USER")}:{environ.get("DB_PASSWORD")}'
    db_host = f'{environ.get("DB_HOST")}:{environ.get("DB_PORT")}'
    if environ.get("DB_PASSWORD") is None:
        db_credentials = environ.get("DB_USER")
    if environ.get("DB_PORT") is None:
        db_host = environ.get("DB_HOST")
    db_string = f'{db_credentials}@{db_host}'
    if db_credentials is None or '' == db_credentials:
        db_string=db_host
    SQLALCHEMY_DATABASE_URI=(f'{environ.get("DB_TYPE")}://{db_string}/{environ.get("DATABASE")}')
    SQLALCHEMY_ECHO = False
    if "DB_CHANGES" in environ:
        SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("DB_CHANGES")
    else:
        SQLALCHEMY_TRACK_MODIFICATIONS = True
