import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Folower(Base):
    __tablename__ = 'folower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(200))
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    comment_text = Column(String)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    url = Column(String, unique=True)
    type = Column(Enum)


# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
