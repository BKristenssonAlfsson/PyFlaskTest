from sqlalchemy import String, Integer, Column
from .. import Base


class Role(Base):
    __tablename__ = 'role'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    role = Column(String(75), nullable=False)

    def __init__(self, role):
        self.role = role

    def __repr__(self):
        return '{} {}'.format(self.id, self.role)