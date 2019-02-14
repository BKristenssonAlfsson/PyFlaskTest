from .config.postgres import postgres
from sqlalchemy import create_engine, orm
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from webapp.main.model import person_model
from .model.person_model import Person
from .model.role_model import Role

engine = create_engine(postgres)

Session = orm.sessionmaker(bind=engine)
session = Session()
engine.connect()

Base = declarative_base()

Base.metadata.create_all(engine)


def create_app():
    app = Flask(__name__)

    return app
