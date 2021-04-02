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
    password = Column(String(250), nullable = False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

class Favorites_Planets(Base):
    __tablename__ = 'favorites_planets'     
    user_id = Column( Integer , ForeignKey('user.id'), primary_key = True)
    planet_id = Column( Integer , ForeignKey('planet.id'), primary_key = True)
    planet = relationship(Planet)
    user = relationship(User)
    
class Favorites_Characters(Base):
    __tablename__ = 'favorites_characters'     
    user_id = Column( Integer , ForeignKey('user.id'), primary_key = True)
    character_id = Column( Integer , ForeignKey('character.id'), primary_key = True)
    character = relationship(Character)
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')