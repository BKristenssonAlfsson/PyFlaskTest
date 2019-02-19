from .config.postgres import postgres
from sqlalchemy import create_engine, orm
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine(postgres)

Base.metadata.create_all(engine, checkfirst=True)
Session = orm.sessionmaker(bind=engine)
session = Session()

from .model import person_model
from .model import role_model


def create_app():
    app = Flask(__name__)

    return app
