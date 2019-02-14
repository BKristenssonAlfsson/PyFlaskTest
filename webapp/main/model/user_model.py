from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, DateTime, Column

Base = declarative_base()


class User(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=False)
    created_on = Column(DateTime)
    role = Column(String(50), nullable=False)

    def __init__(self, user, created_on, role):
        self.name = user
        self.created_on = created_on
        self.role = role

    def __repr__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.created_on, self.role)
