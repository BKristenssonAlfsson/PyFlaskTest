from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'temp'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(75), nullable=False)
    created_on = db.Column(db.DateTime)

    def __init__(self, user, created_on):
        self.name = user
        self.created_on = created_on
        super(User, self).__init__()
