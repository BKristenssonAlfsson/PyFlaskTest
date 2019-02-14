from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship, backref
from .role_model import Role

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column(String(75), nullable=False)
    created_on = Column(DateTime)
    role = Column(Integer, ForeignKey('role.id'), nullable=False)
    role_type = relationship(Role, backref('role.role'))

    def __init__(self, user, created_on, role):
        self.name = user
        self.created_on = created_on
        self.role = role

    def __repr__(self):
        return '{} {} {} {}'.format(self.id, self.name, self.created_on, self.role)
