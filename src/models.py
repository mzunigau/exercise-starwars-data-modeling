import os
import sys
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

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    id = Column(Integer, primary_key= True)
    type_media = Column(Enum)
    url = Column(String(250))
    post_id = Column( Integer , ForeignKey('post.id'))

class

#class Address(Base):
   # __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    

 
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')