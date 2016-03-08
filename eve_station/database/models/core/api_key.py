from ...database import Base
from sqlalchemy import Column, Integer, String

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from ...database import Base


class ApiKey(Base):
    api_key_id = Column(Integer, primary_key=True, autoincrement=False)
    key = Column(String)
    vcode = Column(String)

    mask = Column(Integer)

    character_1_id = Column(Integer, ForeignKey('character.character_id'))
    character_2_id = Column(Integer, ForeignKey('character.character_id'))
    character_3_id = Column(Integer, ForeignKey('character.character_id'))

    corporation_id = Column(Integer, ForeignKey('corporation.corporation_id'))
