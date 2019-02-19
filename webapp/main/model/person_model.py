from .. import Base
from sqlalchemy import String, Integer, DateTime, Column
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=False)
    created_on = Column(DateTime)
    role = Column(Integer, nullable=False)
    trooper = relationship('Role', uselist=False)

    def __init__(self, user, created_on, role):
        self.name = user
        self.created_on = created_on
        self.role = role

    def __repr__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.created_on, self.role)
