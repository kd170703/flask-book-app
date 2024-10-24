import os
from sqlalchemy.orm import DeclarativeBase

basedir = os.path.abspath(os.path.dirname(__file__))

class Base(DeclarativeBase):
    pass

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'books.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False