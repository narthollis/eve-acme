from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ...database import Base
from .alliance import Alliance


class Corporation(Base):
    __tablename__ = 'corporation'

    corporation_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    alliance_id = Column(Integer, ForeignKey('alliance.alliance_id'))

Alliance.corporations = relationship('Corporation', back_populates='alliance')
