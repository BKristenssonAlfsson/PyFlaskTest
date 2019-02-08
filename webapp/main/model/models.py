from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, DateTime, Column

Base = declarative_base()


class User(Base):
    __tablename__ = 'temp'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=False)
    created_on = Column(DateTime)

    def __init__(self, user, created_on):
        self.name = user
        self.created_on = created_on
        super(User, self).__init__()

    def __repr__(self):
        return '{} {} {}'.format(self.id, self.name, self.created_on)
