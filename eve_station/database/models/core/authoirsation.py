from ...database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .users import User


class Authorisation(Base):
    __tablename__ = 'authorisation'

    authorisation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    character_owner_hash = Column(String, unique=True)

    user = relationship('User', back_populates='authorisations')

    def __repr__(self):
        return '<Authorisation(user_id={user_id!d}, character_owner_hash="{hash!s}")>'\
            .format(user_id=self.user_id, hash=self.character_owner_hash)

User.authorisations = relationship('Authorisation', back_populates='user')
