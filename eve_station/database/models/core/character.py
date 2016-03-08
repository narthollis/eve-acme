from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ...database import Base
from .corporation import Corporation

class Character(Base):
    __tablename__ = 'character'

    character_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    corporation_id = Column(Integer, ForeignKey('corporation.corporation_id'))

    corporation = relationship('Corporation', back_populates='characters')

Corporation.characters = relationship('Character', back_populates='corporation')