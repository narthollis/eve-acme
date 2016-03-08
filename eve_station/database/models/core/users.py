from ...database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    display_name = Column(String)

    def __repr__(self):
        return '<User(user_id={user_id!d}, display_name="{name!s}")>'.format(name=self.display_name)

    def __str__(self):
        return self.display_name
