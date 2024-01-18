"""Initializes the DB"""
import os
import flask
import inspect
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String,DateTime,Numeric,Date,TIMESTAMP,func,Text,Time,ForeignKey,Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,query
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import as_declarative
from flask_sqlalchemy import SQLAlchemy

if flask.has_app_context():
    db = SQLAlchemy()
else:
    basedir = os.path.abspath(os.path.dirname(__file__)+'/../..')
    load_dotenv(os.path.join(basedir, ".env"))
    # Define variables DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
    db_credentials = os.environ.get('DB_USER')+':'+os.environ.get('DB_PASSWORD')
    if os.environ.get('DB_PASSWORD') in None:
        db_credentials = os.environ.get('DB_USER')
    if os.environ.get('DB_PORT') in None:
        db_host = os.environ.get('DB_HOST')
    db_string = db_credentials+'@'+db_host
    if db_credentials is None or '' == db_credentials:
        db_string=db_host
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_TYPE")+'://'+db_string+'/'+os.environ.get('DATABASE')

    engine=None
    Base=None
    Session=None
    session=None
    try:
        # ----- This is related code -----
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Base = declarative_base()
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        Session.configure(bind=engine)
        session=Session()
        # ----- This is related code -----
    except OperationalError as error:
        if "Connection refused" in str(error):
            print("server is not accessiable at this ip and port.")
        exit(1)

    # class Model(Base):
    #     query=query
    @as_declarative()
    class Base:
        def _asdict(self):
            return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    class db():
        Model=Base
        session=session
        Column=Column
        Integer=Integer
        String=String
        DateTime=DateTime
        Numeric=Numeric
        Date=Date
        TIMESTAMP=TIMESTAMP
        func=func
        Text=Text
        Time=Time
        Float=Float
        ForeignKey=ForeignKey
        relationship=relationship