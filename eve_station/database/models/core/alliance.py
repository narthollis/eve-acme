from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ...database import Base


class Alliance(Base):
    alliance_id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    executor_corporation_id = Column(Integer, ForeignKey('corporation.corporation_id'))

    executor_corporation = relationship('Corporation')
