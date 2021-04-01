import os
import sys
from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'    
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique = True)

class Follower(Base):
    __tablename__ = 'follower'
    user_to_id = Column(Integer,ForeignKey('user.id'), primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key= True)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = True)
    type_media = Column(String(250))
    url = Column(String(250))
    post_id = Column( Integer , ForeignKey('post.id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(250), nullable= False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')