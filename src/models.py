import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Person(Base):
  __tablename__ = 'person'
  # Here we define columns for the table person
  # Notice that each column is also a normal Python instance attribute.
  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)


class Address(Base):
  __tablename__ = 'address'
  # Here we define columns for the table address.
  # Notice that each column is also a normal Python instance attribute.
  id = Column(Integer, primary_key=True)
  street_name = Column(String(250))
  street_number = Column(String(250))
  post_code = Column(String(250), nullable=False)
  person_id = Column(Integer, ForeignKey('person.id'))
  person = relationship(Person)

  def to_dict(self):
    return {}


class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  user_Name = Column(String(100), unique=True)
  biography = Column(String(350))
  name = Column(String(100), index=True)
  email = Column(String(100), unique=True)


class Post(Base):
  __tablename__ = 'post'
  id = Column(Integer, primary_key=True)
  user_relationship = Column(Integer, ForeignKey('User.id'))
  user = relationship(User)


class Savedpost(Base):
  __tablename__ = 'savedpost'
  id = Column(Integer, primary_key=True)
  user_relarionship = Column(Integer, ForeignKey('user.id'))
  user = relationship(User)
  post_relationship = Column(Integer, ForeignKey('post.id'))
  post = relationship(Post)


class Followers(Base):
  __tablename__ = 'followers'
  id = Column(Integer, primary_key=True)
  user_relationship = Column(Integer, ForeignKey('user.id'))
  user = relationship(User)


class Comments(Base):
  __tablename__ = 'comments'
  id = Column(Integer, primary_key=True)
  description = Column(String(400))
  post_relationship = Column(Integer, ForeignKey('post.id'))
  post = relationship(Post)
  followers_relationship = Column(Integer, ForeignKey('followers.id'))
  followers = relationship(Followers)
  user_relationship = Column(Integer, ForeignKey('user.id'))
  user = relationship(User)


# Draw from SQLAlchemy base
try:
  result = render_er(Base, 'diagram.png')
  print("Success! Check the diagram.png file")
except Exception as e:
  print("There was a problem genering the diagram")
  raise e
