from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User:
    __tablename__ = 'temp'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(75), nullable=False)
    created_on = db.Column(db.DateTime)

    def __init__(self, user):
        self.user = user
        self.created_on = datetime.now()
